import blocks
import random


def convert(name, position):
    if name == "grass":
        return blocks.grass(position, 0)
    if name == "meadow":
        return blocks.grass(position, random.randint(1, 2))
    if name == "dirt":
        return blocks.dirt(position, random.randint(0, 3))
    if name == "mud":
        return blocks.mud(position)
    if name == "mud-brick":
        return blocks.mudBrick(position)
    if name == "log":
        return blocks.log(position, random.randint(0, 1))
    if name == "wood":
        return blocks.wood(position)
    if name == "leaves":
        return blocks.leaves(position)
    if name == "ash":
        return blocks.ash(position)
    if name == "glass":
        return blocks.glass(position)
    if name == "sand":
        return blocks.sand(position)
    if name == "clay":
        return blocks.clay(position)
    if name == "stone":
        return blocks.stone(position,0)
    if name == "magma":
        return blocks.magma(position)
    if name == "amber":
        return blocks.amber(position)
    if name == "amethyst":
        return blocks.amethyst(position)
    if name == "quartz":
        return blocks.quartz(position)
    if name == "zircon":
        return blocks.zircon(position)
    if name == "ruby":
        return blocks.ruby(position)
    if name == "obsidian":
        return blocks.obsidian(position)
    if name == "obsidian-brick":
        return blocks.obsidianBrick(position,random.randint(0,3))
    if name == "gravel":
        return blocks.gravel(position)
    if name == "stone-brick":
        return blocks.stoneBrick(position,0)
    if name == "mossy-stone":
        return blocks.stone(position,1)
    if name == "mossy-stone-brick":
        return blocks.stoneBrick(position,1)
    if name == "stone-tiles":
        return blocks.stoneTiles(position)
    if name == "concrete":
        return blocks.concrete(position)
    if name == "concrete-brick":
        return blocks.concreteBrick(position)
    if name == "concrete-pillar":
        return blocks.concretePillar(position)
    if name == "marble":
        return blocks.marble(position)
    if name == "marble-brick":
        return blocks.marbleBrick(position)
    if name == "marble-pillar":
        return blocks.marblePillar(position)
    if name == "sandstone":
        return blocks.sandstone(position)
    if name == "sandstone-brick":
        return blocks.sandstoneBrick(position)
    if name == "sandstone-pillar":
        return blocks.sandstonePillar(position)
    if name == "basalt":
        return blocks.basalt(position)
    if name == "basalt-brick":
        return blocks.basaltBrick(position)
    if name == "basalt-tiles":
        return blocks.basaltTiles(position)
    if name == "terracotta":
        return blocks.terracotta(position)
    if name == "brick":
        return blocks.brick(position)
    if name == "terracotta-tiles":
        return blocks.terracottaTiles(position, random.randint(0, 9))

    if name == "concrete":
        return blocks.concrete(position)

    if name == "iron":
        return blocks.iron(position)
    if name == "iron-plating":
        return blocks.ironPlating(position, random.randint(0, 4))
    if name == "water":
        return blocks.water(position)
