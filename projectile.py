'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: N/A
Description: Defines the Projectiles class containing all attributes of the projectiles
'''

import pygame
import math
pygame.init()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 10
        self.power = 1
        self.velocity = [self.speed*math.cos(angle),self.speed*-math.sin(angle)]
        self.imageRaw = pygame.image.load("pics\omatoAmmo.png")
        self.image = pygame.transform.scale(self.imageRaw, (15,15))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update (self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

class TomatoBullet(Bullet):
    def __init__(self,x,y,angle):
        super().__init__(x,y,angle)

class Spatula(Bullet):
    def __init__(self,x,y,angle):
        super().__init__(x,y,angle)
        self.speed = 15
        self.power = 3
        self.imageRaw = pygame.image.load("pics\spatulaAmmo.png")
        self.imageR = pygame.transform.scale(self.imageRaw, (10, 40))
        self.image = pygame.transform.rotate(self.imageR, (angle*180/math.pi)-90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class SoupBomb(Bullet):
    def __init__(self,x,y,angle):
        super().__init__(x,y,angle)
        self.speed = 5
        self.power = 5
        self.imageRaw = pygame.image.load("pics\soupAmmo.png")
        self.imageR = pygame.transform.scale(self.imageRaw, (30, 30))
        self.image = pygame.transform.rotate(self.imageR, (angle * 180 / math.pi) - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)






class OnionBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle,originOnion):
        pygame.sprite.Sprite.__init__(self)
        self.origin = originOnion
        self.x = x
        self.y = y
        self.speed = 7
        self.power = .25
        self.velocity = [self.speed*math.cos(angle),self.speed*-math.sin(angle)]
        self.image = pygame.image.load("pics\onionBullet.png")
        self.image = pygame.transform.scale(self.image,(15,15))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update (self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class BossOnionBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 7
        self.power = 1
        self.velocity = [self.speed*math.cos(angle),self.speed*-math.sin(angle)]
        self.image = pygame.image.load("pics\onionBullet.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update (self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]










