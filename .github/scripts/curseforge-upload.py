"""Upload the client and server zips to CurseForge. Run only by the manual "Publish to CurseForge" workflow
(never on a tag push). Needs the CURSEFORGE_TOKEN secret and CURSEFORGE_PROJECT_ID variable.
Usage: curseforge-upload.py <tag> <client.zip> <server.zip>   (reads changelog-client.md / changelog-server.md)
Env: CLIENT_FILE_ID (optional, skips the client upload), CURSEFORGE_TOKEN (API token from curseforge.com/account/api-tokens), CURSEFORGE_PROJECT_ID.
The token is only sent as a header and never printed."""
import json, os, sys, tomllib, urllib.error, urllib.request, uuid
from pathlib import Path

tag, client, server = sys.argv[1:4]
token, project = os.environ["CURSEFORGE_TOKEN"], os.environ["CURSEFORGE_PROJECT_ID"]
API = "https://minecraft.curseforge.com/api"
versions_toml = tomllib.loads(Path(os.environ.get("PACK_TOML", "packwiz/pack.toml")).read_text(encoding="utf-8"))["versions"]
mc = versions_toml["minecraft"]
pack_name = tomllib.loads(Path(os.environ.get("PACK_TOML", "packwiz/pack.toml")).read_text(encoding="utf-8"))["name"]
title = f"{pack_name} {tag.removeprefix('v')}"  # e.g. "My Pack 1.2.0"; the server file adds " Server Pack"



def call(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers={"X-Api-Token": token, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:  # show CurseForge's reason (the response body holds no secrets)
        sys.exit(f"CurseForge answered HTTP {e.code} for {url.split('/api/')[1]}: {e.read().decode('utf-8', 'replace')[:500]}")


def required_deps():
    """Project ids from .github/curseforge-required-deps.txt, as CurseForge relations (slug = packwiz file name)."""
    f = Path(".github/curseforge-required-deps.txt")
    ids = [l.split("#")[0].strip() for l in f.read_text(encoding="utf-8").splitlines()] if f.exists() else []
    out = []
    for pid in filter(None, ids):
        hit = next((p for p in Path("packwiz").rglob("*.pw.toml")
                    if str(tomllib.loads(p.read_text(encoding="utf-8")).get("update", {}).get("curseforge", {}).get("project-id")) == pid), None)
        if not hit:
            sys.exit(f"Project id {pid} in curseforge-required-deps.txt is not in packwiz/")
        out.append({"slug": hit.name.removesuffix(".pw.toml"), "projectID": pid, "type": "requiredDependency"})
    return out


def required_deps():
    """Project ids from .github/curseforge-required-deps.txt, as CurseForge relations (slug = packwiz file name)."""
    f = Path(".github/curseforge-required-deps.txt")
    ids = [l.split("#")[0].strip() for l in f.read_text(encoding="utf-8").splitlines()] if f.exists() else []
    out = []
    for pid in filter(None, ids):
        hit = next((p for p in Path("packwiz").rglob("*.pw.toml")
                    if str(tomllib.loads(p.read_text(encoding="utf-8")).get("update", {}).get("curseforge", {}).get("project-id")) == pid), None)
        if not hit:
            sys.exit(f"Project id {pid} in curseforge-required-deps.txt is not in packwiz/")
        out.append({"slug": hit.name.removesuffix(".pw.toml"), "projectID": pid, "type": "requiredDependency"})
    return out


def upload(path, changelog, name, release_type, parent=None):
    meta = {"changelog": changelog, "changelogType": "markdown", "displayName": name, "releaseType": release_type}
    if parent:  # an additional file inherits the parent's game versions; CurseForge rejects them here
        meta["parentFileID"] = parent
        if required_deps():  # the server file lists the mods that can only be downloaded from CurseForge
            meta["relations"] = {"projects": required_deps()}
        if required_deps():  # the server file lists the mods that can only be downloaded from CurseForge
            meta["relations"] = {"projects": required_deps()}
    else:
        meta["gameVersions"] = game_versions
    b = uuid.uuid4().hex
    body = b"".join([
        f'--{b}\r\nContent-Disposition: form-data; name="metadata"\r\n\r\n{json.dumps(meta)}\r\n'.encode(),
        f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{Path(path).name}"\r\n'
        f'Content-Type: application/zip\r\n\r\n'.encode(), Path(path).read_bytes(), f"\r\n--{b}--\r\n".encode()])
    return call(f"{API}/projects/{project}/upload-file", body, {"Content-Type": f"multipart/form-data; boundary={b}"})["id"]


versions = call(f"{API}/game/versions")
game_versions = []
for want in (mc, "NeoForge"):  # the Minecraft version and the mod loader, as on CurseForge's file page
    ids = [v["id"] for v in versions if v["name"] == want]
    if not ids:
        sys.exit(f"CurseForge has no game version named {want}")
    game_versions.append(ids[0])
# RELEASE_TYPE (alpha|beta|release) overrides; "auto" = from the tag: -alpha -> alpha, other suffix -> beta, none -> release
rtype = os.environ.get("RELEASE_TYPE", "auto")
if rtype == "auto":
    rtype = "alpha" if "-alpha" in tag else "beta" if "-" in tag else "release"
main_id = os.environ.get("CLIENT_FILE_ID")  # set to attach the server zip to a client file that is already uploaded
if main_id:
    main_id = int(main_id)
else:
    main_id = upload(client, Path("changelog-client.md").read_text(encoding="utf-8"), title, rtype)
    print("client file id", main_id)
print("server file id", upload(server, Path("changelog-server.md").read_text(encoding="utf-8"), f"{title} Server Pack", rtype, main_id))
