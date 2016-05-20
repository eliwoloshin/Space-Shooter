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
    def __init__(self, app, position, velocity, sun): # Ship1.asset, app, position, velocity, sun
        super().__init__(SpaceShip.asset, position)
        self.app = app
        self.velocity = velocity
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
    def step(self, T, dT):
        self.x = self.x+1
    def move(self):
        self.X = math.sin(self.rotation)
        self.Y = math.cos(self.rotation)
        self.vx = self.X/math.sqrt(self.X*self.X + self.Y*self.Y)
        self.vy = self.Y/math.sqrt(self.X*self.X + self.Y*self.Y)

class Ship1(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, app, position, velocity, sun):
        super().__init__(Ship1.asset, position)
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        self.VX = 0
        self.VY = 0   
        self.vx = 0
        self.vy = 0
        self.turn = 0
        SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "a", self.rotateLeft)
        SpaceGame.listenKeyEvent("keyup", "a", self.lrOff)
        SpaceGame.listenKeyEvent("keydown", "d", self.rotateRight)
        SpaceGame.listenKeyEvent("keyup", "d", self.rrOff)
        SpaceGame.listenKeyEvent("keypress", "e", self.fire)
        self.fxcenter = self.fycenter = 0.5
        self.bullet = None

    def step(self, T, dT):
        super().step(T, dT)
        if self.visible:
            collides = self.collidingWithSprites(Sun)
            if len(collides):
                if collides[0].visible:
                    collides[0].explode()
                    self.explode()





class ExplosionSmall(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)

    def __init__(self, position):
        super().__init__(ExplosionSmall.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)

    def step(self):
        self.setImage(self.image//2)  # slow it down
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()

class ExplosionBig(Sprite):
    
    asset = ImageAsset("images/explosion2.png", Frame(0,0,4800/25,195), 25)

    def __init__(self, position):
        super().__init__(ExplosionBig.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)

    def step(self):
        self.setImage(self.image//2)  # slow it down
        self.image = self.image + 1
        if self.image == 50:
            self.destroy()


class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        asset = ImageAsset("images/sun.png")
        sun = Sun((200, 150))
        Ship1(self, (100, 100), (0,0), sun)

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



