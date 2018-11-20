'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: N/A
Description: Creates empty map templates and contains functions necessary to create
randomized obstacles and enemies
'''



import pygame
pygame.init()

def makeStartBoard(n):
    startBoard = []
    startBoard.append([0]*n)
    startBoard.append([0]+[2]*(n-5)+[0]*4)
    startBoard.append([0] + [2] + [1]*(n-7) + [2] + [0]*4)
    for i in range(n-17):
        startBoard.append([0] + [2] + [0]*(n-7) + [2] + [0]*4)
    startBoard.append([0] + [2] + [0]*(n-7) + [2]*5)
    startBoard.append([0] + [2] + [0]*(n-7) + [1]*5)
    for i in range(4):
        startBoard.append([0] + [2] + [0]*(n-2))
    startBoard.append([0] + [2] + [0]*(n-7) + [2]*5)
    startBoard.append([0] + [2] + [0]*(n-7) + [2] + [1]*4)
    for i in range(n-17):
        startBoard.append([0] + [2] + [0]*(n-7) + [2] + [0]*4)
    startBoard.append([0] + [2]*(n-5) + [0]*4)
    startBoard.append([0] + [1]*(n-5) + [0]*4)
    return startBoard



startBoard =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
             [0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]

class WallTop(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill((255,200,0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class WallSide(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

class Floor(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill((139,69,19))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

