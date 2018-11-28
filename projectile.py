'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: N/A
Description: Defines the Projectiles class containing all attributes of the projectiles
'''

import pygame
import math
pygame.init()

class TomatoBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 10
        self.power = 1
        self.velocity = [self.speed*math.cos(angle),self.speed*-math.sin(angle)]
        self.image = pygame.image.load("pics\omato.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update (self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

class OnionBullet(pygame.sprite.Sprite):
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









