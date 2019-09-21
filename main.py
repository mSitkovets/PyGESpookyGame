from PyGE import pyge_application
from Player import Player
xml = open("level.xml").read()
images = {"PyGE": {"path": "PyGE.png", "w": 100, "h": 100}}
custom_objects = [Player]
pyge_application(xml, "start", images=images, custom_objects=custom_objects, caption="Python Game", fullscreen=False, auto_scale=False, development_screen_size=(800, 600))
