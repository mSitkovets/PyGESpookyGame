import pygame
from PyGE.Objects import ObjectBase
from PyGE.DisplayMethods import Image
from PyGE.Misc.AlarmClock import AlarmClock

class Maze(ObjectBase):
    
    def oncreate(self):
        self.set_display_method(Image(self.screen, "block"))
    def draw(self):
        self.draw_to_screen()
    def oncollide(self, obj:'ObjectBase'):
        if obj.object_type == "Person":
            obj.undo_last_move()  
            
            
        
    
