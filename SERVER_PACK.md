# Server pack plan

NeoForge 21.1.249 / Minecraft 1.21.1. Built from the client pack, minus client-only mods.
Mod ids below are `modId`s from each jar's `neoforge.mods.toml` (176 mods in `mods/`: 124 kept on the server, 52 excluded; the server pack has 125 jars: those 124 plus server-only Chunky; staged in `../../ServerPacks/jankeys-tensura-0.1.0-server`).

## Exclude from the server (client-only)
Rendering / performance (client): `sodium`, `sodium_extra`, `reeses_sodium_options`, `sodiumextrainformation`, `iris`, `immediatelyfast`, `entityculling`, `moreculling`, `entity_model_features`, `entity_texture_features`, `vanillin`, `badoptimizations`, `dynamic_fps`, `smoothchunk`, `chloride`
Animation / visuals: `firstperson`, `notenoughanimations`, `skinlayers3d`, `modefite`, `manas_cosmetics`, `advancementplaques`, `ragdollified`*
UI / HUD / QoL: `chat_heads`, `cinematiczoom`, `betteradvancements`, `controlling`, `mousetweaks`, `extremesoundmuffler`, `trashslot`, `obscure_tooltips`, `betteradvancedtooltips`, `enchdesc`, `jei`, `jeresources`, `ftbjeiextras`, `searchables`, `defaultoptions`, `ftbqopt`
Map: `xaerominimap`, `xaeroworldmap`, `ftbxaerocompat`, `pingtomapxaeros`, `w2w2` (Waystones2Waypoints2)
Audio: `musicnotification`, `timm`, `extrasounds`, `battlemusic`*, `sound_physics_remastered`

## Keep (server needs them)
`waystones`, `spawnstones`, `mysticism`, `tensura_boss_structure`, `patchouli`, `pingwheel` (both sides), `spark` (server profiler), `configuration` (library), `tensura`, `tensura_*`, `manas*`, `trnightmare`, `nightmareutils`, `greatsage`, `trying_to_make_an_addon`, `iceandfire`, `kubejs`, `rhino`, `ftb*` (chunks/essentials/quests/teams/ultimine/ranks/library/xmodcompat), `curios`, `artifacts`, `lootr`, `corpse`, `voicechat`, `dungeons_arise`, `yungs*` / `better*` structures, `terrablender`, `terralith`, `lithostitched` (Terralith dependency), `twilightforest`, `eternal_starlight`, `chronodawn`, `the_afterdark` (own-dimension content mods), `cataclysm`, `lionfishapi` (Cataclysm dependency), `farmersdelight`, `supplementaries`, `comforts`, `dummmmmmy`, `mowziesmobs`, `tensura_guild`, `tensuraenigmatic`, `tr_unique_monsters`, `chunky` (server-only pregenerator; not in the client pack), `sophistic*`, `backpacked`, libraries (`geckolib`, `architectury`, `balm`, `cloth_config`, `iceberg`, `bookshelf`, ...), `ferritecore`, `modernfix`, `krypton_fnp`, `fastleafdecay`, `alltheleaks`, `easy_npc*`, `watut`, `polymorph`, `carryon`, `incontrol`, `torchmaster`

## Uncertain: test on a real dedicated server
Marked `*` above plus `distanthorizons` (optional server side; leave out unless wanted), `punchy`, `fragmentum`, `showcaseitem`, `eliteholograms`, `cosmeticarmorreworked`, `corpse_waypoints`. NeoForge fails loudly at boot on a client-only mod, so start the server, remove what it names, repeat.

## Steps
1. Export the client pack from the CurseForge app (0.1.1).
2. Build the server zip with ServerPackCreator (downloads mods from CurseForge itself and writes start scripts) using the exclude list above.
3. Boot it, remove any mod that crashes on server.
4. Set `server.properties`, review `ftbessentials`/`ftbchunks`/`ftbteams` defaults for multiplayer.
5. Upload the zip as the "server pack" additional file on the CurseForge release.

## Boot test (2026-09-29)
Built with ServerPackCreator 9.0.0, then cleaned by hand (removed `*.jar.disabled`, plus AdvancementPlaques, ExtremeSoundMuffler, entityculling and JEI, which the tool left active; fixed `JAVA_ARGS` to `-Xms4G -Xmx8G`). Result: 107 mods, 210 MB zip.
- NeoForge 21.1.249 dedicated server reached `Done (11.7s)`; no client-only mod crashed. Loaded 5715 recipes, 13 quest chapters / 360 quests, all 12 `kubejs/data` recipe overrides, voice chat on UDP 24454.
- Known harmless log noise: `trnightmare` tag typos and the two unfixable recipes (Ancient Grimoire, Galand Halberd), Ice and Fire x Farmer's Delight recipes (Farmer's Delight not installed), two Dungeons Arise advancements, `forge:entity_gravity` attribute warnings, first-start "can't keep up" while the labyrinth dimension and EMC map are built.
- The EULA is not included in the zip; server owners accept it themselves.
- Not yet done: a real client joining the server.
- Not tested: FTB Ranks restrictions with a non-op player (needs a real client). The shipped default ranks add no restrictions, so behavior is vanilla; custom rules a host writes are untested.
