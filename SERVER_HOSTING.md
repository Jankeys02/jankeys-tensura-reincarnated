# Hosting your own server

Short notes for people running the server pack. For the build/test notes, see `SERVER_PACK.md`.

## Requirements
- Java 21 (NeoForge 21.1.249 / Minecraft 1.21.1). The start scripts can install it for you (`install_java.*`).
- 8 GB RAM for the server is a good start (`-Xms4G -Xmx8G` in `user_jvm_args.txt`); more for many players.
- Open **TCP 25565** (game) and **UDP 24454** (Simple Voice Chat) on your router/firewall.
- You must accept the Minecraft EULA yourself (`eula.txt`).

## First start
- The first start is slow: Tensura builds its labyrinth dimension and EMC map. Later starts take about 15 seconds.
- Terralith generates terrain slowly. Pregenerate around spawn once with Chunky (included), from the server console or in game as an op:
  `/chunky radius 2000` then `/chunky start`. `/chunky pause` and `/chunky continue` control it.
- Biomes only change in newly generated chunks. Do not swap in this pack over an old world and expect new biomes in explored areas.

## Permissions (FTB Ranks)
The pack ships FTB Ranks. Out of the box it behaves like vanilla: everyone is a `member`, ops are `admin`, and no commands are restricted beyond vanilla op levels.

- Rank file: `world/serverconfig/ftbranks/ranks.snbt` (created on first start). Run `/ftbranks reload` after editing.
- A rank grants or denies a command with `command.<name>: true|false`, for example inside `member`:
  `command.home: true` and `command.chunky: false`. `README.txt` in the same folder lists every available node.
- Note: the default ranks add no restrictions and were not tested with a non-op player. Test your own rules before relying on them.
- Give someone a rank: `/ftbranks add <player> <rank>`. List a player's ranks: `/ftbranks list_ranks_of <player>`.

## Mods you must add yourself
Three mods are not bundled because their authors do not allow redistribution. Download the same versions as the client pack from their CurseForge pages and put the jars in `mods/`. Clients that have these mods cannot join a server that lacks them.

- **Tensura: Better Subordinates**: https://www.curseforge.com/projects/1489224
- **Tensura: Enigmatic**: https://www.curseforge.com/projects/1299711
- **Tensura: Unique Monsters**: https://www.curseforge.com/projects/1489273

## Bundled mods with open licenses
These mods have CurseForge third-party distribution switched off, but their licenses allow redistribution, so they are bundled. All credit to their authors:

- Easy NPC (MIT): https://www.curseforge.com/projects/1308987
- Custom Chest Menus (GPLv3): https://www.curseforge.com/projects/1343005
- FiltPick (LGPL): https://www.curseforge.com/projects/700141

## Mods you can remove
This is a full modpack server. Removing mods from `mods/` will break worlds and quests; only remove ones you know are optional, such as `Chunky` or `ftb-ranks` (the pack works without them).
