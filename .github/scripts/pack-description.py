"""Attach PACK_DESCRIPTION.md to the release when it changed since the previous release tag.
Usage: pack-description.py <tag>   (needs notes.md from release-notes.py; run after it)
Writes pack-description.md and appends a "Pack description" section with the changed lines to notes.md.
Does nothing when the description is unchanged."""
import subprocess, sys
from pathlib import Path

tag = sys.argv[1]
FILE = "PACK_DESCRIPTION.md"


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


prev = git("describe", "--tags", "--abbrev=0", "--match", "v*", f"{tag}^").stdout.strip()
if prev and git("diff", "--quiet", prev, tag, "--", FILE).returncode == 0:
    print("pack description unchanged since", prev)
    sys.exit(0)

Path("pack-description.md").write_text(Path(FILE).read_text(encoding="utf-8"), encoding="utf-8")
if prev:
    diff = git("diff", "--no-color", "-U0", prev, tag, "--", FILE).stdout.replace("\r\n", "\n").splitlines()
    changed = "\n".join(l for l in diff if l[:1] in "+-" and not l.startswith(("+++", "---")))
else:
    changed = "(first release: the whole file is new)"
section = (
    "\n## Pack description\n\n"
    "The CurseForge pack description changed in this release. Paste `pack-description.md` (under Assets) "
    "into the CurseForge page. What changed:\n\n"
    f"```diff\n{changed}\n```\n"
)
with open("notes.md", "a", encoding="utf-8") as f:
    f.write(section)
print("pack description changed since", prev or "(no earlier tag)")
