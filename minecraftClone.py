from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random
import blocks

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

boxes = []


def update():
    for box in boxes:
        box.update()
    if held_keys['left mouse']:

        arm.position = (0.6, -0.5)
    elif held_keys['right mouse']:
        arm.position = (0.6, -0.5)
    else:
        arm.position = (0.75, -0.6)


for n in range(16):
    for k in range(16):
        boxes.append(blocks.grass((k, 0, n)))

        # box=Button(
        #     position=(k, 0, n),
        #     color=color.white50,
        #     model='cube',
        #     texture=load_texture('assets/water'),
        #     origin_y=0.5,
        #     parent=scene
        # )


# def input(key):
    # for box in boxes:
    #     if box.hovered:
    #         if key == 'left mouse down':
    #             boxes.remove(box)
    #             destroy(box)

    #         if key == 'right mouse down':
    #             newBox = Button(
    #                 position=box.position + mouse.normal,
    #                 color=color.white,
    #                 model='cube',
    #                 texture=load_texture('assets/stone'),
    #                 origin_y=0.5,
    #                 parent=scene
    #             )
    #             boxes.append(newBox)


app.run()
