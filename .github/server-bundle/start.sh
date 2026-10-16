#!/bin/sh
# First run installs the NeoForge server (needs Java 21), then every run starts it.
cd "$(dirname "$0")"
[ -d libraries ] || java -jar neoforge-installer.jar --installServer
sh run.sh nogui
