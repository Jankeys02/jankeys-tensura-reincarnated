# Hosting your own server

Short notes for people running the server pack. Developers: the server is built from the `packwiz/` mod list, see `DEVELOPMENT.md`. `SERVER_PACK.md` is the older build history.

## Requirements
- Java 21 (NeoForge 21.1.249 / Minecraft 1.21.1).
- 8 GB RAM for the server is a good start (`-Xms4G -Xmx8G` in `user_jvm_args.txt`); more for many players.
- Open **TCP 25565** (game) and **UDP 24454** (Simple Voice Chat) on your router/firewall.
- You must accept the Minecraft EULA yourself (`eula.txt`).

## Setup
Download the server file of the version you want from the CurseForge page (the file marked "Server Pack", under the pack's additional files) or from the [GitHub release](https://github.com/Jankeys02/jankeys-tensura-reincarnated/releases) under **Assets** (`jankeys-tensura-reincarnated-vX.Y.Z-server.zip`). It holds the mods, configs, scripts, the NeoForge installer and start scripts. The `-server-installer.zip` next to it is a small alternative that downloads the mods when you run it.

1. Unzip it into an empty folder.
2. Open `MISSING-MODS.txt`. It lists the few mods that can't be bundled because their authors block downloads outside CurseForge. Download each from its link and put the jars in `mods/`. (Hosts that install CurseForge dependencies may do this for you.)
3. Run `start.bat` (Windows) or `sh start.sh` (Linux). The first run installs the NeoForge server, then stops because the EULA isn't accepted yet.
4. Open `eula.txt`, set `eula=true`, and run the start script again.

## Mods you must add yourself
`MISSING-MODS.txt` in the zip is the list. Clients that have these mods can't join a server that lacks them, so use the same versions as the pack.

## First start
- The first start is slow: Tensura builds its labyrinth dimension and EMC map, and loading the mods takes about a minute. Expect a "Can't keep up" warning once.
- Terralith generates terrain slowly. Pregenerate around spawn once with Chunky (included), from the server console or in game as an op:
  `/chunky radius 2000` then `/chunky start`. `/chunky pause` and `/chunky continue` control it.
- Biomes only change in newly generated chunks. Do not swap in this pack over an old world and expect new biomes in explored areas.

## Updating
1. **Back up your world.**
2. Download the new server zip and unzip it over your server folder (keep your world, `eula.txt` and any changes of your own to configs).
3. Delete mods from `mods/` that are no longer in the new zip's `mods/` folder, and check `MISSING-MODS.txt` again.
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
