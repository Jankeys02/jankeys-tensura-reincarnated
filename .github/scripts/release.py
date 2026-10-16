"""Cut a release: bump package.json, date the [Unreleased] changelog section, commit and tag.
Usage: python .github/scripts/release.py X.Y.Z[-rc.1] [--push]
Without --push it stops after the local commit and tag, so you can look first.
Pushing the tag starts the release workflow. Admins can push main directly; otherwise open a PR for the commit."""
import datetime, json, re, subprocess, sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if len(args) != 1 or not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.]+)?", args[0]):
    sys.exit(__doc__)
v, push = args[0], "--push" in sys.argv


def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"git {' '.join(a)} failed: {r.stderr.strip()}")
    return r.stdout.strip()


if git("status", "--porcelain", "--untracked-files=no"):
    sys.exit("Tracked files have uncommitted changes. Commit or stash them first.")
if git("tag", "-l", f"v{v}"):
    sys.exit(f"Tag v{v} already exists.")

cl = Path("CHANGELOG.md")
text = cl.read_bytes().decode("utf-8")
nl = "\r\n" if "\r\n" in text else "\n"
text = text.replace("\r\n", "\n")
m = re.search(r"^## \[Unreleased\]\n(.*?)(?=^## \[|\Z)", text, re.M | re.S)
if not m or not m.group(1).strip():
    sys.exit("CHANGELOG.md has nothing under [Unreleased].")
today = datetime.date.today().isoformat()
text = text[:m.start()] + f"## [Unreleased]\n\n## [{v}] - {today}\n{m.group(1).strip()}\n\n" + text[m.end():]
cl.write_bytes(text.replace("\n", nl).encode("utf-8"))

pj = Path("package.json")
raw = pj.read_bytes().decode("utf-8")
new, n = re.subn(r'("version"\s*:\s*")[^"]*(")', rf"\g<1>{v}\g<2>", raw, count=1)
if not n:
    sys.exit('package.json has no "version" field.')
pj.write_bytes(new.encode("utf-8"))
json.loads(new)  # still valid JSON

# Top-level folders hidden by the whitelist .gitignore, so pack content isn't silently left out.
subprocess.run([sys.executable, str(Path(__file__).with_name("doctor.py"))])

git("add", "package.json", "CHANGELOG.md")
git("commit", "-m", f"Release {v}")
git("tag", "-a", f"v{v}", "-m", f"Release version {v}")
print(f"Committed and tagged v{v}.")
if push:
    git("push", "origin", "HEAD")
    git("push", "origin", f"v{v}")
    print("Pushed. The release workflow is running (Actions tab).")
else:
    print(f"Check with: git show v{v}. Then: git push origin HEAD && git push origin v{v}")
