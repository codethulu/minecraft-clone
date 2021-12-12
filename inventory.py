from ursina import *
from ursina import collider
from ursina.color import rgba
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random
import time


class Inventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='white_cube',
            texture_scale=(8, 8),
            scale=(.8, .8),
            origin=(-.5, .5),
            position=(-.4, .5),
            color=color.color(0, 0, .1, .9),
            visible=False,
            lifeMagic=False

        )

        for key, value in kwargs.items():
            setattr(self, key, value)

    def getVisible(self):
        return self.visible

    def toggleVisible(self):
        self.visible = not self.visible
        window.exit_button.visible = self.visible
        mouse.locked = not self.visible
        time.sleep(0.1)

    def find_free_spot(self):
        for y in range(8):
            for x in range(8):
                grid_positions = [(int(e.x*self.texture_scale[0]),
                                   int(e.y*self.texture_scale[1])) for e in self.children]

                if not (x, -y) in grid_positions:
                    return x, y

    def append(self, item, x=0, y=0, type="item"):

        if len(self.children) >= 8*8:
            error_message = Text('<red>Inventory is full!',
                                 origin=(0, -1.5), x=-.5, scale=2)
            destroy(error_message, delay=1)
            return

        x, y = self.find_free_spot()

        icon = Draggable(
            name=item,
            parent=self,
            model='quad',
            texture='items/'+item,
            color=color.white,
            scale_x=1/self.texture_scale[0],
            scale_y=1/self.texture_scale[1],
            origin=(-.5, .5),
            x=x * 1/self.texture_scale[0],
            y=-y * 1/self.texture_scale[1],
            z=-.5,
        )
        name = item.replace('_', ' ').title()
        if type == "tool":
            icon.tooltip = Tooltip('<orange>[Tool] ' + name)
        elif type == "magic":
            icon.tooltip = Tooltip('<blue>[Magic] ' + name)
        else:
            icon.tooltip = Tooltip(name)

        # if random.random() < .25:
        #     icon.color = color.gold
        #     name = '<orange>[Tool] ' + name

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

                    c.position = icon.org_pos
                    if type == "tool":
                        if icon.name == "chisel":
                            if c.name == "concrete":
                                self.append("concrete-pillar")
                            if c.name == "stone":
                                self.append("stone-tiles")
                            if c.name == "terracotta":
                                self.append("terracotta-tiles")
                        if icon.name == "hammer":
                            if c.name == "stone":
                                self.append("sand")
                        if icon.name == "saw":
                            if c.name == "log":
                                self.append("wood")
                            if c.name == "stone":
                                self.append("stone-brick")
                            if c.name == "terracotta":
                                self.append("brick")
                            if c.name == "concrete":
                                self.append("concrete-brick")
                    if type == "magic":
                        if icon.name == "fire":
                            if c.name == "log" or c.name == "wood":
                                self.append("ash")
                            if c.name == "sand":
                                self.append("glass")
                            if c.name == "clay":
                                self.append("terracotta")
                            if c.name == "water":
                                self.append("special", type="magic")
                        if icon.name == "water":
                            if c.name == "dirt":
                                self.append("mud")
                            if c.name == "sand":
                                self.append("clay")
                            if c.name == "fire":
                                self.append("special", type="magic")
                        if icon.name == "life":
                            if c.name == "dirt":
                                self.append("grass")

        icon.drag = drag
        icon.drop = drop
        if len(self.children) > 16 and self.lifeMagic == False:
            self.lifeMagic = True
            self.append("life", type="magic")
