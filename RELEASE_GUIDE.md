# How to Create a Release

Only repo admins can do this: the `v*` tags are protected by a GitHub ruleset, so nobody else can create them.

## Versioning

This project follows [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **MAJOR**: changes that break existing worlds or saves.
- **MINOR**: new content or features that keep worlds working (new quests, new mods).
- **PATCH**: fixes only, and release tooling changes.

The version in `package.json` is the source of truth. Release tags are that version prefixed with `v` (for example `v0.3.0`), and pushing one is what starts the release build. A tag with a suffix (`v0.3.0-rc.1`) is published as a pre-release.

## Before you start

1. Everything for the release is merged into `main`, and your working tree is clean (`git status`).
2. Mod changes are recorded in `packwiz/` (see [DEVELOPMENT.md](DEVELOPMENT.md)); run `packwiz refresh` in that folder if you edited any mod file by hand.
3. You have launched the pack once with the final mod list and quests, and (if mods changed) booted the server.

## Steps

### 1. Update the version

In `package.json`:

```json
{
  "version": "0.3.0"
}
```

### 2. Write the changelog

In [CHANGELOG.md](CHANGELOG.md), turn the `[Unreleased]` items into a dated section, `## [0.3.0] - YYYY-MM-DD`. Write it for players.

- Everything in the section is the **client changelog**.
- Put server-specific notes under a `### Server pack` heading at the end of the same section; that part becomes the **server changelog**.
- The heading must match the version exactly (`## [0.3.0]` for tag `v0.3.0`), or the release notes fall back to "See CHANGELOG.md".

### 3. Commit and tag

```bash
git add package.json CHANGELOG.md
git commit -m "Update version to 0.3.0"
git push origin main
git tag -a v0.3.0 -m "Release version 0.3.0"
git push origin v0.3.0
```

`main` requires a Pull Request for everyone except admins. Tags can't be changed or deleted afterwards, so double-check the version before you push the tag.

## What happens next

Pushing the tag starts [`.github/workflows/release.yml`](.github/workflows/release.yml). It takes several minutes and builds:

- `jankeys-tensura-v0.3.0-curseforge.zip`: the client pack (a mod list plus the configs, `defaultconfigs` and `kubejs` as overrides).
- `jankeys-tensura-v0.3.0-server.zip`: the **finished server pack**: the mods, configs, scripts, the NeoForge installer, `start.bat` / `start.sh` and a readme in one zip (a few hundred MB). Mods whose authors block downloads outside CurseForge can't be bundled; they are listed in `MISSING-MODS.txt` inside the zip, and `start.bat` / `start.sh` warn about them at every start. Which mods those are is decided by `.github/curseforge-required-deps.txt` (see "Blocked mods" in [DEVELOPMENT.md](DEVELOPMENT.md)).
- `jankeys-tensura-v0.3.0-server-installer.zip`: a small alternative server pack that downloads the mods when you run it.
- `jankeys-tensura-v0.3.0-prism-dev.zip`: the developer instance for Prism (not for players).
- `changelog-client.md`, `changelog-server.md` and, when it changed, `pack-description.md`.

Check the **Actions** tab on GitHub; when it's green, the files are on the **Releases** page under **Assets**. If the build fails, fix the cause and release the next patch version. Don't reuse the tag. To try the server zip without releasing, run **Actions > Server zip (test build) > Run workflow**; it keeps the zip as a downloadable artifact for 3 days. Type `yes` in the **accept_eula** box to also run a smoke test: the zip is unzipped on the runner, started once (you accept the Minecraft EULA by typing yes) and stopped as soon as the server prints "Done"; the console log is kept as an artifact. The mods that can't be bundled are missing in that test, so a pass means the server boots without them.

## Publish on CurseForge

Uploading is a separate, deliberate step. A tag push never publishes anything.

**With one click (optional):**
1. One-time setup: create an API token at curseforge.com/account/api-tokens (from the account that may upload to the project). In the GitHub repo go to Settings, Secrets and variables, Actions, and add a secret `CURSEFORGE_TOKEN` and a variable `CURSEFORGE_PROJECT_ID` (the project number in the author console). Never paste the token anywhere else.
2. After the release workflow is green: Actions > **Publish to CurseForge** > Run workflow. Enter the tag in both boxes (the second box is the confirmation), pick the **release type** (`auto` = `-alpha` in the tag gives alpha, any other suffix such as `-beta.1` or `-rc.1` gives beta, no suffix gives release) and leave `client_file_id` empty. It works for older tags too.
3. It uploads the client zip, then the server zip as an additional file attached to it. File names are `<pack name> <version>` and `<pack name> <version> Server Pack`; the changelogs come from `changelog-client.md` and `changelog-server.md`; game versions are Minecraft plus NeoForge. Dependencies are not set through the upload: for a modpack, CurseForge fills the server file's Related Projects with the pack's projects as type Include and the type cannot be changed, so there is nothing to set. Mods that can't be bundled are covered by `MISSING-MODS.txt` in the zip.
4. If the client file uploaded but the server file failed, do not run it again from scratch (that uploads a second client file). Wait a few minutes, then run it again with the client file's id in `client_file_id`; it then only adds the server zip to that file. CurseForge only accepts the attach once the client file is processed, and the error "parentFileID ... not editable" means it isn't yet (or the file was deleted). The fallback is **Add Additional File** under the client file in the console.
5. Failed uploads print CurseForge's error message in the log.

**Manual:**

1. From the release page, download the `-curseforge.zip` and `-server.zip`. The `-prism-dev.zip` is for developers (Prism instance with the pre-launch script, see DEVELOPMENT.md) and is not uploaded to CurseForge.
2. In the CurseForge author console, upload the client zip as a new file of the modpack, and paste the client changelog into its changelog box.
3. Upload the server zip as an additional file of that client file, paste the server changelog, and leave Related Projects as CurseForge fills it (type Include, not changeable).
4. **Related Projects (Dependencies)** on the project page (Description tab) is filled in by CurseForge from the uploaded pack: it lists the shader packs and resource packs with the type **Include** (they ship inside the pack). Leave those entries as they are; do not change them to Required. At the time of writing: Photon, Noble, Complementary Reimagined, BSL and Bliss shaders, and the resource packs Refined Torches, Refined Buckets, Fyoncle's 3D Trims, Fresh Moves, Fresh Animations, Fresh Animations: Extensions and Drigo's 3D Lantern x Punchy. There is nothing to set in either place.
5. The project description cannot be changed through the upload. If the release notes have a **Pack description** section, the description changed since the last release: paste `pack-description.md` (under Assets, same text as [PACK_DESCRIPTION.md](PACK_DESCRIPTION.md)) into the CurseForge page. The section lists the changed lines.
