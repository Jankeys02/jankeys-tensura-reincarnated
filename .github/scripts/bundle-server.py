"""Build the finished server zip: mods, configs, NeoForge installer, start scripts and a readme in one archive.
Usage: bundle-server.py <tag> <out.zip> <pack.toml URL>
Mods come from the packwiz installer (-s server). Mods whose authors block downloads can't be fetched, so they
are not bundled: they are listed in MISSING-MODS.txt (and should be Required Dependencies on the CurseForge file).
Needs Java on PATH and network access."""
import shutil, subprocess, sys, tomllib, urllib.request, zipfile
from pathlib import Path

tag, out, pack_url = sys.argv[1:4]
pack = tomllib.loads(Path("packwiz/pack.toml").read_text(encoding="utf-8"))
neo, mc, name = pack["versions"]["neoforge"], pack["versions"]["minecraft"], pack["name"]
srv = Path("srv-full")
shutil.rmtree(srv, ignore_errors=True)
srv.mkdir()

for d in ("config", "defaultconfigs", "kubejs"):
    if Path(d).is_dir():
        shutil.copytree(d, srv / d)
for f in Path(".github/server-bundle").iterdir():
    text = f.read_text(encoding="utf-8").replace("@VERSION@", tag).replace("@NEOFORGE@", neo).replace("@MC@", mc)
    (srv / f.name).write_text(text.replace("{{PACK_NAME}}", name), encoding="utf-8", newline="\n")
    if f.suffix == ".bat":  # Windows scripts need CRLF
        (srv / f.name).write_bytes(text.replace("{{PACK_NAME}}", name).replace("\n", "\r\n").encode("utf-8"))


def fetch(url, dest):
    with urllib.request.urlopen(url, timeout=120) as r, open(dest, "wb") as w:
        shutil.copyfileobj(r, w)


fetch("https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar",
      srv / "packwiz-installer-bootstrap.jar")
fetch(f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{neo}/neoforge-{neo}-installer.jar",
      srv / "neoforge-installer.jar")

# Blocked mods make the installer report failures; that is expected, so the exit code is not checked.
subprocess.run(["java", "-jar", "packwiz-installer-bootstrap.jar", "-g", "-s", "server", pack_url],
               cwd=srv, stdin=subprocess.DEVNULL, timeout=3600, check=False)
(srv / "packwiz-installer-bootstrap.jar").unlink(missing_ok=True)
(srv / "packwiz.json").unlink(missing_ok=True)

have = {p.name for p in (srv / "mods").glob("*")} if (srv / "mods").is_dir() else set()
missing = []
for p in sorted(Path("packwiz").rglob("*.pw.toml")):
    m = tomllib.loads(p.read_text(encoding="utf-8"))
    if m.get("side") == "client" or p.parent.name != "mods":
        continue
    if m.get("filename") not in have:
        pid = m.get("update", {}).get("curseforge", {}).get("project-id", "")
        missing.append(f"{m.get('name', p.stem)}: https://www.curseforge.com/projects/{pid}")
(srv / "MISSING-MODS.txt").write_text(
    "Mods that could not be bundled (their authors block downloads outside CurseForge).\n"
    "Download each file from its link and put it in the mods folder before the first start.\n\n"
    + ("\n".join(missing) if missing else "None: every mod is in the mods folder.") + "\n", encoding="utf-8")

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(srv.rglob("*")):
        if f.is_file():
            z.write(f, f.relative_to(srv).as_posix())
print(f"{len(have)} mods bundled, {len(missing)} missing -> {out} ({Path(out).stat().st_size // 1_000_000} MB)")
