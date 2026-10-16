"""Upload the client and server zips to CurseForge. Run only by the manual "Publish to CurseForge" workflow
(never on a tag push). Needs the CURSEFORGE_TOKEN secret and CURSEFORGE_PROJECT_ID variable.
Usage: curseforge-upload.py <tag> <client.zip> <server.zip>   (reads changelog-client.md / changelog-server.md)
Env: CURSEFORGE_TOKEN (API token from curseforge.com/account/api-tokens), CURSEFORGE_PROJECT_ID.
The token is only sent as a header and never printed."""
import json, os, sys, tomllib, urllib.request, uuid
from pathlib import Path

tag, client, server = sys.argv[1:4]
token, project = os.environ["CURSEFORGE_TOKEN"], os.environ["CURSEFORGE_PROJECT_ID"]
API = "https://minecraft.curseforge.com/api"
mc = tomllib.loads(Path("packwiz/pack.toml").read_text(encoding="utf-8"))["versions"]["minecraft"]


def call(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers={"X-Api-Token": token, **(headers or {})})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)


def upload(path, changelog, name, release_type, parent=None):
    meta = {"changelog": changelog, "changelogType": "markdown", "displayName": name,
            "gameVersions": [game_version], "releaseType": release_type}
    if parent:
        meta["parentFileID"] = parent
    b = uuid.uuid4().hex
    body = b"".join([
        f'--{b}\r\nContent-Disposition: form-data; name="metadata"\r\n\r\n{json.dumps(meta)}\r\n'.encode(),
        f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{Path(path).name}"\r\n'
        f'Content-Type: application/zip\r\n\r\n'.encode(), Path(path).read_bytes(), f"\r\n--{b}--\r\n".encode()])
    return call(f"{API}/projects/{project}/upload-file", body, {"Content-Type": f"multipart/form-data; boundary={b}"})["id"]


versions = call(f"{API}/game/versions")
ids = [v["id"] for v in versions if v["name"] == mc]
if not ids:
    sys.exit(f"CurseForge has no game version named {mc}")
game_version = ids[0]
# v1.0.0-alpha.1 -> alpha, any other suffix (-beta.1, -rc.1) -> beta, no suffix -> release
rtype = "alpha" if "-alpha" in tag else "beta" if "-" in tag else "release"
main_id = upload(client, Path("changelog-client.md").read_text(encoding="utf-8"), tag, rtype)
print("client file id", main_id)
print("server file id", upload(server, Path("changelog-server.md").read_text(encoding="utf-8"), f"{tag} server", rtype, main_id))
