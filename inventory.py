from ursina import *
from ursina import collider
from ursina.color import rgba
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random
import time


class InventoryItem(Draggable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_click(self):
        if self.item_type == "item": Inventory.selectedItem = self.name


class Inventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='assets/item-square',
            texture_scale=(8, 8),
            scale=(0.7, 0.7),
            origin=(-.5, .5),
            position=(-.75, .4),
            color=color.color(0, 0, .3, .9),
            visible=False,
            lifeMagic=False,
            selectedItem=None,
            unlocks=[[16, "life","magic"],[25, "concrete","item"], [28, "marble","item"], [32, "basalt","item"],[48, "ruby","item"],[63, "life","item"]],
            inventoryLabel =Text("Inventory", position=(-0.73,.47), background=True, visible=False, font="assets/DTM-Sans.otf"),
            nextUnlockLabel =Text("0 Till Next Unlock:", position=(-0.73,-.34), background=True, visible=False, font="assets/DTM-Sans.otf"),
            itemsUnlockedLabel =Text("10/64", position=(-0.15,-.34), background=True, visible=False, font="assets/DTM-Sans.otf"),
            nextUnlockIcon = Button(
                parent=self,
                model='quad',
                color=color.gray,
                scale_x=1/12,
                scale_y=1/12,
                position=(-0.445,-.35),
                visible = False,
                highlight_color = color.gray
            ),
            
        )
        

        for key, value in kwargs.items():
            setattr(self, key, value)

    def getVisible(self):
        return self.visible

    def toggleVisible(self):
        self.visible = not self.visible
        window.exit_button.visible = self.visible
        mouse.locked = not self.visible
        self.itemsUnlockedLabel.text = str(len(self.children))+"/64"
        self.itemsUnlockedLabel.visible= self.visible
        self.inventoryLabel.visible= self.visible
        self.nextUnlockLabel.visible= self.visible
        self.nextUnlockLabel.text = str(self.unlocks[0][0] - len(self.children))+" Till Next Unlock:"
        self.nextUnlockIcon.visible= self.visible
        self.nextUnlockIcon.texture = texture='assets/items/'+self.unlocks[0][1]
        time.sleep(0.1)

    def find_free_spot(self):
        for y in range(8):
            for x in range(8):
                grid_positions = [(int(e.x*self.texture_scale[0]),
                                   int(e.y*self.texture_scale[1])) for e in self.children]

                if not (x, -y) in grid_positions:
                    return x, y

    def append(self, item, x=0, y=0, type="item", combination="element"):
        
        unique=True
        for i in self.children:
            if i.name == item:
                return

        if len(self.children) >= 8*8:
            error_message = Text('<red>Inventory is full!',
                                 origin=(0, -1.5), x=-.5, scale=2)
            destroy(error_message, delay=1)
            return

        x, y = self.find_free_spot()

        icon = InventoryItem(
            name=item,
            parent=self,
            model='quad',
            texture='assets/items/'+item,
            color=color.white,
            scale_x=1/self.texture_scale[0],
            scale_y=1/self.texture_scale[1],
            origin=(-.5, .5),
            x=x * 1/self.texture_scale[0],
            y=-y * 1/self.texture_scale[1],
            z=-.5,
            item_type = type
        )
        name = item.replace('_', ' ').title()
        if type == "tool":
            icon.tooltip = Tooltip(name+'\n<orange> -> tool', font="assets/DTM-Sans.otf")
        elif type == "magic":
            icon.tooltip = Tooltip(name+'\n<blue> -> magic', font="assets/DTM-Sans.otf")
        else:
            if combination=="element":
                icon.tooltip = Tooltip(name+'\n<green> -> '+combination, font="assets/DTM-Sans.otf")
            else:
                icon.tooltip = Tooltip(name+'\n<gray> -> '+combination, font="assets/DTM-Sans.otf")


        icon.tooltip.background.color = color.color(0, 0, 0, .8)

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01

        def drop():
            icon.x = int((icon.x + (icon.scale_x/2)) * 8) / 8
            icon.y = int((icon.y - (icon.scale_y/2)) * 8) / 8
            icon.z += .01

            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                return

            for c in self.children:
                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    if type == "tool":
                        icon.position = icon.org_pos
                        if icon.name == "chisel":
                            if c.name == "concrete":
                                self.append("concrete-pillar",combination = icon.name+"+"+c.name)
                            if c.name == "sandstone":
                                self.append("sandstone-pillar",combination = icon.name+"+"+c.name)
                            if c.name == "marble":
                                self.append("marble-pillar",combination = icon.name+"+"+c.name)
                            if c.name == "stone":
                                self.append("stone-tiles",combination = icon.name+"+"+c.name)
                            if c.name == "terracotta":
                                self.append("terracotta-tiles",combination = icon.name+"+"+c.name)
                            if c.name == "basalt":
                                self.append("basalt-tiles",combination = icon.name+"+"+c.name)
                        if icon.name == "hammer":
                            if c.name == "stone":
                                self.append("gravel",combination = icon.name+"+"+c.name)
                            if c.name == "sand":
                                self.append("sandstone",combination = icon.name+"+"+c.name)
                        if icon.name == "saw":
                            if c.name == "log":
                                self.append("wood",combination = icon.name+"+"+c.name)
                            if c.name == "stone":
                                self.append("stone-brick",combination = icon.name+"+"+c.name)
                            if c.name == "obsidian":
                                self.append("obsidian-brick",combination = icon.name+"+"+c.name)
                            if c.name == "terracotta":
                                self.append("brick",combination = icon.name+"+"+c.name)
                            if c.name == "concrete":
                                self.append("concrete-brick",combination = icon.name+"+"+c.name)
                            if c.name == "sandstone":
                                self.append("sandstone-brick",combination = icon.name+"+"+c.name)
                            if c.name == "marble":
                                self.append("marble-brick",combination = icon.name+"+"+c.name)
                            if c.name == "basalt":
                                self.append("basalt-brick",combination = icon.name+"+"+c.name)
                            if c.name == "iron":
                                self.append("iron-plating",combination = icon.name+"+"+c.name)
                        if icon.name == "pickaxe":
                            if c.name == "stone":
                                self.append("iron",combination = icon.name+"+"+c.name)
                            if c.name == "basalt":
                                self.append("amber",combination = icon.name+"+"+c.name)
                            if c.name == "clay":
                                self.append("amethyst",combination = icon.name+"+"+c.name)
                            if c.name == "sandstone":
                                self.append("zircon",combination = icon.name+"+"+c.name)
                            if c.name == "marble":
                                self.append("quartz",combination = icon.name+"+"+c.name)
                        
                    elif type == "magic":
                        icon.position = icon.org_pos
                        if icon.name == "fire":
                            # if c.name == "log" or c.name == "wood":
                            #     self.append("ash",combination = icon.name+"+"+c.name)
                            if c.name == "stone":
                                self.append("magma",combination = icon.name+"+"+c.name)
                            if c.name == "sand":
                                self.append("glass",combination = icon.name+"+"+c.name)
                            if c.name == "clay":
                                self.append("terracotta",combination = icon.name+"+"+c.name)
                            if c.name == "mud":
                                self.append("mud-brick",combination = icon.name+"+"+c.name)
                            if c.name == "water":
                                self.append("special", type="magic")
                        if icon.name == "water":
                            if c.name == "dirt":
                                self.append("mud",combination = icon.name+"+"+c.name)
                            if c.name == "sand":
                                self.append("clay",combination = icon.name+"+"+c.name)
                            if c.name == "magma":
                                self.append("obsidian",combination = icon.name+"+"+c.name)
                            if c.name == "fire":
                                self.append("special", type="magic",combination = icon.name+"+"+c.name)
                        if icon.name == "life":
                            if c.name == "dirt":
                                self.append("grass",combination = icon.name+"+"+c.name)
                            if c.name == "log":
                                self.append("leaves",combination = icon.name+"+"+c.name)
                            if c.name == "stone":
                                self.append("mossy-stone",combination = icon.name+"+"+c.name)
                            if c.name == "stone-brick":
                                self.append("mossy-stone-brick",combination = icon.name+"+"+c.name)
                        if icon.name == "special":
                            if c.name == "grass":
                                self.append("meadow",combination = icon.name+"+"+c.name)

                    else:
                        c.position = icon.org_pos
                           

        icon.drag = drag
        icon.drop = drop

        

        if len(self.children) == self.unlocks[0][0]:
            self.append(self.unlocks[0][1], type=self.unlocks[0][2])
            self.unlocks.pop(0)
        
        self.nextUnlockLabel.text = str(self.unlocks[0][0] - len(self.children))+" Till Next Unlock:"
        self.nextUnlockIcon.texture = texture='assets/items/'+self.unlocks[0][1]
        self.itemsUnlockedLabel.text = str(len(self.children))+"/64"
