// Dimension gate: keeps low-progress survival players out of the high-tier dimensions.
// A player standing in a gated dimension without the required advancement is sent back to the overworld (their bed
// if it is in the overworld, otherwise the world spawn) with a short message. The required advancements are the same
// vanilla milestones the Miner's Path rank quests use: Nether visited = tier 3, Wither summoned = tier 4.
// Twilight Forest is deliberately NOT gated (tier 2, left open).
// Creative/spectator players are exempt, and so are operators unless EXEMPT_OPERATORS is false (set it to false to
// test the gate as an op, then `/kubejs reload server_scripts`).

const EXEMPT_OPERATORS = true
const CHECK_EVERY_TICKS = 20

// dimension id -> [required advancement, message]
const GATES = {
  'eternal_starlight:starlight': ['minecraft:story/enter_the_nether', 'The sky here is not ready for you. Return once you have seen the nether.'],
  'chronodawn:chronodawn': ['minecraft:story/enter_the_nether', 'Time here is not ready for you. Return once you have seen the nether.'],
  'the_afterdark:afterdark': ['minecraft:nether/summon_wither', 'The dark below is not ready for you. Return once you have called a wither.']
}

const GateResourceLocation = Java.loadClass('net.minecraft.resources.ResourceLocation')
const GateHeightmap = Java.loadClass('net.minecraft.world.level.levelgen.Heightmap$Types')

function advancementDone(player, id) {
  const holder = player.server.getAdvancements().get(GateResourceLocation.parse(id))
  if (holder == null) return true // unknown advancement: never lock a player out because of a typo
  return player.getAdvancements().getOrStartProgress(holder).isDone()
}

function sendHome(player, message) {
  const server = player.server
  const overworld = server.overworld()
  let x, y, z
  const bed = player.getRespawnPosition()
  if (bed != null && String(player.getRespawnDimension()).indexOf('minecraft:overworld') !== -1) {
    x = bed.getX() + 0.5
    y = bed.getY()
    z = bed.getZ() + 0.5
  } else {
    const spawn = overworld.getSharedSpawnPos()
    x = spawn.getX() + 0.5
    z = spawn.getZ() + 0.5
    y = overworld.getHeight(GateHeightmap.MOTION_BLOCKING, spawn.getX(), spawn.getZ())
  }
  player.teleportTo(overworld, x, y, z, player.getYRot(), player.getXRot())
  server.runCommandSilent('tellraw ' + player.getGameProfile().getName() + ' {"text":"' + message + '","color":"gray","italic":true}')
  console.info('dimension_gate: sent ' + player.getGameProfile().getName() + ' home from a gated dimension')
}

PlayerEvents.tick(event => {
  const player = event.player
  if (player.tickCount % CHECK_EVERY_TICKS !== 0) return
  if (player.isCreative() || player.isSpectator()) return
  if (EXEMPT_OPERATORS && player.hasPermissions(2)) return
  const dimension = String(player.level.dimension)
  for (const id in GATES) {
    if (dimension.indexOf(id) === -1) continue
    const gate = GATES[id]
    if (!advancementDone(player, gate[0])) sendHome(player, gate[1])
    return
  }
})
