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

Pushing the tag starts [`.github/workflows/release.yml`](.github/workflows/release.yml). It takes a few minutes and builds:

- `jankeys-tensura-v0.3.0-curseforge.zip`: the client pack (a mod list plus the configs, `defaultconfigs` and `kubejs` as overrides).
- `jankeys-tensura-v0.3.0-server.zip`: the server pack (configs plus an installer that downloads the server's mods).
- `changelog-client.md` and `changelog-server.md`, also shown in the release description.

Check the **Actions** tab on GitHub; when it's green, the files are on the **Releases** page under **Assets**. If the build fails, fix the cause and release the next patch version. Don't reuse the tag.

## Publish on CurseForge (manual)

1. From the release page, download the `-curseforge.zip` and `-server.zip`.
2. In the CurseForge author console, upload the client zip as a new file of the modpack, and paste the client changelog into its changelog box.
3. Upload the server zip as the server pack file for that version, paste the server changelog, and list the six manual-download mods as Required Dependencies (see [SERVER_HOSTING.md](SERVER_HOSTING.md)).
4. If the pack description changed, update it from [PACK_DESCRIPTION.md](PACK_DESCRIPTION.md).
