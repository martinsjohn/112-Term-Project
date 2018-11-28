'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: N/A
Description: Defines the Projectiles class containing all attributes of the projectiles
'''
import pygame
import misc
import math
pygame.init()

class Chaser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
        self.attackRadius = 200
        self.health = 0
        self.image = pygame.image.load("pics\chaser.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.imageL = pygame.image.load("pics\chaser.png")
        self.imageR = pygame.transform.flip(self.imageL,True,False)
        self.velocity =[0,0]


    def chase(self,destination):
        sX  = self.rect.center[0]
        sY = self.rect.center[1]
        dX = destination[0]
        dY = destination[1]
        xDiff = dX - sX
        yDiff = dY - sY
        self.angle = misc.getAngle(sX,sY,dX,dY)
        if ((xDiff)**2 + (yDiff)**2)**0.5 <= self.attackRadius:
          self.velocity = [self.speed*math.cos(self.angle),self.speed*-math.sin(self.angle)]
        else:
            self.velocity = [0,0]
    def update(self):
        self.rect.center = (self.rect.center[0] + self.velocity[0], self.rect.center[1] + self.velocity[1])

