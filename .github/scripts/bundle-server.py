"""Build the finished server zip: mods, configs, NeoForge installer, start scripts and a readme in one archive.
Usage: bundle-server.py <tag> <out.zip>
Mods come from the packwiz installer (-s server). Mods whose authors block downloads can't be fetched, so they are
not bundled: they are the project ids in .github/curseforge-required-deps.txt, listed in MISSING-MODS.txt and
attached as Required Dependencies on the CurseForge server file. The installer aborts on any blocked mod, so it is
given a temporary copy of packwiz/ without them. A blocked mod missing from that list fails the build with its name.
Needs Java on PATH and network access."""
import hashlib, re, shutil, subprocess, sys, tomllib, urllib.request, zipfile
from pathlib import Path

tag, out = sys.argv[1:3]
pack = tomllib.loads(Path("packwiz/pack.toml").read_text(encoding="utf-8"))
neo, mc, name = pack["versions"]["neoforge"], pack["versions"]["minecraft"], pack["name"]
srv = Path("srv-full")
shutil.rmtree(srv, ignore_errors=True)
srv.mkdir()


def lf(p):
    return p.read_bytes().decode("utf-8").replace("\r\n", "\n")


def fetch(url, dest):
    with urllib.request.urlopen(url, timeout=120) as r, open(dest, "wb") as w:
        shutil.copyfileobj(r, w)


for d in ("config", "defaultconfigs", "kubejs"):
    if Path(d).is_dir():
        shutil.copytree(d, srv / d)
for f in Path(".github/server-bundle").iterdir():
    text = lf(f).replace("@VERSION@", tag).replace("@NEOFORGE@", neo).replace("@MC@", mc).replace("{{PACK_NAME}}", name)
    if f.suffix == ".bat":  # Windows scripts need CRLF
        text = text.replace("\n", "\r\n")
    (srv / f.name).write_bytes(text.encode("utf-8"))

fetch("https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar",
      srv / "packwiz-installer-bootstrap.jar")
fetch(f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{neo}/neoforge-{neo}-installer.jar",
      srv / "neoforge-installer.jar")

deps = Path(".github/curseforge-required-deps.txt")
blocked = {l.split("#")[0].strip() for l in deps.read_text(encoding="utf-8").splitlines()} - {""} if deps.exists() else set()

# Temporary pack for the installer: blocked mods removed, index.toml and its hash in pack.toml updated.
tmp = Path("srv-pack")
shutil.rmtree(tmp, ignore_errors=True)
shutil.copytree("packwiz", tmp)
index = lf(tmp / "index.toml")
for f in sorted(tmp.rglob("*.pw.toml")):
    pid = str(tomllib.loads(lf(f)).get("update", {}).get("curseforge", {}).get("project-id", ""))
    if pid in blocked:
        rel = f.relative_to(tmp).as_posix()
        f.unlink()
        index = re.sub(r'\[\[files\]\]\nfile = "' + re.escape(rel) + r'"\n(?:(?!\[\[files\]\]).*\n?)*', "", index)
(tmp / "index.toml").write_bytes(index.encode("utf-8"))
digest = hashlib.sha256(index.encode("utf-8")).hexdigest()
pt = re.sub(r'(\[index\][^\[]*?hash = ")[0-9a-f]+(")', rf"\g<1>{digest}\g<2>", lf(tmp / "pack.toml"))
(tmp / "pack.toml").write_bytes(pt.encode("utf-8"))

r = subprocess.run(["java", "-jar", "packwiz-installer-bootstrap.jar", "-g", "-s", "server", (tmp / "pack.toml").resolve().as_uri()],
                   cwd=srv, stdin=subprocess.DEVNULL, timeout=3600, check=False)
if r.returncode:
    sys.exit(f"The packwiz installer failed (exit {r.returncode}). If it names a blocked mod, "
             "add its CurseForge project id to .github/curseforge-required-deps.txt.")
(srv / "packwiz-installer-bootstrap.jar").unlink(missing_ok=True)
(srv / "packwiz.json").unlink(missing_ok=True)
(srv / "packwiz-installer.jar").unlink(missing_ok=True)

have = {p.name for p in (srv / "mods").glob("*")} if (srv / "mods").is_dir() else set()
missing, required = [], []
for p in sorted(Path("packwiz").rglob("*.pw.toml")):
    m = tomllib.loads(lf(p))
    if m.get("side") == "client" or p.parent.name != "mods":
        continue
    if m.get("filename") not in have:
        pid = str(m.get("update", {}).get("curseforge", {}).get("project-id", ""))
        if pid not in blocked:
            sys.exit(f"{m.get('name', p.stem)} was not installed and is not in curseforge-required-deps.txt")
        missing.append(f"{m.get('name', p.stem)}: https://www.curseforge.com/projects/{pid}")
        required.append(f"{m.get('filename')}|{m.get('name', p.stem)}|https://www.curseforge.com/projects/{pid}")
(srv / "required-mods.txt").write_text("".join(r + "\n" for r in required), encoding="utf-8")  # read by start.sh / start.bat
(srv / "MISSING-MODS.txt").write_text(
    "Mods that could not be bundled (their authors block downloads outside CurseForge).\n"
    "Download each file from its link and put it in the mods folder before the first start.\n\n"
    + ("\n".join(missing) if missing else "None: every mod is in the mods folder.") + "\n", encoding="utf-8")

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(srv.rglob("*")):
        if f.is_file():
            z.write(f, f.relative_to(srv).as_posix())
print(f"{len(have)} mods bundled, {len(missing)} missing -> {out} ({Path(out).stat().st_size // 1_000_000} MB)")
