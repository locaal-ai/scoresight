[Setup]
AppName=ScoreSight
AppVersion=@SCORESIGHT_VERSION@
DefaultDirName={pf}\ScoreSight
DefaultGroupName=ScoreSight
OutputDir=.\dist
OutputBaseFilename=scoresight-setup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "dist\scoresight\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\ScoreSight"; Filename: "{app}\scoresight.exe"

[Run]
Filename: "{app}\scoresight.exe"; Description: "Launch ScoreSight"; Flags: nowait postinstall skipifsilent
