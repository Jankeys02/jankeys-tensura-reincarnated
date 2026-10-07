# Changelog

Versioning: [SemVer](https://semver.org/).

## [Unreleased]

### Fixed
- Great Sage menu and Elite Tensura Council screen both defaulted to `I`, so neither opened. The Council screen now defaults to `O` (Iris's shader-menu key is unbound; Video Settings still opens it) (only for new installs; existing players can rebind in Controls).

### Removed
- Ragdollified and Ragdollified Player Corpses.
- Waystones2Waypoints2 (Xaero's Minimap already shows waystones itself, so every waystone had a duplicate marker).

## [0.2.2] - 2026-10-07
Everything since 0.1.1 in player terms: the quest-book release. The book grows from 14 to 31 chapters (830 quests), told by the "Voice of the World", with a short tutorial ("Field note") in every quest. Release tooling also changed (packwiz mod list, automatic release builds); see DEVELOPMENT.md.

### Added
- **Field Guide** chapter: a controls tutorial that shows your own key bindings (race ability, status menu, ability slots, dodge, naming, Great Sage, Ultimine, quest book and more).
- **Dimensions** chapters: Twilight Forest, Eternal Starlight, Chrono Dawn, and Lesser Dimensions (The Afterdark, Ice and Fire graves and liches, secret Elemental Realm/Kamui quests).
- **Boss Hunts** chapters: Cataclysm and Mowzie's Mobs.
- **Paths** with 5 ranks plus bonus quests each: Explorer's Path (more claimed chunks, faster /back), Homesteader's Path (more homes, faster /home) and Hunter's Path (+10% max health per rank). Each rank also grants a Tensura skill.
- **Homestead** chapters: Cooking and Farming (Farmer's Delight), Homestead and Travel (Comforts, Supplementaries, Waystones).
- **Tensura Addons** chapters for the new mods: Ascension, Lineages of Ascension (all 69 races in 11 lineages), Origins, Blood and Avalon, and Elite Forge.
- Four new Tensura addons: Tensura: Ascension, TensuraMoreSkills, Elite Tensura Addon, Tensura: Origins.
- **Dimension gate:** in survival, entering Eternal Starlight or Chrono Dawn before visiting the Nether, or The Afterdark before summoning a Wither, sends you back to your bed or spawn with a message. Creative, spectator and (by default) operators are exempt. Twilight Forest stays open.

### Changed
- Chapters are grouped in the sidebar (Beginnings, Tensura, World, Dimensions, Boss Hunts, Homestead, Paths, Tensura Addons, Records).
- Race catalogs show one row per lineage and reveal later forms as you reach them. Your Evolution Paths progress from 0.1.1 is kept.
- Later acts and bosses stay hidden until earlier ones are done; side quests are secret until completed.
- Rewards were rebalanced: boss quests pay 15 levels and chapter finals pay 25, plus existence points on chapter finals.
- Removed five Adventure quests that repeated other chapters; "Hear Me, Direwolves" is now "Pack Hunters".

### Fixed
- Eight Skills and Spirits quests (Magicule Reserves, Sea of Magicules, Aura, Overwhelming Aura) could never complete. They work now.
- Rank rewards (Miner's Path and the new paths) only worked for operators. They now work for everyone.
- "Land of the Dead" needed a biome you can't reach in survival; it is now a secret optional quest.

### Known issues
- The Path skill rewards and the chapter-final EP rewards haven't been claimed in game yet.
- The Hunter's Path health bonus hasn't been tested against Tensura's own health system.
- The Afterdark teleport catalyst is only found in chests; it has no recipe.
- The Ice and Fire Dread Lands dimension has no working entrance in survival.

Back up your world before updating. World generation mods only affect newly generated chunks.

### Server pack
The server pack now installs its mods with an installer instead of shipping them inside the zip, so the mods always match the release.

- The zip holds the configs, quests and KubeJS scripts, plus `install-mods.bat` / `install-mods.sh`, which download the server's 130 mods for this exact release. Client-only mods are skipped.
- Chunky (pregeneration) is included.
- Built from the same mod list as the client pack, so the two stay in step.
- Includes the quest-book changes above, including the dimension gate.

How to set up:
1. Unzip, install NeoForge 21.1.249 (Minecraft 1.21.1, Java 21).
2. Run the installer script.
3. Six mods can't be downloaded automatically (their authors block it): Custom Chest Menus, Easy NPC, FiltPick, Tensura: Better Subordinates, Tensura: Enigmatic, Tensura: Unique Monsters. The installer prints a link for each. Save the files into `mods/` and run the installer again.
4. Accept the Minecraft EULA yourself, give it 4-8 GB of RAM, and open UDP 24454 for proximity voice chat.

Boot-tested with the current mod list: starts without crashing and loads all quests. Not yet tested with a real player joining.

## [0.2.1] - 2026-10-07
Not released: the tag exists but the release build failed. See 0.2.2.

## [0.2.0] - 2026-10-07
The quest-book release: 17 new chapters narrated by the Voice of the World, four Tensura addons, a full audit of the book, and the dimension gate. Mods added since 0.1.1 are All Rights Reserved and are linked, not bundled, in the server pack.

### Added
- **12 new quest chapters** (book grows from 14 to 26 chapters, 365 to 620 quests, before the addon chapters below), written as a story narrated by the "Voice of the World", with a short in-line tutorial ("Field note") in every quest:
  - **Field Guide**: controls tutorial. Every key shown is the player's own current binding (race ability, status menu, ability slots and modes, dodge, naming, Great Sage, Nightmares deep slots, councils, Cataclysm gear, backpack/accessories/map, Ultimine, quest book).
  - **Dimensions** group: Twilight Forest, Eternal Starlight, Chrono Dawn, Lesser Dimensions (The Afterdark, graves and liches from Ice and Fire, and secret Elemental Realm/Kamui quests).
  - **Boss Hunts** group: Cataclysm Hunts, Mowzie's Hunts.
  - **Paths** group: Explorer's Path (more claimed/force-loaded chunks, faster /back), Homesteader's Path (more homes, faster /home), Hunter's Path (+10% maximum health per rank, see Known issues). Each has 5 ranks plus 5 optional bonus quests. 15 new ranks in `config/ftbranks-pack.snbt`.
  - **Homestead** group: Cooking and Farming (Farmer's Delight), Homestead and Travel (Comforts, Supplementaries, Waystones).
- **Tensura Addons** group, 5 more chapters for the new mods (book grows to 31 chapters; 830 quests after the audit below): Ascension (magicule infrastructure, Great Mage line, Ultimate awakening), Lineages of Ascension (all 69 races in 11 lineages), Origins (True Dragons, Dragotite gear, progenitor angels and daemons, the sub-dragon forms), Blood and Avalon (Bloodfiend line, Avalon relics, secret Lord-tier skills) and Elite Forge (Elite skills, the Saiyan line, armoury, plushie collection). Skills or items without a documented source are optional or secret quests.
- Progression tiers: high-tier chapters unlock with the Miner's Path milestones (iron, diamond, Nether, Wither); later acts and bosses are hidden until earlier ones are done; side quests are secret until completed.
- `kubejs/server_scripts/dimension_gate.js`: survival players who enter Eternal Starlight or Chrono Dawn before visiting the Nether, or The Afterdark before summoning a Wither, are sent back to their bed or spawn with a message. Creative, spectator and (by default) operators are exempt. Twilight Forest stays open.
- Mods: Tensura: Ascension, TensuraMoreSkills, Elite Tensura Addon, Tensura: Origins. All four are All Rights Reserved: the server pack must not bundle them. `SERVER_HOSTING.md` links them, and they should be added as Required Dependencies on the server-pack file on CurseForge (ids 1505110, 1399788, 515631, 1230188).

### Changed (quest-book audit, 2026-10-07)
- Sidebar: every chapter now sits in a group (Beginnings, Tensura, World, Dimensions, Boss Hunts, Homestead, Paths, Tensura Addons, Records); Miner's Path moved into Paths. Each new chapter has a subtitle tooltip saying which mod it covers and what unlocks it.
- Race catalogs (Evolution Paths, Lineages of Ascension, the Origins progenitors, the Bloodfiend and Saiyan lines) show one row per lineage: only the first race is visible, the final form(s) appear once you have been recorded as any stage of that lineage, and the stages in between appear as you reach them. Quest ids of the 0.1.1 Evolution Paths chapter are unchanged, so progress on them survives.
- Reward scale unified: boss quests in the new chapters pay 15 levels (was 8), chapter finals 25 (was 10). Chapter finals also grant existence points (1,000 to 10,000 EP) through the Tensura quest reward.
- Paths: each Explorer, Hunter and Homesteader rank now also grants a Tensura skill (senses, resistances, Strength, Haki, Farsight, Self-Regeneration; the Homesteader's final rank grants the Unique Skill Cook).
- Removed five Adventure quests that only repeated tasks from Caves and Treasure, Dragons and Myths or the Paths (Hot Feet, Down in the Dark, Temple Run, Dragon Egg, Dragonslayer); "Hear Me, Direwolves" (Adventure) is now "Pack Hunters". Repeated narrator lines in the addon catalogs were varied. The Nightingale armour quest (Elite Forge) was removed: the set is not a registered item. Book: 31 chapters, 830 quests.

### Fixed
- Eight Skills and Spirits quests (Magicule Reserves I to III, Sea of Magicules, Aura I to III, Overwhelming Aura) could never complete: their task type did not exist and FTB Quests had replaced it with an empty custom task. They now use the Tensura existence-value task (max magicules / max aura).
- Quest command rewards ran at permission level 0, so rank rewards (Miner's Path and all new paths) only worked for operators. All command rewards now run at level 4 and show a readable name and icon (for example "Rank: Apprentice Miner") instead of the raw command.
- "Land of the Dead" (Explorer's Journal) needs a biome that only exists in the unreachable Dread Lands dimension; it is now a secret optional quest with a mysterious description.

### Known issues
- The Path skill rewards (`tensura_ftb:ability`) and the chapter-final EP rewards (`tensura_ftb:existence_value`) load and serialise correctly but have not been claimed in game yet.
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
