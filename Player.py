from PyGE.Objects import ObjectBase
from PyGE.DisplayMethods import Image
from Entity import Entity

class Player(ObjectBase):
    p_velocity = 200
    DEFAULT_VELOCITY = 200
    playerScore = 0
    health = 3

    def oncreate(self):
        self.set_display_method(Image(self.screen, "Player"))

    def draw(self):
        self.draw_to_screen()

    # def collision_detection(self, objects: List[ForwardRef('ObjectBase')]):
    #     return super().collision_detection(objects)

    def update(self, pressed_keys):
        if pressed_keys[276]:
            self.time_move(-self.p_velocity, 0)
        if pressed_keys[275]:
            self.time_move(self.p_velocity, 0)
        if pressed_keys[273]:
            self.time_move(0, self.p_velocity)
        if pressed_keys[274]:
            self.time_move(0, -self.p_velocity)

        self.p_velocity = self.DEFAULT_VELOCITY

        # self.collision_detection(self, Entity.entities)

    def oncollide(self, other: 'ObjectBase'):
        if other.object_type == "Enemy":
            self.take_damage()
            other.delete(other)
        if other.object_type == "Candy":
            self.gain_candy()

    def gain_candy(self):
        self.score += 1

    def take_damage(self):
        self.health -= 1
        # self.draw_to_screen(self, 200, 200)
        if self.health <= 0:
            self.lose_game()

    def lose_game(self):
        self.delete(self)



