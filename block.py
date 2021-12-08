from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random


class Block(Entity):
    def __init__(self, pos,  add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities=add_to_scene_entities, **kwargs)
        position = pos
        color = color.white
        model = "cube"
        texture = load_texture('assets/default')
        origin_y = 0.5
        parent = scene


class grass_block(Block):
    def __init__(self, pos, add_to_scene_entities=True, **kwargs):
        super().__init__(pos, add_to_scene_entities=add_to_scene_entities, **kwargs)
        texture = load_texture('assets/grass')
