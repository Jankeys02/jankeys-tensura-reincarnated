@echo off
rem Downloads/updates the server's mods to match this release. Run again after every update.
java -jar packwiz-installer-bootstrap.jar -g -s server @PACK_URL@
pause
