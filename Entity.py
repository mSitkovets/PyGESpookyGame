from PyGE.Objects import ObjectBase
from PyGE.DisplayMethods import Image


class Entity(ObjectBase):

    # entities = []

    def oncreate(self):
        self.set_display_method(Image(self.screen, "Block"))
        # Entity.entities.append(self)
        # self.add_object("Player", {}, 200, 200)

    def draw(self):
        self.draw_to_screen()

    def oncollide(self, other):
        other.undo_last_move()
    # pass
