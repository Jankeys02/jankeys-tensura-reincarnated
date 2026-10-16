"""List top-level folders/files that the whitelist .gitignore hides, except known runtime ones.
Usage: python .github/scripts/doctor.py
If something listed is pack content (not a world, log or downloaded mod), add `!/name/` to .gitignore."""
import subprocess

RUNTIME = {
    "mods", "saves", "logs", "crash-reports", "screenshots", "shaderpacks", "resourcepacks", "downloads",
    "essential", "local", "kb", "packwiz-bin", "options.txt", "usercache.json", "usernamecache.json",
    "command_history.txt", "minecraftinstance.json", "packwiz-installer-bootstrap.jar", "packwiz-installer.jar",
    "servers.dat", "servers.dat_old", "options.txt.old", "realms_persistence.json", "eula.txt", "journeymap",
    "xaero", "XaeroWaypoints", "XaeroWorldMap", "backups", "debug", ".curseclient", ".mixin.out", "mods.bak",
}
out = subprocess.run(["git", "status", "--ignored", "--short"], capture_output=True, text=True).stdout
hidden = [l[3:].strip('"').rstrip("/") for l in out.splitlines() if l.startswith("!! ") and "/" not in l[3:].rstrip("/")]
odd = [h for h in hidden if h not in RUNTIME and not h.startswith(".")]
if odd:
    print("Ignored by .gitignore (add `!/name/` if it is pack content):", ", ".join(sorted(odd)))
else:
    print("doctor: no unexpected ignored top-level entries.")
