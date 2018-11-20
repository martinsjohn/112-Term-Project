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
    elif yDiff == 0 and destX < startY:
        angle = math.pi
    else:
        angle = math.pi / 2 + math.atan(xDiff / -yDiff)
        if destY > startY:
            angle *= -1
        else:
            angle = math.pi - angle
    return angle


def createButton(surface, rect, activeColor, inactiveColor, action = None):

    mousePos = pygame.mouse.get_pos()
    clickPos = pygame.mouse.get_pressed()
    (x,y,width,height) = rect
    if x < mousePos[0] < x + width and y < mousePos[1] < y + height:
        pygame.draw.rect(surface,activeColor,rect)
        if clickPos[0] :
            action()
    else:
        pygame.draw.rect(surface,inactiveColor,rect)

