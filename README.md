# Jankeys' Tensura Reincarnated

NeoForge 1.21.1 modpack built around *That Time I Got Reincarnated as a Slime* (Tensura) with 14 FTB Quests chapters.

> Download and install through the CurseForge app: [Jankeys' Tensura Reincarnated](https://www.curseforge.com/minecraft/modpacks/jankeys-tensura-reincarnated). This repo holds the pack's configs, KubeJS scripts, quests, changelog and the mod list (`packwiz/`); mod jars are not stored here.

**What's inside**
- Tensura core + addons (Ice and Fire, Nightmare, FTB quests, better subordinates, Guild, Enigmatic, Unique Monsters)
- 14 FTB Quests chapters guiding you from Getting Started to Myths and Treasure
- Leveling system: quests grant ranks as you progress. Ultimine starts small (8 blocks) and grows to 64 with the Miner's Path, with hunger cost and cooldown; more rank paths to come
- Better structures (YUNG's suite), Dungeons Arise, Artifacts, Backpacked, Sophisticated Storage
- Performance: Sodium, Iris, ModernFix, FerriteCore, Entity Culling, Distant Horizons
- World: Terralith biomes plus four extra dimensions (The Twilight Forest, Eternal Starlight, Chrono Dawn, The Afterdark)
- Bosses and structures: L_Ender's Cataclysm, Mowzie's Mobs, plus custom Tensura boss structures
- Polished visuals: Fresh Animations, 3D trims, Complementary shaders (optional)

**Requirements**
- Minecraft 1.21.1, NeoForge 21.1.249
- 6-8 GB RAM allocated (8 GB recommended with shaders / Distant Horizons)

**Credits** — see the mod list; all mods belong to their authors.

**Server pack**
The server pack (`jankeys-tensura-vX-server.zip`) is attached to each [GitHub release](https://github.com/Jankeys02/jankeys-tensura-reincarnated/releases) under **Assets**. It holds the configs, quests and KubeJS scripts plus an installer that downloads the server's mods (client-only mods are skipped; Chunky is included). Unzip it, install NeoForge 21.1.249, run `install-mods.bat` (or `sh install-mods.sh`), and follow the `README.txt` inside. Accept the Minecraft EULA yourself, give it 4-8 GB RAM, and open UDP 24454 for proximity voice chat; see `SERVER_HOSTING.md` for permissions (FTB Ranks). Six mods can't be downloaded automatically because their authors block it (Custom Chest Menus, Easy NPC, FiltPick, Tensura: Better Subordinates, Tensura: Enigmatic, Tensura: Unique Monsters): the installer prints a link for each, and you save the file into `mods/`. The server hasn't been boot-tested with the current mod list yet. Back up your world before updating, since worldgen mods only change newly generated chunks.

**Contributing**
Clone the repo and read [DEVELOPMENT.md](DEVELOPMENT.md). Mods are tracked in `packwiz/` (one small file per mod); add or change a mod with `packwiz curseforge add <link>`, then open a Pull Request. Releases are built by GitHub when a `v*` tag is pushed.

## Repo layout
- `config/`, `defaultconfigs/` — mod configs and FTB Quests
- `kubejs/` — scripts and resource overrides (incl. `musicnotification/musics.json` fix)
- `packwiz/` — the mod list (one file per mod, with its client/server side); source for the release zips
- `server/` — files that go into the server zip
- `DEVELOPMENT.md` — how to work on the pack together
- `SERVER_PACK.md`, `SERVER_HOSTING.md` — server pack history and hosting guide
- `CHANGELOG.md` — SemVer; `package.json` `version` is the source of truth

## License
See [LICENSE](LICENSE). Mods belong to their authors.
