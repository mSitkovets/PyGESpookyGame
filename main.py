from PyGE import pyge_application
from Player import Player
from Entity import Entity
from EntityManager import EntityManager
from Enemy import Enemy

xml = open("level.xml").read()

images = {"Player": {"path": "res/player.png", "w": 26, "h": 26},
          "Block": {"path": "res/block.png", "w": 32, "h": 32},
          "enemy0": {"path": "res/ghost.png", "w": 26, "h": 26},
          "enemy1": {"path": "res/zombie.png", "w": 32, "h": 32},
          "enemy2": {"path": "res/spider.png", "w": 32, "h": 32}}

custom_objects = [Player, Entity, EntityManager, Enemy]

pyge_application(
    xml,
    start_room="start",
    images=images,
    custom_objects=custom_objects,
    caption="Python Game",
    fullscreen=False,
    auto_scale=False,
    development_screen_size=(640, 640)
)


