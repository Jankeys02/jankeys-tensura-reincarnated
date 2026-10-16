"""Download the packwiz command-line tool into ./packwiz-bin (ignored by git). Usage: python .github/scripts/install-packwiz.py
Then run it from the packwiz/ folder as ../packwiz-bin/packwiz (Windows: ..\packwiz-bin\packwiz.exe),
or add packwiz-bin to your PATH. Builds come from packwiz's own CI (nightly.link); there are no official release files."""
import io, platform, stat, sys, urllib.request, zipfile
from pathlib import Path

BASE = "https://nightly.link/packwiz/packwiz/workflows/go/main/"
os_name = platform.system()
art = {"Windows": "Windows%2064-bit", "Linux": "Linux%2064-bit%20x86", "Darwin": "macOS%2064-bit%20x86"}.get(os_name)
if not art:
    sys.exit(f"No packwiz build for {os_name}; install it with: go install github.com/packwiz/packwiz@latest")
dest = Path("packwiz-bin")
dest.mkdir(exist_ok=True)
with urllib.request.urlopen(BASE + art + ".zip", timeout=60) as r:
    zipfile.ZipFile(io.BytesIO(r.read())).extractall(dest)
for f in dest.iterdir():
    f.chmod(f.stat().st_mode | stat.S_IEXEC)
print("Installed to", dest.resolve(), "->", ", ".join(p.name for p in dest.iterdir()))
