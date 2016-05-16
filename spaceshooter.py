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
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
    def registerKeys(self, keys):
        commands = ["left", "right", "forward", "fire"]
        self.keymap = dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]
    def controldown(self, event):
        if self.visible:
            command = self.keymap[event.key]
            if command == "left":
                self.rrate = Ship.R
            elif command == "right":
                self.rrate = -Ship.R
            elif command == "forward":
                self.thrust = 40.0
                self.imagex = 1 # start the animated rockets
                self.setImage(self.imagex)
    def controlup(self, event):
        command = self.keymap[event.key]
        if command in ["left", "right"]:
            self.rrate = 0.0
        elif command == "forward":
            self.thrust = 0.0
            self.imagex = 0 # stop the animated rockets
            self.setImage(self.imagex)
    def explode(self):
        self.visible = False
        ExplosionBig(self.position)
        self.waitspawn = 5
class Ship1(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
        
    def __init__(self, app, position, velocity, sun):
        super().__init__(Ship1.asset, app, position, velocity, sun)
        self.registerKeys(["a", "d", "w", "space"])
        
    def step(self, T, dT):
        super().step(T, dT)
        if self.visible:
            collides = self.collidingWithSprites(Sun)
            if len(collides):
                if collides[0].visible:
                    collides[0].explode()
                    self.explode()



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



