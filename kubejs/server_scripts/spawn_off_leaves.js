// Terralith forests are tall, and vanilla picks the world spawn from a heightmap that counts leaves,
// so players can spawn on top of a tree canopy. If a player (re)spawns near the world spawn standing
// on leaves, move them to the nearest real ground. Never moves anyone who is not on leaves.

const McHeightmap = Java.loadClass('net.minecraft.world.level.levelgen.Heightmap$Types')
const McBlockPos = Java.loadClass('net.minecraft.core.BlockPos')
const McBlockTags = Java.loadClass('net.minecraft.tags.BlockTags')

const SPAWN_RADIUS = 24 // only act this close to the world spawn
const SEARCH_RADIUS = 12 // how far to look for open ground
const OFFSETS = (function () {
  const list = []
  for (let dx = -SEARCH_RADIUS; dx <= SEARCH_RADIUS; dx++) {
    for (let dz = -SEARCH_RADIUS; dz <= SEARCH_RADIUS; dz++) list.push([dx, dz])
  }
  list.sort(function (a, b) { return (a[0] * a[0] + a[1] * a[1]) - (b[0] * b[0] + b[1] * b[1]) })
  return list
})()

function groundY(level, x, z) {
  // MOTION_BLOCKING_NO_LEAVES = first free y above the top non-leaf block
  const y = level.getHeight(McHeightmap.MOTION_BLOCKING_NO_LEAVES, x, z)
  const below = level.getBlockState(new McBlockPos(x, y - 1, z))
  if (below.is(McBlockTags.LEAVES) || below.is(McBlockTags.LOGS)) return null
  if (!below.getFluidState().isEmpty()) return null
  if (!level.getBlockState(new McBlockPos(x, y, z)).isAir()) return null
  if (!level.getBlockState(new McBlockPos(x, y + 1, z)).isAir()) return null
  return y
}

function groundPlayer(event) {
  const player = event.player
  const level = player.level
  // level.dimension is a KubeJS property (not a method); its string form contains the dimension id
  if (String(level.dimension).indexOf('minecraft:overworld') === -1) return
  const pos = player.blockPosition()
  const spawn = level.getSharedSpawnPos()
  if (Math.abs(pos.getX() - spawn.getX()) > SPAWN_RADIUS || Math.abs(pos.getZ() - spawn.getZ()) > SPAWN_RADIUS) return
  if (!level.getBlockState(pos.below()).is(McBlockTags.LEAVES)) return

  for (let i = 0; i < OFFSETS.length; i++) {
    const x = pos.getX() + OFFSETS[i][0]
    const z = pos.getZ() + OFFSETS[i][1]
    const y = groundY(level, x, z)
    if (y !== null) {
      const name = player.getGameProfile().getName()
      event.server.runCommandSilent('tp ' + name + ' ' + (x + 0.5) + ' ' + y + ' ' + (z + 0.5))
      console.info('spawn_off_leaves: moved ' + name + ' from the canopy at ' + pos.getX() + ' ' + pos.getY() + ' ' + pos.getZ() + ' to ' + x + ' ' + y + ' ' + z)
      return
    }
  }
}

PlayerEvents.loggedIn(groundPlayer)
PlayerEvents.respawned(groundPlayer)
