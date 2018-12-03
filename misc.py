'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: Button ideas and Text methods derived from YouTube user 'sentdex' in
videos "Game Development in Python3 With Pygame - 5, 11, 13, 15"
link to Playlist containing his videos :
https://www.youtube.com/playlist?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO

Description: This file house miscellaneous items used primarily in menu screens
such as buttons, button functions, text, etc...
'''


import pygame
import math
pygame.init()



def getAngle(startX,startY,destX,destY):
    xDiff = destX - (startX)
    yDiff = destY - (startY)

    if xDiff == 0 and destY < startY:
        angle = math.pi / 2
    elif xDiff == 0 and destY > startY:
        angle = 3 * math.pi / 2
    elif yDiff == 0 and destX > startX:
        angle = 0
    elif yDiff == 0 and destX < startX:
        angle = math.pi
    elif yDiff == 0 and xDiff == 0:
        angle = 0
    else:
        angle = math.pi / 2 + math.atan(xDiff / -yDiff)
        if destY > startY:
            angle *= -1
        else:
            angle = math.pi - angle
    return angle

def inRect(checkP,rectP):

    if rectP[0] < checkP[0] < rectP[2] and rectP[1] < checkP[1] < rectP[3]:
        return True
    return False


class Button(object):
    def __init__(self,rect,text):
        self.rect = rect
        self.left = rect[0]
        self.right = rect[0] + rect[2]
        self.top = rect[1]
        self.bottom = rect[1] + rect[3]
        self.textSize = 275//len(text)
        self.activeColor = (255,200,0)
        self.inactiveColor = (255,0,0)
        self.color = self.inactiveColor
        self.font = pygame.font.Font('font\coolFont.ttf', self.textSize)
        self.text = self.font.render(str(text), True, (0,0,0))
        self.textRect = self.text.get_rect(center =(self.left + rect[2]//2, self.top + rect[3]//2))

    def mouseCheck(self,mouseX,mouseY):
        if (self.left < mouseX < self.right) and (self.top < mouseY < self.bottom):
            self.color = self.activeColor
        else:
            self.color = self.inactiveColor

    def clickCheck(self,clickX,clickY):
        if (self.left < clickX < self.right) and (self.top < clickY < self.bottom):
            return True


    def draw(self,surface):
        pygame.draw.rect(surface,self.color, self.rect)
        surface.blit(self.text,self.textRect)


class Text(object):
    def __init__(self, rect, text, color):
        self.rect = rect
        self.textSize = 3*rect[2] // len(text)
        self.font = pygame.font.Font('font\coolFont.ttf', self.textSize)
        self.text = self.font.render(str(text), True, color )
        self.textRect = self.text.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))

    def draw(self,surface):
        surface.blit(self.text,self.textRect)


class Portal(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.imageRaw = pygame.image.load("pics\ladder2.png")
        self.image = pygame.transform.scale(self.imageRaw,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)








class PowerUp(pygame.sprite.Sprite):
    def __init__(self,x,y,image = None):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center =(x,y)

class CircleShot(PowerUp):
    def __init__(self,x,y,image = pygame.image.load("pics\circleShot.png")):
        super().__init__(x,y,image)
        self.image = pygame.transform.scale(image,(50,50))

class Invincibility(PowerUp):
    def __init__(self,x,y,image = pygame.image.load("pics\invincibility.png")):
        super().__init__(x,y,image)
        self.image = pygame.transform.scale(image,(50,50))


class Speed(PowerUp):
    def __init__(self,x,y,image = pygame.image.load("pics\speed.png")):
        super().__init__(x,y,image)
        self.image = pygame.transform.scale(image,(50,50))


class Strength(PowerUp):
    def __init__(self,x,y,image = pygame.image.load("pics\strength.png")):
        super().__init__(x,y,image)
        self.image = pygame.transform.scale(image,(50,50))


class Health(PowerUp):
    def __init__(self,x,y,image = pygame.image.load("pics\health.png")):
        super().__init__(x,y,image)
        self.image = pygame.transform.scale(image,(50,50))




