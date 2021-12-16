import blocks
import random


def convert(name, position):
    if name == "grass":
        return blocks.grass(position, 0)
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
    if name == "ash":
        return blocks.ash(position)
    if name == "glass":
        return blocks.glass(position)
    if name == "sand":
        return blocks.sand(position)
    if name == "stone":
        return blocks.stone(position)
    if name == "stone-brick":
        return blocks.stoneBrick(position)
    if name == "stone-tiles":
        return blocks.stoneTiles(position)
    if name == "concrete":
        return blocks.concrete(position)
    if name == "concrete-brick":
        return blocks.concreteBrick(position)
    if name == "concrete-pillar":
        return blocks.concretePillar(position)
    if name == "terracotta":
        return blocks.terracotta(position)
    if name == "brick":
        return blocks.brick(position)
    if name == "terracotta-tiles":
        return blocks.terracottaTiles(position, random.randint(0, 9))

    if name == "concrete":
        return blocks.concrete(position)
