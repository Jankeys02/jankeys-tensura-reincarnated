@echo off
rem Prism pre-launch: update this repo (configs, quests, scripts), then sync the mods with packwiz.
rem Set the Pre-launch Command in Prism to:  cmd /c pre-launch.bat
rem A failed git pull (for example local edits in the way) does not stop the launch.
git pull --ff-only --autostash
"%INST_JAVA%" -jar packwiz-installer-bootstrap.jar -s client https://raw.githubusercontent.com/Jankeys02/jankeys-tensura-reincarnated/main/packwiz/pack.toml
exit /b %errorlevel%
