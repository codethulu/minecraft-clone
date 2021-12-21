from ursina import *
from ursina import collider
from ursina.color import rgba
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random
from ursina.shaders import basic_lighting_shader
from ursina.shaders import colored_lights_shader


from ursina.scripts.colorize import colorize
defaultpath = "assets/blocks/"


class Block(Button):
    def __init__(self, pos):
        super().__init__()
        self.parent = scene
        self.model = 'cube'
        self.collider = 'box'
        self.color = color.color(0, 0, 1)

        self.texture = load_texture(defaultpath+'default')
        self.origin_y = 0.5
        self.parent = scene
        self.position = pos
        self.hardness = 5
        self.highlight_color = color.white
        shader = colored_lights_shader

    def destroy(self):
        self.hardness -= 1

    def update(self):
        return


class bedrock(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "bedrock"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 10000

    def destroy(self):
        self.highlight_color = color.red


class grass(Block):
    def __init__(self, pos, var):
        super().__init__(pos)
        self.name = "grass"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class dirt(Block):
    def __init__(self, pos, var):
        super().__init__(pos)
        self.name = "dirt"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class mud(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "mud"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class mudBrick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "mud-brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class sand(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "sand"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1

class clay(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "clay"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1
class stone(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "stone"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1

class magma(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.var = 0
        self.name = "magma"
        self.texture = load_texture(defaultpath + self.name + '-' + str(self.var))
        self.hardness = 1
        self.animationConstant = 50
    def update(self):
        if self.animationConstant==0:
            self.animationConstant=50
            self.var+=1
            if self.var>9:
                self.var = 0
            self.texture = load_texture(defaultpath + self.name + '-' + str(self.var))
        else:
            self.animationConstant-=1

class amber(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.var = 0
        self.name = "amber"
        self.texture = load_texture(defaultpath + self.name + '-' + str(self.var))
        self.hardness = 1
        self.animationConstant = 50
    def update(self):
        if self.animationConstant==0:
            self.animationConstant=50
            self.var+=1
            if self.var>8:
                self.var = 0
            self.texture = load_texture(defaultpath + self.name + '-' + str(self.var))
        else:
            self.animationConstant-=1

class amethyst(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.var = 0
        self.name = "amethyst"
        self.texture = load_texture(defaultpath + self.name + '-' + str(self.var))
        self.hardness = 1
        self.animationConstant = 50
    def update(self):
        if self.animationConstant==0:
            self.animationConstant=50
            self.var+=1
            if self.var>11:
                self.var = 0
            self.texture = load_texture(defaultpath + self.name + '-' + str(self.var))
        else:
            self.animationConstant-=1

class obsidian(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "obsidian"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1
class obsidianBrick(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "obsidian-brick"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1
class gravel(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "gravel"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1
class stoneBrick(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "stone-brick"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class stoneTiles(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "stone-tiles"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class terracotta(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "terracotta"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class brick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class terracottaTiles(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "terracotta-tiles"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class concrete(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "concrete"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class concreteBrick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "concrete-brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class concretePillar(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "concrete-pillar"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1

class sandstone(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "sandstone"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class sandstoneBrick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "sandstone-brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class sandstonePillar(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "sandstone-pillar"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1

class marble(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "marble"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class marbleBrick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "marble-brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class marblePillar(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "marble-pillar"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1

class basalt(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "basalt"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class basaltBrick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "basalt-brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class basaltTiles(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "basalt-tiles"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1

class log(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "log"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1

class leaves(Block):
    def __init__(self, pos):
        super().__init__(pos)
        # self.Branches = Block(texture=load_texture(defaultpath + "branches"), scale=(0.6,0.6,0.6))

        self.name = "leaves"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1
        self.collider = MeshCollider


class wood(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "wood"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class ash(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "ash"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class glass(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "glass"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class iron(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "iron"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1

class ironPlating(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "iron-plating"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1

class water(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.var = 0
        self.name = "water"
        self.texture = load_texture(defaultpath + self.name + '-' + str(self.var))
        self.hardness = 1
        self.animationConstant = 50
        self.color = color.white50
        self.scale = Vec3(1,0.9,1)
        self.render_queue=1
        self.y-=0.1
    def update(self):
        if self.animationConstant==0:
            self.animationConstant=50
            self.var+=1
            if self.var>8:
                self.var = 0
            self.texture = load_texture(defaultpath + self.name + '-' + str(self.var))
        else:
            self.animationConstant-=1