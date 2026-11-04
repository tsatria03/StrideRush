; Stride Rush's Windows installer, ported from ToyMania's build/installer.iss (dev, 2026-11-04). tools.py's package stage
; compiles it with iscc, passing MyAppId, MyAppName, MyAppURL, MyAppExeName, MyAppPassword and MySourcePath from
; tools.ini; the version comes from version.txt beside this file.
#define MyAppVersion Trim(FileRead(FileOpen("version.txt")))
#define MyAppPublisher "tsatria03"
#define MyOutputFilename MyAppName + "_windows_installer_password_is_" + MyAppPassword

[Setup]
AppId={{{#MyAppId}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppPublisher}\{#MyAppName}\sdr
DefaultGroupName={#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin
UninstallDisplayName={#MyAppName} {#MyAppVersion}
AppMutex={#MyAppName}_Mutex
OutputDir=..\releases\archives
OutputBaseFilename={#MyOutputFilename}
Password={#MyAppPassword}
Encryption=yes
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"
Name: "startmenuicon"; Description: "Create a Start Menu shortcut"; GroupDescription: "Additional icons:"

[Files]
Source: "{#MySourcePath}\*"; \
  DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: startmenuicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; \
  Flags: nowait postinstall skipifsilent unchecked;
