"""Writes sdr/data/lang/template.lng, every line the game speaks as English=English, and reports what each language
file in sdr/data/lang is missing.

The lines come from four places, each under its own // heading:
- the code in src: the text passed to the speaking calls (speak, speak_buffer, dialogs, menu items, form captions,
  menu intros, list lines). A plain string becomes an exact line; text joined with values ("You have run " + steps +
  " steps.") becomes a wildcard line, a * for each value and $1, $2 in the translation. Text built some other way (a
  variable alone, a string built across functions) can't be read here, and is listed as flagged for a hand-written
  line. The debug options (functions after a "DEBUG OPTION" comment) are left out, since players never see them.
- achievements.ini: each achievement's name, description (its %threshold% as a *) and hint.
- the documents: each document's name, as the documentation menu says it.
- the sound folders: names the game reads from folders (environments, obstacle, item and weapon names).

template.lng is rewritten in full each run. The language files are never touched; each is compared with the template:
missing lines (in the template, not the file) and stale lines (in the file, no longer in the template).

Usage: python build/lang_template.py [--details], or double-click build/lang_template.bat, which runs it with --details
and waits for a key so the report stays on screen.
"""
import os
import re
import sys

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.abspath(os.path.join(BUILD_DIR, ".."))
SRC_DIR = os.path.join(REPO_DIR, "src")
SDR_DIR = os.path.join(REPO_DIR, "sdr")
LANG_DIR = os.path.join(SDR_DIR, "data", "lang")
TEMPLATE = os.path.join(LANG_DIR, "template.lng")
ACHIEVEMENTS_INI = os.path.join(SDR_DIR, "data", "config", "game", "achievements.ini")
DOCKS_DIR = os.path.join(SDR_DIR, "docks", "lang", "english")
SOUNDS_DIR = os.path.join(SDR_DIR, "sounds", "game")

# Each speaking call, and which argument holds its text (0 is the first).
CALLS = {
    "speak": 0, "speak_buffer": 0, "speak_interrupt": 0, "dlg": 0, "dlgmessage": 0, "dlgmessage_return": 0,
    "translate": 0, "add_item": 0, "add_item_to_tab": 1, "add_list_item": 1, "add_tab": 0, "create_window": 0,
    "create_checkbox": 0, "create_button": 0, "create_list": 0, "create_slider": 0, "create_input_box": 0,
    "create_status_bar": 0, "create_tab_panel": 0, "insert_last": 0,
    "stat_line": 0, "add_count_line": 3,  # a statistic's label, spoken as "label, value" (the general "*, *" line)
}
# Lines no single call shows, tried by the game only after every closer line: a statistic, "label, value".
GENERAL_LINES = ["*, *"]
CALL_RE = re.compile(r"\b(" + "|".join(CALLS) + r")\s*\(")
INTRO_RE = re.compile(r"\bintro_text\s*\+?=\s*")
RETURN_RE = re.compile(r"\breturn\s+")
MAX_VARIANTS = 8
# The plain heading each code file's lines get in the language files, so they never show the game's file names.
SECTION_TITLES = {
    "ammo": "Ammo packs", "capsule": "Life capsules", "door": "Doors and keys", "goldpack": "Gold packs",
    "playerstats": "Player stats", "potion": "Health potions", "powerup": "Powerups", "shield": "Steel shields",
    "specials": "Player shop specials", "teleporter": "Player teleporters", "buffer": "Speech buffers",
    "dlg": "Dialogs", "downloader": "Downloads", "form": "Form controls", "form_menu": "Menu controls",
    "ini": "Configuration files", "key_config": "Key bindings", "rotation": "Directions", "speech": "Speech",
    "virtual_dialogs": "Input boxes", "achievements": "Achievement announcements", "difficulty": "Difficulty",
    "endrun": "Run endings", "environments": "Environments", "freebelt": "Free run belt",
    "freerun": "Free run console", "game": "Run readouts", "heartbeat": "Heartbeat", "inventory": "Inventory",
    "joystick": "Joystick", "lane": "Lanes", "lives": "Health and lives", "practice": "Practice runs",
    "practice_hints": "Practice hints", "timerun": "Timed runs", "updater": "Updates", "weapons": "Weapons",
    "achievements_menu": "Achievements menu", "bindings_menu": "Key bindings menu",
    "learn_sounds_menu": "Learn sounds menu", "menu": "Main and game menus", "pause_menu": "Pause menu",
    "results_menu": "Session results", "settings_menu": "Settings menu", "shop_menu": "Player shop",
    "stats_menu": "Statistics menu",
}


