from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random
import block

app = Ursina()
Sky()
player = FirstPersonController()
# window.fullscreen = True
arm = Entity(
    parent=camera.ui,
    model='cube',
    color=color.blue,
    position=(0.75, -0.6),
    rotation=(150, -10, 6),
    scale=(0.2, 0.2, 1.5)
)


def update():
    if held_keys['left mouse']:
        arm.position = (0.6, -0.5)
    elif held_keys['right mouse']:
        arm.position = (0.6, -0.5)
    else:
        arm.position = (0.75, -0.6)


boxes = []

for n in range(16):
    for k in range(16):
        if random.randint(0, 3) == 0:
            box = Button(
                position=(k, 0, n),
                color=color.white50,
                model='cube',
                texture=load_texture('assets/water'),
                origin_y=0.5,
                parent=scene
            )
        else:
            box = Button(
                position=(k, 0, n),
                color=color.white,
                model='cube',
                texture=load_texture('assets/grass.png'),
                origin_y=0.5,
                parent=scene
            )
        boxes.append(box)
        for i in range(1, 4):
            box = Button(
                position=(k, -i, n),
                color=color.white,
                model='cube',
                texture=load_texture('assets/dirt'),
                origin_y=0.5,
                parent=scene
            )
            boxes.append(box)
        for i in range(4, 8):
            a = random.randint(0, 70)
            if a == 0:
                box = Button(
                    position=(k, -i, n),
                    color=color.white,
                    model='cube',
                    texture=load_texture('assets/diamond'),
                    origin_y=0.5,
                    parent=scene
                )
            elif a < 4:
                box = Button(
                    position=(k, -i, n),
                    color=color.white,
                    model='cube',
                    texture=load_texture('assets/iron'),
                    origin_y=0.5,
                    parent=scene
                )
            elif a < 9:
                box = Button(
                    position=(k, -i, n),
                    color=color.white,
                    model='cube',
                    texture=load_texture('assets/coal'),
                    origin_y=0.5,
                    parent=scene
                )
            else:
                box = Button(
                    position=(k, -i, n),
                    color=color.white,
                    model='cube',
                    texture=load_texture('assets/stone'),
                    origin_y=0.5,
                    parent=scene
                )
            boxes.append(box)


def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                boxes.remove(box)
                destroy(box)

            if key == 'right mouse down':
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model='cube',
                    texture=load_texture('assets/stone'),
                    origin_y=0.5,
                    parent=scene
                )
                boxes.append(newBox)


app.run()
