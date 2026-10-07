# Working on the pack together

How this repo works, how to get it onto your machine, and how to stay in sync while developing.

## How it works

There are two separate things, and they travel by different routes:

| What | Where it lives | How it reaches you |
|------|----------------|--------------------|
| **Configs, quests, KubeJS scripts, docs** | This Git repo | `git pull` |
| **Mod jars** (the `.jar` files in `mods/`) | CurseForge | The CurseForge app installs and updates them |

**Mod jars are not in the repo.** `git pull` never adds, removes or updates a mod. If a change needs a new mod, the person who made it must say so (in the commit message, the CHANGELOG, or a message), and everyone installs it themselves.

The repo is laid out like a Minecraft *instance folder* (the folder holding `mods`, `config`, `saves`). So the repo root and the instance folder are the same place.

## One-time setup

You need the pack installed first, so you have the right mods.

1. Install the pack from CurseForge (or ask for the mod list if it isn't published yet).
2. Install [Git](https://git-scm.com) if you don't have it.
3. Close Minecraft.
4. In the CurseForge app, click the three dots (⋯) on the pack, then **Open Folder**.
5. **Back up first:** copy the `config` folder somewhere safe. The next step overwrites it.
6. Click the address bar of that folder window, type `cmd`, press Enter. A terminal opens in the folder.
7. Run these one at a time:

```bash
git init
git remote add origin https://github.com/Jankeys02/jankeys-tensura-reincarnated.git
git fetch origin
git checkout -f -B main origin/main
```

`checkout -f` replaces files that share a name with repo files (like `config/`). Your mods, saves and screenshots are untouched, because the repo doesn't contain them.

## Staying up to date

Before you start working each session:

```bash
git pull origin main
```

If Git refuses because you changed a file yourself, either commit your change (see below) or run `git stash` to set it aside, pull, then `git stash pop` to bring it back.

## Developing: the daily loop

1. **Pull** the latest (above).
2. **Make a branch** for your work, so `main` stays stable:
   ```bash
   git checkout -b my-change-name
   ```
3. **Edit and test in-game.** Launch the pack and check your change works.
4. **See what you changed:**
   ```bash
   git status
   ```
5. **Commit** (save a snapshot) only the files you meant to change:
   ```bash
   git add config/ftbquests kubejs
   git commit -m "Short description of what and why"
   ```
6. **Push** your branch to GitHub:
   ```bash
   git push -u origin my-change-name
   ```
7. **Open a Pull Request** on GitHub (the "Compare & pull request" button). The owner reviews it and merges it into `main`.

Outside collaborators can't push to this repo directly. They **fork** it (GitHub's Fork button), push to their fork, and open the Pull Request from there. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Syncing mods while developing

Git can't carry mod jars, so the repo tracks a **mod list** instead: [MODS.md](MODS.md) (name, exact file, CurseForge download link for each mod). Because it's a text file, Git shows exactly which mods were added, removed or updated in every commit.

**If you add, remove or update a mod** (anyone with the pack installed):

1. Change the mod in the CurseForge app as normal and test in-game.
2. Regenerate the list (needs [Node.js](https://nodejs.org)); run it in the instance folder:
   ```bash
   node tools/modlist.js
   ```
3. Commit `MODS.md` together with the configs/quests that need the mod, in the same commit and Pull Request. Add a line to `CHANGELOG.md`.

**If you pulled and something is missing or broken** (everyone else):

```bash
git pull origin main
node tools/modlist.js --check
```

It prints **MISSING** (mods to install or update, each with a download link) and **EXTRA** (mods you have that the pack doesn't list). Fix those in the CurseForge app, then launch.

**Rules that keep this working**

- A PR that changes `MODS.md` is not done until the reviewer has also installed those mods.
- Configs for a new mod (`config/<mod>*.toml`) go in the same commit as the `MODS.md` change. Mods write their config on first launch, so launch once before committing.
- `MODS.md` is generated from `minecraftinstance.json` (CurseForge's record of installed mods), so a jar dropped into `mods/` by hand won't appear. Install through the CurseForge app.
- Mods whose authors forbid redistribution are listed with their CurseForge link only; nothing is uploaded.
- At release, the owner publishes the pack on CurseForge and the list in `MODS.md` should match it.

**Later, if the manual step gets annoying:** a GitHub Action that fails a PR when `MODS.md` is out of date, or CurseForge's modpack manifest (`manifest.json`) as the source of truth. Not needed at two or three people.

## Server pack

The server pack is **not stored in this repo**. It is a zip built from the client pack and attached to each CurseForge release as an extra file. Players who just want to host download it from there; see [SERVER_HOSTING.md](SERVER_HOSTING.md). Build notes and boot-test results are in [SERVER_PACK.md](SERVER_PACK.md).

How it relates to the repo:

- **Same configs and quests.** The server uses the same `config/`, `kubejs/` and quests as the client. A change here reaches the server on the next server pack build, nothing extra to do.
- **Fewer mods.** The server leaves out client-only mods (shaders, minimap, JEI and so on). [client-mods-to-exclude.txt](client-mods-to-exclude.txt) is that list, and the `Side` column in [MODS.md](MODS.md) shows it per mod: `client` means left out of the server, `client+server` means it goes on both.
- **Three mods can't be bundled** (their authors forbid redistribution). Hosts download them themselves; see SERVER_HOSTING.md.

**When you add a mod, also decide its side:**

1. If it's client-only (visuals, HUD, sounds, minimap), add its exact jar filename to `client-mods-to-exclude.txt`.
2. Run `node tools/modlist.js` so `MODS.md` shows the right `Side`.
3. If you're not sure, leave it off the exclude list and test: start the server, and NeoForge crashes loudly at boot naming any client-only mod. Add that one to the list and retry.

**To self-host a test server from your own game folder:** don't copy your whole instance. Build the zip with ServerPackCreator as described in SERVER_PACK.md, so the exclude list is applied for you.

**Releasing:** every client release should come with a rebuilt server pack, so versions match. Players on a different version than the server get a mod-mismatch error when joining.

## Where things are

- `config/ftbquests/quests/chapters/*.snbt` — one file per quest chapter
- `config/ftbquests/quests/lang/en_us.snbt` — quest text (titles, descriptions)
- `config/ftbquests/quests/data.snbt` — quest book settings
- `kubejs/` — scripts and resource overrides
- `defaultconfigs/` — defaults applied to new worlds
- `CHANGELOG.md` — what changed per release
- `QUEST_EXPANSION.md`, `SERVER_PACK.md`, `SERVER_HOSTING.md` — design and server notes

## Tips and gotchas

- **Editing quests in-game** (the FTB Quests editor) writes straight to the `.snbt` files. Those edits show up in `git status`; commit them like any other change.
- **Two people editing the same quest chapter** will cause a *merge conflict* (Git can't combine both edits). Keep one person per chapter at a time, and pull before you start.
- **Don't commit** worlds (`saves/`), `logs/`, `crash-reports/`, screenshots, or anything with your username or account tokens. These are meant to stay local; if `git status` lists them, leave them out of `git add`.
- **Config files rewrite themselves.** Mods often rewrite their own config when the game starts, so `git status` can show changes you didn't make (for example `DistantHorizons.toml`). Only commit the ones you changed on purpose.
- **Adding or removing a mod?** Say so clearly in your commit/PR and in `CHANGELOG.md`, since Git can't carry the jar. The release maintainer updates the CurseForge pack.

## Releasing (owner)

Versions follow [SemVer](https://semver.org/): `MAJOR.MINOR.PATCH`.

1. Bump `version` in `package.json`.
2. Move the `[Unreleased]` items in `CHANGELOG.md` into a dated version section.
3. Commit, then tag and push:
   ```bash
   git tag v1.2.0
   git push origin main --tags
   ```
4. Upload the new pack version to CurseForge. See [RELEASE_GUIDE.md](RELEASE_GUIDE.md).
