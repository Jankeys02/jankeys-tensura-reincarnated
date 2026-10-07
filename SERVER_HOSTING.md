# Hosting your own server

Short notes for people running the server pack. Developers: the server is built from the `packwiz/` mod list, see `DEVELOPMENT.md`. `SERVER_PACK.md` is the older build history.

## Requirements
- Java 21 (NeoForge 21.1.249 / Minecraft 1.21.1).
- 8 GB RAM for the server is a good start (`-Xms4G -Xmx8G` in `user_jvm_args.txt`); more for many players.
- Open **TCP 25565** (game) and **UDP 24454** (Simple Voice Chat) on your router/firewall.
- You must accept the Minecraft EULA yourself (`eula.txt`).

## Setup
The server pack (`jankeys-tensura-vX.Y.Z-server.zip`) is on each [GitHub release](https://github.com/Jankeys02/jankeys-tensura-reincarnated/releases) under **Assets**. It holds the configs, quests and scripts plus an installer that downloads the mods. It contains no mod jars.

1. Unzip it into an empty folder.
2. Install the NeoForge 21.1.249 server into that folder: get the installer from [neoforged.net](https://neoforged.net), run it and choose **Install server**. This creates `run.bat` / `run.sh`.
3. Run `install-mods.bat` (Windows) or `sh install-mods.sh` (Linux). It downloads the server's mods (about 130) into `mods/`. It stops and prints a link for each mod it can't download (next section).
4. Download those files from the printed links, put them in `mods/`, and run the installer again until it says it finished.
5. Start the server once (`run.bat` / `run.sh`) so it creates `eula.txt`, set `eula=true`, and start it again.

## Mods you must add yourself
Six mods can't be downloaded automatically, because their authors block downloads from outside CurseForge. The installer prints a link for each. Download the same versions as the pack and put the jars in `mods/`. Clients that have these mods can't join a server that lacks them.

- **Tensura: Better Subordinates**: https://www.curseforge.com/projects/1489224
- **Tensura: Enigmatic**: https://www.curseforge.com/projects/1299711
- **Tensura: Unique Monsters**: https://www.curseforge.com/projects/1489273
- **Easy NPC**: https://www.curseforge.com/projects/1308987
- **Custom Chest Menus**: https://www.curseforge.com/projects/1343005
- **FiltPick**: https://www.curseforge.com/projects/700141

Every other mod (including Tensura: Ascension, TensuraMoreSkills, Elite Tensura Addon and Tensura: Origins) is downloaded for you.

## First start
- The first start is slow: Tensura builds its labyrinth dimension and EMC map, and loading the mods takes about a minute. Expect a "Can't keep up" warning once.
- Terralith generates terrain slowly. Pregenerate around spawn once with Chunky (included), from the server console or in game as an op:
  `/chunky radius 2000` then `/chunky start`. `/chunky pause` and `/chunky continue` control it.
- Biomes only change in newly generated chunks. Do not swap in this pack over an old world and expect new biomes in explored areas.

## Updating
1. **Back up your world.**
2. Download the new server zip and copy its `config`, `defaultconfigs` and `kubejs` folders over yours (keep your own changes, such as ranks, if you made any).
3. Run the installer script again. It adds, updates and removes mods to match the release.
4. Players need the matching client pack version, or they get a mod-mismatch error when joining.

## Permissions (FTB Ranks)
The pack ships FTB Ranks. Out of the box it behaves like vanilla: everyone is a `member`, ops are `admin`, and no commands are restricted beyond vanilla op levels.

- Rank file: `world/serverconfig/ftbranks/ranks.snbt` (created on first start). Run `/ftbranks reload` after editing.
- A rank grants or denies a command with `command.<name>: true|false`, for example inside `member`:
  `command.home: true` and `command.chunky: false`. `README.txt` in the same folder lists every available node.
- Note: the default ranks add no restrictions and were not tested with a non-op player. Test your own rules before relying on them.
- Give someone a rank: `/ftbranks add <player> <rank>`. List a player's ranks: `/ftbranks list_ranks_of <player>`.

## Mods you can remove
This is a full modpack server. Removing mods from `mods/` will break worlds and quests; only remove ones you know are optional, such as `Chunky` or `ftb-ranks` (the pack works without them). The installer re-adds a removed mod on its next run.
