'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: N/A
Description: Defines the Projectiles class containing all attributes of the projectiles
'''
import pygame
import misc
import math
import random
pygame.init()



class Chaser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
        self.attackRadius = 200
        self.power = 0.1
        self.health = 2
        self.image = pygame.image.load("pics\chaser.png")
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = (x, y)
        self.velocity =[0,0]
        self.dirs = [[1, 0], [1, 1], [0, 1], [-1, 0], [-1, -1], [0, -1]]
        self.roamVel = random.choice(self.dirs)

    def chase(self,destination):
        sX  = self.rect.x
        sY = self.rect.y
        dX = destination[0]
        dY = destination[1]
        xDiff = dX - sX
        yDiff = dY - sY
        self.angle = misc.getAngle(sX,sY,dX,dY)
        if ((xDiff)**2 + (yDiff)**2)**0.5 <= self.attackRadius:
            self.velocity = [self.speed*math.cos(self.angle),self.speed*-math.sin(self.angle)]

        else:
            self.velocity = self.roamVel

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def switchDir(self):
        self.roamVel[0], self.roamVel[1] = -self.roamVel[0], -self.roamVel[1]




class OnionBoss(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 2
        self.power = 1
        self.health = 2
        self.image = pygame.image.load("pics\evilOnionBoss.png")
        self.image = pygame.transform.scale(self.image,(150,100))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = (x, y)
        self.dirs = [[self.speed, 0], [self.speed, self.speed], [0, self.speed]\
                     ,[-self.speed, 0], [-self.speed, -self.speed], [0, -self.speed]]
        self.roamVel = random.choice(self.dirs)

    def update(self):
        self.rect.x += self.roamVel[0]
        self.rect.y += self.roamVel[1]

    def switchDir(self):
        self.rect.x -= self.roamVel[0]
        self.rect.y -= self.roamVel[1]
        self.roamVel = random.choice(self.dirs)

    def shoot(self,destination):
        sX = self.rect.x + self.rect.width//2
        sY = self.rect.y + self.rect.height//2
        dX = destination[0]
        dY = destination[1]
        xDiff = dX - sX
        yDiff = dY - sY
        self.angle = misc.getAngle(sX, sY, dX, dY)







