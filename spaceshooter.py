"""
spaceshooter.py
Author: Eli Woloshin
Credit: none

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos

class Stars(Sprite):
    
    asset = ImageAsset("images/starfield.jpg")
    width = 4000
    height = 4000
    
    def __init__(self, position):
        super().__init__(Stars.asset, position)

class Sun1(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun1.asset, position)
        self.fxcenter = self.fycenter = 0.5

class Sun2(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun2.asset, position)
        self.fxcenter = self.fycenter = 0.5

class Sun3(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun3.asset, position)
        self.fxcenter = self.fycenter = 0.5



class Ship(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertrov_with_thrust.png",
        Frame(277,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.asset, position)
        self.fxcenter = self.fycenter = 0.5
        SpaceGame.listenKeyEvent('keydown', 'right arrow', self.rotateRight)
        SpaceGame.listenKeyEvent('keydown', 'left arrow', self.rotateLeft)
        SpaceGame.listenKeyEvent('keydown', 'up arrow', self.moveUp)
        SpaceGame.listenKeyEvent('keydown', 'down arrow', self.moveDown)
        SpaceGame.listenKeyEvent('keyup', 'up arrow', self.thrustoff)
        SpaceGame.listenKeyEvent('keyup', 'down arrow', self.thrustoff)
        SpaceGame.listenKeyEvent('keydown', 'space', self.fire)
        self.thrust = 0
        self.thrustframe = 0
    def rotateRight(self, event):
        self.rotation -= 0.1
    def rotateLeft(self, event):
        self.rotation += 0.1
    def moveUp(self, event):
        self.x += -5*sin(self.rotation)
        self.y += -5*cos(self.rotation)
        self.thrust = 1
    def moveDown(self, event):
        self.x += 7*sin(self.rotation)
        self.y += 7*cos(self.rotation)
        self.thrust = 1
    def thrustoff(self, event):
        self.thrust = 0
    def fire(self, event):
        Bullet((self.x,self.y))

    def step(self):
        if len(self.collidingWithSprites(Sun)) > 0:
            self.destroy()
        if self.thurst == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thurstframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

class Bullet(Sprite):
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
    def __init__(self, position):
        super().__init__(Bullet.asset, position)


class SpaceGame(App):
    def __init__(self):
        super().__init__()
        Stars((0,0))
        Sun1((256,256))
        Sun2((400, 400))
        Sun3((100, 100))
        Ship((100,100))

    def step(self):
        for x in self.getSpritesbyClass(Ship):
            x.step()

    
SpaceGame().run()



    

















'''
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math



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
        super().__init__(ship1.asset, app, position, velocity, sun)
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        self.VX = 0
        self.VY = 0   
        self.vx = 0
        self.vy = 0
        self.turn = 0
        self.fxcenter = self.fycenter = 0.5
        self.bullet = None
    def rotateRight(self, event):
        self.rotation -= 0.1
    def rotateLeft(self, event):
        self.rotation += 0.1
    def moveUp(self, event):
        self.x += -5*sin(self.rotation)
        self.y += -5*cos(self.rotation)
        self.thrust = 1
    def moveDown(self, event):
        self.x += 5*sin(self.rotation)
        self.y += 5*cos(self.rotation)
        self.thrust = 1
    def thrustoff(self, event):
        self.thrust = 0
    def fire(self, event):
        Bullet((self.x,self.y))
    def __init__(self, position):
        super().__init__(Ship.asset, position)
        self.fxcenter = self.fycenter = 0.5
        SpaceGame.listenKeyEvent('keydown', 'right arrow', self.rotateRight)
        SpaceGame.listenKeyEvent('keydown', 'left arrow', self.rotateLeft)
        SpaceGame.listenKeyEvent('keydown', 'up arrow', self.moveUp)
        SpaceGame.listenKeyEvent('keydown', 'down arrow', self.moveDown)
        SpaceGame.listenKeyEvent('keyup', 'up arrow', self.thrustoff)
        SpaceGame.listenKeyEvent('keyup', 'down arrow', self.thrustoff)
        SpaceGame.listenKeyEvent('keydown', 'space', self.fire)
        self.thrust = 0
        self.thrustframe = 0

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
        self.sun = Sun((200, 150))
        Ship1(self, (100, 100), (0,0), self.sun)

class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = self.fycenter = 0.5


myapp = SpaceGame(0,0)
myapp.run()
'''
'''
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos

class Ship(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.asset, position)
        self.fxcenter = self.fycenter = 0.5
        SpaceGame.listenKeyEvent('keydown', 'right arrow', self.rotateRight)
        SpaceGame.listenKeyEvent('keydown', 'left arrow', self.rotateLeft)
        SpaceGame.listenKeyEvent('keydown', 'up arrow', self.moveUp)
        SpaceGame.listenKeyEvent('keydown', 'down arrow', self.moveDown)
        SpaceGame.listenKeyEvent('keyup', 'up arrow', self.thrustoff)
        SpaceGame.listenKeyEvent('keyup', 'down arrow', self.thrustoff)
        SpaceGame.listenKeyEvent('keydown', 'space', self.fire)
        self.thrust = 0
        self.thrustframe = 0
    def rotateRight(self, event):
        self.rotation -= 0.1
    def rotateLeft(self, event):
        self.rotation += 0.1
    def moveUp(self, event):
        self.x += -5*sin(self.rotation)
        self.y += -5*cos(self.rotation)
        self.thrust = 1
    def moveDown(self, event):
        self.x += 5*sin(self.rotation)
        self.y += 5*cos(self.rotation)
        self.thrust = 1
    def thrustoff(self, event):
        self.thrust = 0
    def fire(self, event):
        Bullet((self.x,self.y))
        
    def step(self):
        if len(self.collidingWithSprites(Sun)) > 0:
            self.destroy()
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

        
class Bullet(Sprite):
     asset = ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
     def __init__(self, position):
         super().__init__(Bullet.asset, position)
         
     
    
class SpaceGame(App):
    
    def __init__(self):
        super().__init__()
        Stars((0,0))
        Sun((256,256))
        Ship((100,100))
        
    def step(self):
        for x in self.getSpritesbyClass(Ship):
            x.step()
        

        
        
        
        
    
SpaceGame().run()
'''


