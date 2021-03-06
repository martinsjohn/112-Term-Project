'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: (line 30 of this file)
Image of Chef Kawaski character borrowed from Kirby Super Star and taken
from this website:
http://animegames.wikia.com/wiki/File:Chef_Kawasaki_(Kirby_Super_Star_-_Sprite_Sheets_-_Hitbox).png
Update method on line 46 inspired by Professor Craven's Youtube video "Chapter 14: Sprite Walls"
link: https://youtu.be/8IRyt7ft7zg
Description: Defines the Player class containing all attributes of the player
'''



import pygame
import playerImages   #stores information for player images and animation
import misc
import copy


# sets player class with player attributes
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 3
        self.baseSpeed = 3
        self.power = 1
        self.basePower = 1
        self.velocity = [0,0]
        self.currVelocity = None
        self.isLookLeft = False
        self.isLeft = False
        self.isLookRight = True
        self.isRight = False
        self.walkCount = 0  # increments to determine player animation picture
        self.image ='pics\chefK.png'
        self.getPics(self.image)


        #variable attributes
        self.maxHealth = 10
        self.currHealth = 10

    def getPics(self,image):
        frameWidth = 55
        frameHeight = 65
        cols = 5
        rows = 1
        self.pics = playerImages.getFrames(pygame.image.load(image), (0, 0), (frameWidth, frameHeight), cols, rows)
        self.picsRev = playerImages.getRevFrames(self.pics)
        self.standingR = self.pics[0]
        self.standingL = self.picsRev[0]
        self.walkingR = [self.pics[1], self.pics[2], self.pics[3], self.pics[4]]
        self.walkingL = [self.picsRev[1], self.picsRev[2], self.picsRev[3], self.picsRev[4]]

    #moves player in x direction and checks to see if it has hit a wall, if so, the movement is reverted
    def moveX(self,walls):
        self.x += self.velocity[0]
        self.rect.x = self.x
        wallHit = pygame.sprite.spritecollide(self,walls,False)
        for wall in wallHit:
            #if moving right, make boundary left side of wall
            if self.velocity[0] > 0:
                self.x = wall.rect.x - self.rect.width
                self.rect.x = self.x
            #if moving left, make boundary right side of wall
            elif self.velocity[0] < 0:
                self.x = wall.rect.x + wall.rect.width
                self.rect.x = self.x

    #moves player in y direction and checks to see if it has hit a wall, if so, the movement is reverted
    def moveY(self,walls):
        self.y += self.velocity[1]
        self.rect.y = self.y
        wallHit = pygame.sprite.spritecollide(self,walls,False)
        for wall in wallHit:


            # if moving up =, make boundary bottom of wall
            if self.velocity[1] < 0:
                self.y = wall.rect.y + wall.rect.height
                self.rect.y = self.y
            # if moving down, make boundary top of wall
            elif self.velocity[1] > 0:
                self.y = wall.rect.y - self.rect.height
                self.rect.y = self.y


    def update(self,walls):
        self.preDraw()
        self.moveX(walls)
        self.moveY(walls)

    # takes walkcount and determines animation image/rect from it
    def preDraw(self):
        self.walkCount += 1
        if self.walkCount >= 20:
            self.walkCount = 0

        if self.isLeft:
            self.image = self.walkingL[self.walkCount // 5]
        elif self.isRight:
            self.image = self.walkingR[self.walkCount // 5]
        elif self.isLookLeft:
            self.image = self.standingL
        elif self.isLookRight:
            self.image = self.standingR
        # sets up rect crop to insure better player movement
        self.rectRaw = self.image.get_rect()
        x = self.rectRaw.x
        y = self.rectRaw.y
        wid = self.rectRaw.width
        hei = self.rectRaw.height
        self.rect = self.rectRaw.clip(x,y,wid-29,hei-20)
        (self.rect.x, self.rect.y) = (self.x, self.y)
        self.centerX, self.centerY = (self.x + (self.rect.width // 2), self.y + (self.rect.height // 2))

    def draw(self,surface):
        x = self.rect.x - 14
        y = self.rect.y - 10
        wid = self.rect.width
        hei = self.rect.height
        surface.blit(self.image,(x,y,wid,hei))






