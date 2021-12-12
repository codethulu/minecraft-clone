from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random
import blocks
import inventory
import time

app = Ursina()
inventory = inventory.Inventory()
Sky()
player = FirstPersonController()
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = False
# window.fullscreen = True
arm = Entity(
    parent=camera.ui,
    model='cube',
    color=color.blue,
    position=(0.3, -0.6),
    rotation=(150, -10, 6),
    scale=(0.2, 0.2, 1.5)
)

inventory.append('saw', type="tool")
inventory.append('chisel', type="tool")
inventory.append('pickaxe', type="tool")
inventory.append('hammer', type="tool")
inventory.append('fire', type="magic")
inventory.append('water', type="magic")

# inventory.append('grass')
# inventory.append('grass-v')
inventory.append('dirt')
# inventory.append('mud')
# inventory.append('clay')
inventory.append('log')
# inventory.append('wood')
inventory.append('stone')


# inventory.append('coal')
# inventory.append('iron')
# inventory.append('gold')
# inventory.append('diamond')


# inventory.append('sand')
# inventory.append('glass')
# inventory.append('brick')
# inventory.append('stone-brick')


inventory.append('concrete')


boxes = []


def update():

    if held_keys['left mouse']:

        arm.position = (0.6, -0.5)
    elif held_keys['right mouse']:
        arm.position = (0.6, -0.5)
    elif held_keys['escape']:
        inventory.toggleVisible()
    else:
        arm.position = (0.75, -0.6)


for i in range(16):
    for j in range(16):
        boxes.append(blocks.grass((i, 0, j), random.randint(0, 6)))
        boxes.append(blocks.bedrock((i, -1, j)))


def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                box.destroy()
                if box.hardness < 1:
                    boxes.remove(box)
                    destroy(box)

            if key == 'right mouse down':

                boxes.append(blocks.iron(
                    (box.position + mouse.normal)))


app.run()
