from PyGE.Objects import ObjectBase
from PyGE.DisplayMethods import Image
class Player(Entity):
    def oncreate(self):
        self.set_display_method(Image(self.screen, "PyGE"))
    def draw(self):
        self.draw_to_screen()
    def update(self, pressed_keys):
        if pressed_keys[276]:
            self.time_move(-100, 0)
        if pressed_keys[275]:
            self.time_move(100, 0)
        if pressed_keys[273]:
            self.time_move(0, 100)
        if pressed_keys[274]:
            self.time_move(0, -100)
