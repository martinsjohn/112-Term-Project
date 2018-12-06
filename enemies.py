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
    def __init__(self,x,y,level):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
        self.attackRadius = 200 + (5*level)
        self.power = 0.05 + (0.01*level/2)
        if level < 15:
            self.health = 1 + level//3
        else:
            self.health = 1 + level//2
        self.image = pygame.image.load("pics\chaser.png")
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = (x, y)
        self.velocity =[0,0]
        self.dirs = [[1, 0], [1, 1], [0, 1], [-1, 0], [-1, -1], [0, -1]]
        self.roamVel = random.choice(self.dirs)
        self.chaseOn = False

    # enemy chases player
    def chase(self,destination,walls):
        sX  = self.rect.x
        sY = self.rect.y
        dX = destination[0]
        dY = destination[1]
        xDiff = dX - sX
        yDiff = dY - sY
        self.angle = misc.getAngle(sX,sY,dX,dY)
        if ((xDiff)**2 + (yDiff)**2)**0.5 <= self.attackRadius:
            self.chaseOn = True
            if pygame.sprite.spritecollide(self,walls,False):
                self.velocity = [-self.speed*math.cos(self.angle),-self.speed*-math.sin(self.angle)]
            else:
                self.velocity = [self.speed*math.cos(self.angle),self.speed*-math.sin(self.angle)]

        else:
            self.chaseOn = False
            self.velocity = self.roamVel

    #moves enemy in x direction and checks to see if it has hit a wall, if so, the movement is reverted
    def moveX(self, walls):
        self.rect.x += self.velocity[0]
        wallHit = pygame.sprite.spritecollide(self, walls, False)
        for wall in wallHit:
            # if moving right, make boundary left side of wall
            if self.velocity[0] > 0:
                self.rect.x = wall.rect.x - self.rect.width
            # if moving left, make boundary right side of wall
            elif self.velocity[0] < 0:
                self.rect.x = wall.rect.x + wall.rect.width

    #moves enemy in y direction and checks to see if it has hit a wall, if so, the movement is reverted
    def moveY(self, walls):
        self.rect.y += self.velocity[1]
        wallHit = pygame.sprite.spritecollide(self, walls, False)
        for wall in wallHit:
            # if moving up =, make boundary bottom of wall
            if self.velocity[1] < 0:
                self.rect.y = wall.rect.y + wall.rect.height
            # if moving down, make boundary top of wall
            elif self.velocity[1] > 0:
                self.rect.y = wall.rect.y - self.rect.height

    def update(self, walls):
        if self.chaseOn:
            self.moveX(walls)
            self.moveY(walls)
        else:
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

    # makes enemies move according to wall collisions
    def switchDir(self):
        self.velocity[0] *= -1
        self.velocity[1] *= -1
        self.roamVel = random.choice(self.dirs)




class Onion(pygame.sprite.Sprite):
    def __init__(self, x, y, level):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 1.5
        self.attackRadius = 200 - (5 * level)
        if self.attackRadius < 50:
            self.attackRadius = 50
        self.power = 0.05 + (0.01 * level / 2)
        if level < 15:
            self.health = 1 + level // 3
        else:
            self.health = 1 + level // 2
        self.imageRaw = pygame.image.load("pics\onion.png")
        self.image = pygame.transform.scale(self.imageRaw, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)
        self.velocity = [0, 0]
        self.bullets = 0
        self.isChase = True

    # enemy chases player
    def chase(self, destination, walls):
        sX = self.rect.x
        sY = self.rect.y
        dX = destination[0]
        dY = destination[1]
        xDiff = dX - sX
        yDiff = dY - sY
        self.angle = misc.getAngle(sX, sY, dX, dY)
        if ((xDiff) ** 2 + (yDiff) ** 2) ** 0.5 >= self.attackRadius:
            self.isChase = True
            if pygame.sprite.spritecollide(self, walls, False):
                self.velocity = [-self.speed * math.cos(self.angle), -self.speed * -math.sin(self.angle)]
            else:
                self.velocity = [self.speed * math.cos(self.angle), self.speed * -math.sin(self.angle)]
        else:
            self.isChase = False
            if pygame.sprite.spritecollide(self, walls, False):
                self.velocity = [self.speed * math.cos(self.angle), self.speed * -math.sin(self.angle)]
            else:
                self.velocity = [-self.speed * math.cos(self.angle), -self.speed * -math.sin(self.angle)]

    # moves enemy in x direction and checks to see if it has hit a wall, if so, the movement is reverted
    def moveX(self, walls):
        self.rect.x += self.velocity[0]
        wallHit = pygame.sprite.spritecollide(self, walls, False)
        for wall in wallHit:
            # if moving right, make boundary left side of wall
            if self.velocity[0] > 0:
                self.rect.x = wall.rect.x - self.rect.width
            # if moving left, make boundary right side of wall
            elif self.velocity[0] < 0:
                self.rect.x = wall.rect.x + wall.rect.width

    # moves enemy in y direction and checks to see if it has hit a wall, if so, the movement is reverted
    def moveY(self, walls):
        self.rect.y += self.velocity[1]
        wallHit = pygame.sprite.spritecollide(self, walls, False)
        for wall in wallHit:
            # if moving up =, make boundary bottom of wall
            if self.velocity[1] < 0:
                self.rect.y = wall.rect.y + wall.rect.height
            # if moving down, make boundary top of wall
            elif self.velocity[1] > 0:
                self.rect.y = wall.rect.y - self.rect.height

    def update(self,walls):
        self.moveX(walls)
        self.moveY(walls)

    def isClose(self,dx,dy):
        diffX = dx - (self.rect.x + self.rect.width//2)
        diffY = dy - (self.rect.y + self.rect.height//2)
        if ((diffX)**2 + (diffY)**2)**0.5 < self.attackRadius:
            return False
        else:
            return True












class OnionBoss(pygame.sprite.Sprite):
    def __init__(self,x,y,level):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 2 + (0.1* level)
        self.power = 0.1 + (0.05* level//2)
        if level < 5:
            self.maxHealth = 15 + 2*level
            self.power = 1
        else:
            self.maxHealth = 20 + level
            self.power = 1 + (level/50)
        self.health = self.maxHealth
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