def section_title(rel):
    """The plain heading for a code file's lines; a new file gets its name in words until it's added above."""
    name = os.path.splitext(os.path.basename(rel))[0]
    return SECTION_TITLES.get(name, name.replace("_", " ").capitalize())


def strip_comments(code):
    """Blanks out // and /* */ comments (keeping line breaks, so line numbers hold), leaving strings alone. Returns the
    code and the positions where a DEBUG OPTION comment started."""
    out = []
    debug_marks = []
    i, n = 0, len(code)
    while i < n:
        c = code[i]
        if c == '"':
            j = i + 1
            while j < n and code[j] != '"':
                j += 2 if code[j] == "\\" else 1
            out.append(code[i:j + 1])
            i = j + 1
        elif code.startswith("//", i):
            j = code.find("\n", i)
            j = n if j < 0 else j
            out.append(" " * (j - i))
            i = j
        elif code.startswith("/*", i):
            j = code.find("*/", i + 2)
            j = n if j < 0 else j + 2
            if code.startswith("DEBUG OPTION", i + 2) or code[i + 2:i + 20].strip().startswith("DEBUG OPTION"):
                debug_marks.append(i)
            out.append(re.sub(r"[^\n]", " ", code[i:j]))
            i = j
        else:
            out.append(c)
            i += 1
    return "".join(out), debug_marks


