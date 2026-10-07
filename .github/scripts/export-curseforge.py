"""Build a CurseForge modpack zip (manifest.json + overrides) from the packwiz/ mod list.
Usage: export-curseforge.py <version> <out.zip>
Blocked-from-API mods are fine here: the manifest only needs project/file IDs."""
import json, sys, tomllib, zipfile
from pathlib import Path

version, out = sys.argv[1], sys.argv[2]
pack = tomllib.loads(Path("packwiz/pack.toml").read_text(encoding="utf-8"))
files = []
for p in sorted(Path("packwiz").rglob("*.pw.toml")):
    m = tomllib.loads(p.read_text(encoding="utf-8"))
    if m.get("side") == "server":  # server-only mods stay out of the client pack
        continue
    cf = m["update"]["curseforge"]
    files.append({"projectID": cf["project-id"], "fileID": cf["file-id"], "required": True})
manifest = {
    "minecraft": {"version": pack["versions"]["minecraft"],
                  "modLoaders": [{"id": "neoforge-" + pack["versions"]["neoforge"], "primary": True}]},
    "manifestType": "minecraftModpack", "manifestVersion": 1,
    "name": pack["name"], "version": version, "author": "Jankeys",
    "files": files, "overrides": "overrides",
}
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("manifest.json", json.dumps(manifest, indent=2))
    for d in ("config", "defaultconfigs", "kubejs"):
        for f in sorted(Path(d).rglob("*")):
            if f.is_file():
                z.write(f, f"overrides/{f.as_posix()}")
print(f"{len(files)} mods -> {out}")
