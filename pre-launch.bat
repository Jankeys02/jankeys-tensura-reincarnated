@echo off
setlocal enabledelayedexpansion
rem Prism pre-launch. On the first run it sets up this repo (configs, quests, scripts); on every later run it pulls.
rem If the pull brought changes, a window lists what changed (commits, added/removed/updated mods).
rem Then it downloads the packwiz installer if it is missing and syncs the mods. A failed git step does not stop the launch.
rem Prism Pre-launch Command:  cmd /c .\pre-launch.bat   (the ".\" matters if Windows is set to not search the current folder)
rem Everything sits in one block so cmd has read the whole script before git can replace this file.
(
  set OLD=
  if exist .git for /f %%i in ('git rev-parse HEAD 2^>nul') do set OLD=%%i
  if not exist .git (
    git init -q
    git config core.longpaths true
    git remote add origin https://github.com/Jankeys02/jankeys-tensura-reincarnated.git
    git fetch --no-tags origin main
    git checkout -f -B main origin/main
  ) else (
    git pull --ff-only --autostash
  )
  set NEW=
  for /f %%i in ('git rev-parse HEAD 2^>nul') do set NEW=%%i
  if defined OLD if not "!OLD!"=="!NEW!" start "" powershell -NoProfile -WindowStyle Hidden -Command "$o=$env:OLD;$n=$env:NEW;$r=$o+'..'+$n;$nl=[Environment]::NewLine;$l=@(git log --format='- %%s' -n 15 $r);$m=@(git diff --name-status $o $n -- packwiz/mods packwiz/resourcepacks packwiz/shaderpacks | ForEach-Object { $x=$_ -split [char]9; $nm=[IO.Path]::GetFileNameWithoutExtension([IO.Path]::GetFileNameWithoutExtension($x[1])); switch ($x[0]) { 'A' {'+ added: '+$nm} 'D' {'- removed: '+$nm} default {'~ updated: '+$nm} } });$s='The pack was updated since your last launch.'+$nl+$nl+'Changes:'+$nl+($l -join $nl);if ($m.Count) {$s+=$nl+$nl+'Mods and packs:'+$nl+($m -join $nl)};Add-Type -AssemblyName PresentationFramework;[void][Windows.MessageBox]::Show($s,'Pack updated')"
  if not exist packwiz-installer-bootstrap.jar curl -fsSL -o packwiz-installer-bootstrap.jar https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar
  "%INST_JAVA%" -jar packwiz-installer-bootstrap.jar -s client https://raw.githubusercontent.com/Jankeys02/jankeys-tensura-reincarnated/main/packwiz/pack.toml
)