def debug_ranges(code, marks):
    """The span of each function body that follows a DEBUG OPTION comment."""
    ranges = []
    for m in marks:
        start = code.find("{", m)
        if start < 0:
            continue
        depth, j = 0, start
        while j < len(code):
            if code[j] == '"':
                j = skip_string(code, j)
                continue
            if code[j] == "{":
                depth += 1
            elif code[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        ranges.append((m, j))
    return ranges


def skip_string(code, i):
    j = i + 1
    while j < len(code) and code[j] != '"':
        j += 2 if code[j] == "\\" else 1
    return j + 1


def split_top(expr, sep):
    """Splits expr on sep where it isn't inside a string or brackets."""
    parts, depth, cur, i = [], 0, [], 0
    while i < len(expr):
        c = expr[i]
        if c == '"':
            j = skip_string(expr, i)
            cur.append(expr[i:j])
            i = j
            continue
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        if depth == 0 and expr.startswith(sep, i):
            parts.append("".join(cur))
            cur = []
            i += len(sep)
            continue
        cur.append(c)
        i += 1
    parts.append("".join(cur))
    return parts


def call_args(code, open_paren):
    """The arguments of the call whose ( is at open_paren, and where the call ends."""
    depth, i = 0, open_paren
    while i < len(code):
        c = code[i]
        if c == '"':
            i = skip_string(code, i)
            continue
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return split_top(code[open_paren + 1:i], ","), i
        i += 1
    return [], len(code)


def unescape(body):
    return body.replace('\\"', '"').replace("\\\\", "\\").replace("\\t", "\t").replace("\\r", "\r").replace("\\n", "\n")


def literal(part):
    """The text of a part that is only a string literal (with an optional .format(...)), else None."""
    part = part.strip()
    m = re.fullmatch(r'"((?:[^"\\]|\\.)*)"(\s*\.\s*format\s*\(.*\))?', part, re.S)
    if not m:
        return None
    text = unescape(m.group(1))
    if m.group(2):
        text = re.sub(r"%\d", "*", text)
    return text


def wrapped(expr):
    """Whether expr is one bracketed whole, its first ( closed by its last )."""
    if not (expr.startswith("(") and expr.endswith(")")):
        return False
    depth, i = 0, 0
    while i < len(expr):
        c = expr[i]
        if c == '"':
            i = skip_string(expr, i)
            continue
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return i == len(expr) - 1
        i += 1
    return False


def variants(expr):
    """Every text an expression can speak, with a * for each value. Returns [] if it holds no text at all."""
    expr = expr.strip()
    while wrapped(expr):
        expr = expr[1:-1].strip()
    q = split_top(expr, "?")
    if len(q) == 2:
        branches = split_top(q[1], ":")
        if len(branches) == 2:
            return (variants(branches[0]) or ["*"]) + (variants(branches[1]) or ["*"])
    results = [""]
    any_text = False
    for part in split_top(expr, "+"):
        text = literal(part)
        if text is not None:
            options = [text]
            any_text = True
        else:
            inner = part.strip()
            if wrapped(inner) and "?" in inner:
                options = variants(inner) or ["*"]
                any_text = any_text or any(o != "*" for o in options)
            else:
                options = ["*"]
        results = [r + o for r in results for o in options][:MAX_VARIANTS]
    if not any_text:
        return []
    return [re.sub(r"\*(\*)+", "*", r) for r in results]


def good_line(text):
    """Whether text can be a .lng line: it has letters, isn't a path or file name, and has no = or line break."""
    t = text.strip()
    if not re.search(r"[A-Za-z]", t) or "=" in t or "\n" in t or "\r" in t:
        return False
    if "/" in t or "\\" in t or re.search(r"\.(ogg|wav|mp3|txt|ini|lng|srf|nvgt|exe|dat)\b", t):
        return False
    if t.startswith("Debug run."):
        return False
    # A value glued to a word ("*logs", "runs_*") or an identifier is a name being built, not speech, and a line
    # starting with punctuation is a piece of a longer one.
    if "_" in t or re.search(r"[A-Za-z0-9]\*|\*[A-Za-z0-9]", t) or t[0] in ",.;:+":
        return False
    return True


def add_line(lines, seen, text):
    t = text.strip()
    if t in seen or not good_line(t):
        return
    seen.add(t)
    lines.append(t)


def scan_code():
    """The code's lines, grouped by file, and the flagged calls."""
    groups, flagged, seen = [], [], set()
    files = []
    for root, _, names in os.walk(SRC_DIR):
        for name in names:
            if name.endswith(".nvgt") and name != "version.nvgt":
                files.append(os.path.join(root, name))
    files.sort(key=lambda p: os.path.relpath(p, SRC_DIR).replace("\\", "/"))
    for path in files:
        rel = os.path.relpath(path, SRC_DIR).replace("\\", "/")
        with open(path, encoding="utf-8", errors="replace") as f:
            code, marks = strip_comments(f.read())
        skip = debug_ranges(code, marks)
        found = []
        exprs = []
        for m in CALL_RE.finditer(code):
            args, _ = call_args(code, m.end() - 1)
            index = CALLS[m.group(1)]
            if index < len(args):
                exprs.append((m.start(), args[index], m.group(1)))
        for m in INTRO_RE.finditer(code):
            end = code.find(";", m.end())
            exprs.append((m.start(), code[m.end():end], "intro_text"))
        for m in RETURN_RE.finditer(code):
            end = code.find(";", m.end())
            if '"' in code[m.end():end]:
                exprs.append((m.start(), code[m.end():end], "return"))  # a function that builds a line to speak
        exprs.sort()
        for pos, expr, call in exprs:
            if any(a <= pos <= b for a, b in skip):
                continue
            texts = variants(expr)
            if not texts:
                e = expr.strip()
                definition = re.match(r"(const\s+)?(string|int|bool|double|float|uint)\b", e) or "&" in e
                if call not in ("insert_last", "translate", "add_list_item", "return") and e and not e.isdigit() and not definition:
                    flagged.append("%s:%d %s(%s)" % (rel, code.count("\n", 0, pos) + 1, call, " ".join(e.split())[:70]))
                continue
            for t in texts:
                if call in ("insert_last", "return") and "*" not in t and " " not in t.strip():
                    continue  # a single word put in a list or returned is more likely a name or key than speech
                if call.startswith("create_"):
                    t = t.replace("&", "")  # a caption's & marks its Alt shortcut letter and isn't spoken
                add_line(found, seen, t)
        if rel.endswith("deps/form.nvgt"):
            # The control type names, spoken after each caption, also as type_to_name() puts them for a disabled or
            # read-only control.
            names = re.findall(r'\bname\s*=\s*"([^"]+)"\s*;', code)
            for name in names + ["Read Only " + n for n in names] + ["Disabled " + n for n in names]:
                add_line(found, seen, name)
        if found:
            groups.append((rel, found))
    return groups, flagged, seen


def scan_achievements(seen):
    lines = []
    if not os.path.exists(ACHIEVEMENTS_INI):
        return lines
    with open(ACHIEVEMENTS_INI, encoding="utf-8", errors="replace") as f:
        for row in f:
            m = re.match(r"\s*(name|description|hint)\s*=\s*(.*?)\s*$", row)
            if m:
                add_line(lines, seen, m.group(2).replace("%threshold%", "*"))
                if m.group(1) == "name":
                    add_line(lines, seen, m.group(2).lower())  # the progress lines say it in lower case
    return lines


def scan_documents(seen):
    lines = []
    for section in ("game", "main"):
        folder = os.path.join(DOCKS_DIR, section)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if name.endswith(".txt"):
                add_line(lines, seen, name[:-4].replace("_", " "))
    return lines


def scan_languages(seen):
    """The language names the settings and the documentation menu list, from the .lng files and the docks folders."""
    names = set()
    for name in os.listdir(LANG_DIR):
        if name.endswith(".lng") and name != "template.lng":
            names.add(name[:-4].lower())
    docks_lang = os.path.dirname(DOCKS_DIR)
    if os.path.isdir(docks_lang):
        names.update(d for d in os.listdir(docks_lang) if os.path.isdir(os.path.join(docks_lang, d)))
    lines = []
    for name in ["fallback"] + sorted(names):
        add_line(lines, seen, name)
    return lines


def scan_sound_folders(seen):
    names = set()
    envs = os.path.join(SOUNDS_DIR, "environments")
    if os.path.isdir(envs):
        for env in os.listdir(envs):
            names.add(env)
            for root, dirs, _ in os.walk(os.path.join(envs, env)):
                parts = os.path.relpath(root, os.path.join(envs, env)).replace("\\", "/").split("/")
                if parts[0] in ("audio", "platforms") or "countdown" in parts:
                    continue
                for d in dirs:
                    if d not in ("general", "countdown"):
                        names.add(d)
    for kind in ("items", "weapons"):
        base = os.path.join(SOUNDS_DIR, "equipments", kind)
        if os.path.isdir(base):
            for group in os.listdir(base):
                names.add(group)
                if os.path.isdir(os.path.join(base, group)):
                    names.update(os.listdir(os.path.join(base, group)))
    lines = []
    for name in sorted(names):
        if os.path.splitext(name)[1]:
            continue  # a file, not a folder
        add_line(lines, seen, name.replace("_", " "))
    return lines


def translation_of(english):
    """English=English, with each * as $1, $2 on the right."""
    count = [0]

    def number(_):
        count[0] += 1
        return "$%d" % count[0]
    return english + "=" + re.sub(r"\*", number, english)


def read_lng(path):
    keys = []
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        for row in f:
            row = row.strip()
            if not row or row.startswith("//"):
                continue
            eq = row.find("=")
            if eq > 0 and row[:eq].strip() and row[eq + 1:].strip():
                keys.append(row[:eq].strip())
    return keys


def main():
    details = "--details" in sys.argv
    groups, flagged, seen = scan_code()
    sections = [("// " + section_title(rel), found) for rel, found in groups]
    for heading, found in (("// Achievement names, descriptions and hints", scan_achievements(seen)),
                           ("// Document names", scan_documents(seen)),
                           ("// Language names", scan_languages(seen)),
                           ("// Environment, obstacle, item and weapon names", scan_sound_folders(seen))):
        if found:
            sections.append((heading, found))
    general = [t for t in GENERAL_LINES if t not in seen]
    if general:
        sections.append(("// General lines, tried last: a statistic is spoken as label, value", general))
    out = ["// Stride Rush language template: every line the game speaks.",
           "// Copy this file to <language>.lng and change only the text after each =. A * stands for a value,",
           "// which $1, $2 and on place in your translation. Lines you leave out are spoken in English.", ""]
    total = 0
    for heading, found in sections:
        out.append(heading)
        out.extend(translation_of(t) for t in found)
        out.append("")
        total += len(found)
    with open(TEMPLATE, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))
    print("template.lng: %d lines in %d groups." % (total, len(sections)))
    template_keys = set(t for _, found in sections for t in found)
    for name in sorted(os.listdir(LANG_DIR)):
        if not name.endswith(".lng") or name == "template.lng":
            continue
        keys = read_lng(os.path.join(LANG_DIR, name))
        missing = [k for _, found in sections for k in found if k not in set(keys)]
        stale = [k for k in keys if k not in template_keys]
        print("%s: %d lines, %d missing, %d no longer in the game." % (name, len(keys), len(missing), len(stale)))
        if details:
            for k in stale:
                print("  stale: " + k)
    print("Flagged, text built where the script can't read it (%d): write these lines by hand if needed." % len(flagged))
    if details:
        for item in flagged:
            print("  " + item)


if __name__ == "__main__":
    main()
