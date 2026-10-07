# Changelog

Versioning: [SemVer](https://semver.org/).

## [Unreleased]
Quest book expansion (planned as 0.2.0). Not yet released or tagged.

### Added
- **12 new quest chapters** (book grows from 14 to 26 chapters, 365 to 620 quests, before the addon chapters below), written as a story narrated by the "Voice of the World", with a short in-line tutorial ("Field note") in every quest:
  - **Field Guide**: controls tutorial. Every key shown is the player's own current binding (race ability, status menu, ability slots and modes, dodge, naming, Great Sage, Nightmares deep slots, councils, Cataclysm gear, backpack/accessories/map, Ultimine, quest book).
  - **Dimensions** group: Twilight Forest, Eternal Starlight, Chrono Dawn, Lesser Dimensions (The Afterdark, graves and liches from Ice and Fire, and secret Elemental Realm/Kamui quests).
  - **Boss Hunts** group: Cataclysm Hunts, Mowzie's Hunts.
  - **Paths** group: Explorer's Path (more claimed/force-loaded chunks, faster /back), Homesteader's Path (more homes, faster /home), Hunter's Path (+10% maximum health per rank, see Known issues). Each has 5 ranks plus 5 optional bonus quests. 15 new ranks in `config/ftbranks-pack.snbt`.
  - **Homestead** group: Cooking and Farming (Farmer's Delight), Homestead and Travel (Comforts, Supplementaries, Waystones).
- **Tensura Addons** group, 5 more chapters for the new mods (book grows to 31 chapters, 834 quests): Ascension (magicule infrastructure, Great Mage line, Ultimate awakening), Lineages of Ascension (all 69 races in 11 lineages), Origins (True Dragons, Dragotite gear, progenitor angels and daemons, the sub-dragon forms), Blood and Avalon (Bloodfiend line, Avalon relics, secret Lord-tier skills) and Elite Forge (Elite skills, the Saiyan line, armoury, plushie collection). Skills or items without a documented source are optional or secret quests.
- Progression tiers: high-tier chapters unlock with the Miner's Path milestones (iron, diamond, Nether, Wither); later acts and bosses are hidden until earlier ones are done; side quests are secret until completed.
- `kubejs/server_scripts/dimension_gate.js`: survival players who enter Eternal Starlight or Chrono Dawn before visiting the Nether, or The Afterdark before summoning a Wither, are sent back to their bed or spawn with a message. Creative, spectator and (by default) operators are exempt. Twilight Forest stays open.
- Mods: Tensura: Ascension, TensuraMoreSkills, Elite Tensura Addon, Tensura: Origins.

### Fixed
- Quest command rewards ran at permission level 0, so rank rewards (Miner's Path and all new paths) only worked for operators. All command rewards now run at level 4 and show a readable name and icon (for example "Rank: Apprentice Miner") instead of the raw command.
- "Land of the Dead" (Explorer's Journal) needs a biome that only exists in the unreachable Dread Lands dimension; it is now a secret optional quest with a mysterious description.

### Known issues
- The Hunter's Path health bonus is applied with a vanilla attribute command and has not been tested against Tensura's own health system.
- The Afterdark teleport catalyst is only found in chests (15% in six loot tables); there is no recipe.
- The Ice and Fire Dread Lands dimension has no working entrance in survival.


## [0.1.1] - 2026-10-07
Fixes found while testing the 0.1.0 content; same mod list.

### Changed
- Server pack no longer bundles three mods whose authors disallow redistribution (Tensura: Better Subordinates, Enigmatic, Unique Monsters); `SERVER_HOSTING.md` links to them. Removed ServerPackCreator's `manifest.json` and Easy NPC's generated skin templates from the server zip. Credits added for the open-licensed bundled mods whose CurseForge distribution toggle is off (Easy NPC, Custom Chest Menus, FiltPick).

### Fixed
- Quest IDs: FTB Quests replaces any ID whose first hex digit is 8-F and drops the dependencies that pointed at it. Remapped those IDs in `miners_path` and the boss-structure quests in `adventure` (and the lang keys), restoring the quest chains.
- Players spawning on tree canopies (tall Terralith forests): new `kubejs/server_scripts/spawn_off_leaves.js` moves a player who logs in or respawns standing on leaves near the world spawn down to the nearest open ground. Verified in-game.

## [0.1.0] - 2026-10-03
First public beta.

### Added
- Terralith (with Lithostitched, its dependency). Biomes only change in newly generated chunks.
- The Twilight Forest, Eternal Starlight, Chrono Dawn and The Afterdark: four own-dimension content mods; no overworld biome changes.
- L_Ender's Cataclysm (with Lionfish API) and Mowzie's Mobs: overworld bosses and structures; Tensura addons Guild, Enigmatic and Unique Monsters.
- `kubejs/data/cataclysm/tags/worldgen/biome/has_structure/`: Cataclysm hardcodes vanilla biomes for some structures; Frosted Prison / abandoned structures now also spawn in Terralith's snowy lowlands (about half the distance from spawn in testing), Cursed Pyramid / desert structures accept Terralith deserts.
- `kubejs/data/forge/tags/worldgen/biome/has_structure/`: the six Tensura Boss Structure spawn-biome tags now also accept Terralith biomes (via `#c:is_*` tags). Without this the structures only spawn in vanilla biomes, which Terralith makes rare.
- Server pack only: Chunky 1.4.23 (pregenerates chunks; `/chunky` commands for server owners). Not in the client pack.
- Farmer's Delight (enables the Ice and Fire cooking recipes), Supplementaries (galleons, road signs, wall-mounted lanterns), Comforts and Chat Heads (client-only).
- FTB Ranks 2101.1.5 (command permissions; default ranks behave like vanilla). `SERVER_HOSTING.md` documents hosting, Chunky and ranks.
- Leveling system (first path): new "Miner's Path" quest chapter grants `miner_1`..`miner_5` ranks via `config/ftbranks-pack.snbt`. Ultimine now starts at 8 blocks / 2 s cooldown, needs a real tool, costs more hunger (`exhaustion_per_block` 50), and scales to 64 blocks / 0.5 s with rank. Quest book is now 14 chapters.
- `kubejs/data/tensura/tags/`: corrected two Nightmares tag typos (`trightmare:` / `trnighmtare:`) that stopped the creative-flight race tag and the Rotted Wizard Tower tome skill tag from loading. `medium_thrall_dragon` (does not exist) mapped to `greater_thrall_dragon`. Overrides use `replace: true`; revisit after a Nightmares update.
- Silenced unfixable load errors (Farmer's Delight recipes without Farmer's Delight, two Nightmares recipes, two Dungeons Arise advancements) with false-conditioned overrides; server log now has 0 errors.
- Server pack synced to client mod versions (14 mods updated, e.g. Chrono Dawn 0.11.0, Easy NPC 7.14.0, Sophisticated Core/Storage).

Tested on a 1.21.1 dedicated server: all six structures generate in Terralith worlds, none buried.
The four dimension mods boot and generate on the dedicated server with no errors; boss structures still found.
Cataclysm, Mowzie's and the three Tensura addons also boot cleanly; all Cataclysm and Mowzie's structures were found in Terralith worlds.

### Removed
- Better Auto Third Person: its jar has no `modLoader` entry, so NeoForge refuses it and the client crashes on launch.
- Lanterns Belong on Walls: its copper data maps reference blocks that do not exist in 1.21.1, which breaks the `oxidizables`/`waxables` data maps; Supplementaries already covers wall lanterns.
- Essential and EssentialTweaks (multiplayer overlay/cosmetics; not needed), plus their leftover config and keybind entries.
- Disabled leftovers: Embeddium, old Iris 1.8.12, Sodium addon jars, tensura_trepu, wiki mod

### Changed
- Distant Horizons defaults lowered for typical hardware: LOD radius 256 to 128, threads 8 to 4 (`config/DistantHorizons.toml`).
- Default max FPS 180 to 120 (`config/defaultoptions/options.txt`).
- Added spark (profiler), Waystones/Spawnstones/Waystones2Waypoints2, Ping Wheel/Ping to Map, Patchouli, Tensura: Mysticism, Tensura Boss Structure.
- Adventure quests: hints on the Orc Disaster and Charybdis kill quests; new "Boss Maps" quest (buy maps from Cartographer villagers) plus six structure quests for the Tensura Boss Structure locations.

### Fixed
- Server pack was missing `dummmmmmy` (a Moonlight-based entity mod), which would have stopped clients from joining; added. Server pack synced to client versions and rebuilt (125 jars).
- Music toasts showed raw ids (e.g. `menu-02`) for TIMM tracks: TIMM's `musics.json` keys lacked the `music/` path segment that MusicNotification looks up. Merged override in `kubejs/assets/musicnotification/musics.json`.
- 12 broken `trnightmare` recipes (Excalibur, Caliburn, Terrablade, The World, The Asura, Ark, Lostvayne, Reinhard Locked, Dragon Seal, Divine Axe Rhitta, Ancient History Book, Evil Attribute Stick): the mod uses Tensura 1.x ids (`tensura:smithing`, `block_of_*`, `demon_essence`). Corrected overrides in `kubejs/data/trnightmare/recipe/`.

### Known issues
- `trnightmare` Ancient Grimoire and Galand Halberd recipes stay broken (missing item / `trmysticism` not installed). Ice and Fire pinned to 2.0-beta.15 because `tensura_iaf` 2.0.0.1 needs classes removed in 2.1.x.
