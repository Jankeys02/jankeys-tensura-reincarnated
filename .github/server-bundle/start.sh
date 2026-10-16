#!/bin/sh
# First run installs the NeoForge server (needs Java 21), then every run starts it.
cd "$(dirname "$0")"

# Warn about mods that can't be bundled (see MISSING-MODS.txt) and are not in mods/ yet.
if [ -f required-mods.txt ]; then
  missing=
  while IFS='|' read -r file name link; do
    [ -f "mods/$file" ] || { echo "[start] MISSING MOD: $name - put $file in mods/ (download: $link)"; missing=1; }
  done < required-mods.txt
  [ -n "$missing" ] && echo "[start] The server will probably fail to start or reject players until these are added. Continuing in 10 seconds (Ctrl+C to stop)." && sleep 10
fi

[ -d libraries ] || java -jar neoforge-installer.jar --installServer
sh run.sh nogui
