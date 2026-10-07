# Jankeys' Tensura Reincarnated

NeoForge 1.21.1 modpack built around *That Time I Got Reincarnated as a Slime* (Tensura) with a 31-chapter FTB Quests book (830 quests).

> Download and install through the CurseForge app: [Jankeys' Tensura Reincarnated](https://www.curseforge.com/minecraft/modpacks/jankeys-tensura-reincarnated). This repo holds the pack's configs, KubeJS scripts, quests, changelog and the mod list (`packwiz/`); mod jars are not stored here.

**What's inside**
- **Tensura core + addons:** Ice and Fire, Nightmare, FTB Quests, Better Subordinates, Guild, Enigmatic, Unique Monsters, Ascension, TensuraMoreSkills, Elite Tensura Addon and Origins.
- **A 31-chapter quest book (830 quests)**, with a short tutorial ("Field note") in every quest. Chapters are grouped: a Field Guide to the controls, Tensura, the four extra dimensions, boss hunts, homestead life, ranked Paths, and a chapter for each Tensura addon.
- **Ranked Paths:** quests grant ranks as you progress. The Miner's Path grows Ultimine from 8 to 64 blocks (with hunger cost and cooldown). The Explorer's, Homesteader's and Hunter's Paths add claimed chunks, homes and bonus health, and each rank grants a Tensura skill.
- **Dimension gate:** in survival, three dimensions (Eternal Starlight, Chrono Dawn, The Afterdark) are locked until you have visited the Nether or summoned a Wither. Creative, spectator and operators are exempt.
- **World:** Terralith biomes plus four extra dimensions (The Twilight Forest, Eternal Starlight, Chrono Dawn, The Afterdark).
- **Structures and loot:** the YUNG's suite, Dungeons Arise, Artifacts, Backpacked, Sophisticated Storage.
- **Bosses:** L_Ender's Cataclysm, Mowzie's Mobs, plus custom Tensura boss structures (some boss structures are rare and may be far from spawn).
- **Homestead:** Farmer's Delight, Comforts, Supplementaries, Waystones.
- **Performance:** Sodium, Iris, ModernFix, FerriteCore, Entity Culling, Distant Horizons.
- **Visuals (optional):** Fresh Animations, 3D trims, Complementary shaders.

**Requirements**
- Minecraft 1.21.1, NeoForge 21.1.249
- 6-8 GB RAM allocated (8 GB recommended with shaders / Distant Horizons)

**Credits** — see the mod list; all mods belong to their authors.

**Server pack**
The server pack (`jankeys-tensura-vX-server.zip`) is attached to each [GitHub release](https://github.com/Jankeys02/jankeys-tensura-reincarnated/releases) under **Assets**. It holds the configs, quests and KubeJS scripts plus an installer that downloads the server's mods (client-only mods are skipped; Chunky is included). Unzip it, install NeoForge 21.1.249, run `install-mods.bat` (or `sh install-mods.sh`), and follow the `README.txt` inside. Accept the Minecraft EULA yourself, give it 4-8 GB RAM, and open UDP 24454 for proximity voice chat; see `SERVER_HOSTING.md` for permissions (FTB Ranks). Six mods can't be downloaded automatically because their authors block it (Custom Chest Menus, Easy NPC, FiltPick, Tensura: Better Subordinates, Tensura: Enigmatic, Tensura: Unique Monsters): the installer prints a link for each, and you save the file into `mods/`. Boot-tested 2026-10-07: 130 mods, starts in under a minute. Back up your world before updating, since worldgen mods only change newly generated chunks.

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
