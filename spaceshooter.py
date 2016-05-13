"""
spaceshooter.py
Author: Eli Woloshin
Credit: none

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')
    def__init__(self, position):
        super().__init__(SpaceShip.asset, position)


class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        asset = ImageAsset("images/sun.png")
        Sun((200, 150))
        SpaceShip((100, 100))

class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.mass = 30*1000
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()






myapp = SpaceGame(0,0)
myapp.run()



