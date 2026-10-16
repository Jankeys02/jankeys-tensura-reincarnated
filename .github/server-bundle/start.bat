@echo off
rem First run installs the NeoForge server (needs Java 21), then every run starts it.
cd /d "%~dp0"
if not exist libraries java -jar neoforge-installer.jar --installServer
call run.bat nogui
