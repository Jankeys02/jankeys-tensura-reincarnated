@echo off
rem Prism pre-launch. On the first run it sets up this repo (configs, quests, scripts); on every later run it pulls.
rem Then it syncs the mods with packwiz. A failed git step does not stop the launch.
rem Prism Pre-launch Command:  cmd /c .\pre-launch.bat   (the ".\" matters if Windows is set to not search the current folder)
rem Everything sits in one block so cmd has read the whole script before git can replace this file.
(
  if not exist .git (
    git init -q
    git config core.longpaths true
    git remote add origin https://github.com/Jankeys02/jankeys-tensura-reincarnated.git
    git fetch --no-tags origin main
    git checkout -f -B main origin/main
  ) else (
    git pull --ff-only --autostash
  )
  "%INST_JAVA%" -jar packwiz-installer-bootstrap.jar -s client https://raw.githubusercontent.com/Jankeys02/jankeys-tensura-reincarnated/main/packwiz/pack.toml
)
