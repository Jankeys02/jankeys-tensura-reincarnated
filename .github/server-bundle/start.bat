@echo off
rem First run installs the NeoForge server (needs Java 21), then every run starts it.
cd /d "%~dp0"

rem Warn about mods that can't be bundled (see MISSING-MODS.txt) and are not in mods yet.
set MISSING=
if exist required-mods.txt for /f "usebackq tokens=1,2,3 delims=|" %%a in ("required-mods.txt") do if not exist "mods\%%a" (
  echo [start] MISSING MOD: %%b - put %%a in the mods folder, download: %%c
  set MISSING=1
)
if defined MISSING (
  echo [start] The server will probably fail to start or reject players until these are added. Press Ctrl+C to stop, or
  timeout /t 10
)

if not exist libraries java -jar neoforge-installer.jar --installServer
call .un.bat nogui
