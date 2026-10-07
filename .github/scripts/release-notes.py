"""Split one CHANGELOG.md version into client and server notes.
Usage: release-notes.py <version>   (writes changelog-client.md, changelog-server.md, notes.md)
A version's section is everything under '## [X.Y.Z]'; its '### Server pack' part is the server
changelog, everything before it is the client changelog."""
import re, sys
from pathlib import Path

v = sys.argv[1].lstrip("v")
text = Path("CHANGELOG.md").read_text(encoding="utf-8").replace("\r\n", "\n")
m = re.search(rf"^## \[{re.escape(v)}\][^\n]*\n(.*?)(?=^## \[|\Z)", text, re.M | re.S)
body = m.group(1).strip() if m else ""
client, _, server = body.partition("### Server pack")
client = client.strip() or "See CHANGELOG.md for what changed."
server = server.strip() or "No server pack changes."
Path("changelog-client.md").write_text(client + "\n", encoding="utf-8")
Path("changelog-server.md").write_text(server + "\n", encoding="utf-8")
Path("notes.md").write_text(f"## Client changelog\n\n{client}\n\n## Server pack changelog\n\n{server}\n", encoding="utf-8")
print(f"{v}: client {len(client)} chars, server {len(server)} chars")
