from PyGE.Objects import ObjectBase
from PyGE.DisplayMethods import Image
import random


class Enemy(ObjectBase):

	r = random.randint(0, 2)
	# str = "enemy{0}".format(r)
	# str += str(r)

	x_vel = random.randint(100, 200)
	y_vel = random.randint(100, 200)

	def oncreate(self):
		# if(r == 0):
		# 	self.set_display_method(Image(self.screen, "enemy1"))
		self.set_display_method(Image(self.screen, "enemy0"))
		# Entity.entities.append(self)
		# self.add_object("Player", {}, 200, 200)

	def draw(self):
		self.draw_to_screen()

	def update(self, k):
		self.time_move(self.x_vel, self.y_vel)
		if self.x_vel == 0 and self.y_vel == 0:
			self.change_speed()

	def oncollide(self, other):
		if other.object_type == "Entity":
			self.change_speed()

	def change_speed(self):
		self.x_vel = random.randint(100, 300) * random.randint(-1, 1)
		self.y_vel = random.randint(100, 300) * random.randint(-1, 1)

# def time_move(self):


	# def oncollide(self, other):