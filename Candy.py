from PyGE.Objects import ObjectBase
from PyGE.DisplayMethods import Image
import random

class Candy(ObjectBase):
    def oncreate(self):
        random_int = random.randint(1,101)
        if 25 < random_int <= 50:
            self.set_display_method(Image(self.screen, "candy2"))
        elif random_int <= 25:
            self.set_display_method(Image(self.screen, "candy3"))
        else:
            self.set_display_method(Image(self.screen, "candy1"))
    def draw(self):
        self.draw_to_screen()
    def oncollide(self, obj:'ObjectBase'):
        if obj.object_type == "Player":
            self.delete(self)
        

