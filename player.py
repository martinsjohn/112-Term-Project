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

# sets player class with player attributes
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 4
        self.velocity = [0,0]
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


    def hitTop(self,wall):
        if self.rect.y < wall.rect.y + wall.rect.height:
            if self.rect.y + self.rect.height > wall.rect.y + wall.rect.height:
                return True
        return False


    def hitBottom(self,wall):
        pass

    def hitLeft(self,wall):
        pass

    def hitRight(self,wall):
        pass


    def update(self,walls):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        hitWalls = pygame.sprite.spritecollide(self,walls,False)
        for wall in hitWalls:
            # if moving left, make right side of wall the boundary
            if self.velocity[0] < 0 and self.velocity[1] == 0:
                self.x = wall.rect.x + wall.rect.width
            # if moving right, make left side of wall the boundary
            elif self.velocity[0] > 0 and self.velocity[1] == 0:
                self.x = wall.rect.x - self.rect.width

            # if moving up, make bottom of wall the boundary
            elif self.velocity[1] < 0 and self.velocity[0] == 0:
                self.y = wall.rect.y + wall.rect.height

            # if moving down, make top of wall the boundary
            elif self.velocity[1] > 0 and self.velocity[0] == 0:
                self.y = wall.rect.y - self.rect.height

            elif self.velocity[0] > 0 and self.velocity[1] < 0:
                if self.hitTop(wall):
                    print("NNNNN")
                    self.y = wall.rect.y + wall.rect.height
                    self.velocity[1] = -.001



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

        self.rect = self.image.get_rect()
        (self.rect.x, self.rect.y) = (self.x, self.y)
        self.centerX, self.centerY = (self.x + (self.rect.width // 2), self.y + (self.rect.height // 2))




