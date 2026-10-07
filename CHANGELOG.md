# Changelog

Versioning: [SemVer](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-10-03
First public beta.

### Added
- Terralith (with Lithostitched, its dependency). Biomes only change in newly generated chunks.
- The Twilight Forest, Eternal Starlight, Chrono Dawn and The Afterdark: four own-dimension content mods; no overworld biome changes.
- L_Ender's Cataclysm (with Lionfish API) and Mowzie's Mobs: overworld bosses and structures; Tensura addons Guild, Enigmatic and Unique Monsters.
- `kubejs/data/cataclysm/tags/worldgen/biome/has_structure/`: Cataclysm hardcodes vanilla biomes for some structures; Frosted Prison / abandoned structures now also spawn in Terralith's snowy lowlands (about half the distance from spawn in testing), Cursed Pyramid / desert structures accept Terralith deserts.
- `kubejs/data/forge/tags/worldgen/biome/has_structure/`: the six Tensura Boss Structure spawn-biome tags now also accept Terralith biomes (via `#c:is_*` tags). Without this the structures only spawn in vanilla biomes, which Terralith makes rare.
- Server pack only: Chunky 1.4.23 (pregenerates chunks; `/chunky` commands for server owners). Not in the client pack.
- FTB Ranks 2101.1.5 (command permissions; default ranks behave like vanilla). `SERVER_HOSTING.md` documents hosting, Chunky and ranks.

Tested on a 1.21.1 dedicated server: all six structures generate in Terralith worlds, none buried.
The four dimension mods boot and generate on the dedicated server with no errors; boss structures still found.
Cataclysm, Mowzie's and the three Tensura addons also boot cleanly; all Cataclysm and Mowzie's structures were found in Terralith worlds.

### Removed
- Essential and EssentialTweaks (multiplayer overlay/cosmetics; not needed), plus their leftover config and keybind entries.
- Disabled leftovers: Embeddium, old Iris 1.8.12, Sodium addon jars, tensura_trepu, wiki mod

### Changed
- Distant Horizons defaults lowered for typical hardware: LOD radius 256 to 128, threads 8 to 4 (`config/DistantHorizons.toml`).
- Default max FPS 180 to 120 (`config/defaultoptions/options.txt`).
- Added spark (profiler), Waystones/Spawnstones/Waystones2Waypoints2, Ping Wheel/Ping to Map, Patchouli, Tensura: Mysticism, Tensura Boss Structure.
- Adventure quests: hints on the Orc Disaster and Charybdis kill quests; new "Boss Maps" quest (buy maps from Cartographer villagers) plus six structure quests for the Tensura Boss Structure locations.

### Fixed
- Music toasts showed raw ids (e.g. `menu-02`) for TIMM tracks: TIMM's `musics.json` keys lacked the `music/` path segment that MusicNotification looks up. Merged override in `kubejs/assets/musicnotification/musics.json`.
- 12 broken `trnightmare` recipes (Excalibur, Caliburn, Terrablade, The World, The Asura, Ark, Lostvayne, Reinhard Locked, Dragon Seal, Divine Axe Rhitta, Ancient History Book, Evil Attribute Stick): the mod uses Tensura 1.x ids (`tensura:smithing`, `block_of_*`, `demon_essence`). Corrected overrides in `kubejs/data/trnightmare/recipe/`.

### Known issues
- `trnightmare` Ancient Grimoire and Galand Halberd recipes stay broken (missing item / `trmysticism` not installed). Ice and Fire pinned to 2.0-beta.15 because `tensura_iaf` 2.0.0.1 needs classes removed in 2.1.x.
