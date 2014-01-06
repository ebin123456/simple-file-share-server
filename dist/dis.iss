; -- Example2.iss --
; Same as Example1.iss, but creates its icon in the Programs folder of the
; Start Menu instead of in a subfolder, and also creates a desktop icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=File Share server
AppVersion=1.5
DefaultDirName={pf}\File Server
; Since no icons will be created in "{group}", we don't need the wizard
; to ask for a Start Menu folder name:
DisableProgramGroupPage=yes
UninstallDisplayIcon={app}\MyProg.exe
OutputDir=userdocs:Inno Setup Examples Output
ChangesEnvironment=yes
[Files]
Source: "fserver.exe"; DestDir: "{app}"
[Registry]
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{pf}\File Server";Check: NeedsAddPath('File Server')

[Code]

const
    ModPathName = 'modifypath';
    ModPathType = 'system';

function ModPathDir(): TArrayOfString;
begin
    setArrayLength(Result, 1)
    Result[0] := ExpandConstant('{app}');
end;



function NeedsAddPath(Param: string): boolean;

var
  OrigPath: string;
  Path:string;
  OldData:string;
  Check:Integer;
 
begin
  Log(Param)   ;
  Path := ExpandConstant('{app}');
  RegQueryStringValue(HKEY_LOCAL_MACHINE,'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'Path', OrigPath);
  Log(OrigPath);
  
  
  
  Log(Path);
  Result := Pos(Path, OrigPath) = 0; 
  if Result = False then  begin
  Log('ok');
  Result := False;
  exit;
  end;
  Result := True;
  exit;
  end;