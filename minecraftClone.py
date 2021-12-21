from ursina import *
from ursina import shader
from ursina import texture
from ursina import text
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random
import blocks
import inventory
import itemblockconverter
from ursina.shaders import basic_lighting_shader
from ursina.shaders import colored_lights_shader
import time

app = Ursina()
inventory = inventory.Inventory()
Sky()
scene.fog_density=.01
scene.fog_color = color.rgb(50,50,50)
player = FirstPersonController()
player.gravity= 0.7
player.jump_height=1.3
player.jump_duration=.3
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = False


# DirectionalLight(parent=pivot, x=2, y=30, z=3, shadows=True)
# window.fullscreen = True
selecteditem = "stone"
selected = Entity(
    parent=camera.ui,
    model='cube',
    color=color.white,
    position=(0.5, -0.2),
    rotation=(170, -10, 6),
    scale=(0.3, 0.3, 0.3),
    shader=basic_lighting_shader,
    texture="assets/blocks/" + selecteditem

)
arm = Entity(
    parent=camera.ui,
    model='cube',
    color=color.white,
    position=(0.3, -0.6),
    rotation=(150, -10, 6),
    scale=(0.2, 0.2, 1.5),
    texture="assets/arm",
        
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
inventory.append('sand')


# inventory.append('coal')
# inventory.append('iron')
# inventory.append('gold')
# inventory.append('diamond')





boxes = []


def update():
    hovered_block = None
    for block in boxes:
        block.update()
        if block.hovered:
            hovered_block=block
            
    if held_keys[ 'left shift']:
        player.speed = 9
    else:
        player.speed = 5
    
    if not inventory.visible:
        if held_keys['left mouse']:
            selected.position = (0.4, -0.1)
            arm.position = (0.6, -0.5)
            if hovered_block!=None:
                hovered_block.destroy()
                if hovered_block.hardness < 1:
                    boxes.remove(hovered_block)
                    destroy(hovered_block)
                    time.sleep(0.1)
            


        elif held_keys['right mouse']:
            selected.position = (0.4, -0.1)
            arm.position = (0.6, -0.5)
            if hovered_block!=None:
                boxes.append(itemblockconverter.convert(
                        selecteditem, (hovered_block.position + mouse.normal)))
                time.sleep(0.1)

    if held_keys['escape']:
        inventory.toggleVisible()

        if selecteditem == None:
            selected.visible = False
        else:
            selected.texture = "assets/blocks/" + selecteditem
            selected.visible = not inventory.visible

    else:
        selected.position = (0.5, -0.2)
        arm.position = (0.75, -0.6)


for i in range(16):
    for j in range(16):
        boxes.append(blocks.grass((i, 0, j), random.randint(0, 6)))
        boxes.append(blocks.bedrock((i, -1, j)))


def input(key):
    if key == 'left mouse down':
        if inventory.visible:
            for item in inventory.children:
                if item.hovered:
                    global selecteditem
                    selecteditem = item.name
  
            # for box in boxes:
            #     if box.hovered:
            #         box.destroy()
            #         if box.hardness < 1:
            #             boxes.remove(box)
            #             destroy(box)

    # if key == 'right mouse down':
    #     for box in boxes:
    #         if box.hovered:
    #             boxes.append(itemblockconverter.convert(
    #                 selecteditem, (box.position + mouse.normal)))
                # boxes.append(blocks.iron(
                #     (box.position + mouse.normal)))
    


app.run()
