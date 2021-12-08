from ursina import *
from ursina import collider
from ursina.color import rgba
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random

from ursina.scripts.colorize import colorize


class Block(Entity):
    def __init__(self, pos):
        super().__init__()
        self.parent = scene
        self.model = 'cube'
        self.collider = 'box'
        self.color = color.color(0, 0, 0.8)

        self.texture = load_texture('assets/default')
        self.origin_y = 0.5
        self.parent = scene

        self.position = pos

    def update(self):
        self.color = color.color(0, 0, 0.8)


class grass(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.texture = load_texture('assets/grass')
