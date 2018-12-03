'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart
Credits: N/A
Description: Creates empty map templates and contains functions necessary to create
randomized obstacles and enemies
'''



import pygame
import random
pygame.init()

obs1 = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 3, 0],
        [0, 3, 1, 1, 3, 0],
        [0, 3, 3, 1, 3, 0],
        [0, 0, 3, 1, 3, 0],
        [0, 0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

obs2 = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 0, 0],
        [0, 3, 1, 3, 0, 0],
        [0, 3, 1, 3, 3, 0],
        [0, 3, 1, 1, 3, 0],
        [0, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

obs3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 0, 0, 0, 0, 0],
        [0, 0, 3, 1, 3, 3, 3, 0, 0],
        [0, 0, 3, 1, 1, 1, 3, 0, 0],
        [0, 0, 3, 3, 3, 3, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

obs4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 3, 3, 3, 0, 0],
        [0, 0, 3, 1, 1, 1, 3, 0, 0],
        [0, 0, 3, 3, 3, 1, 3, 0, 0],
        [0, 0, 0, 0, 3, 3, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

obs5 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 3, 3, 0, 0, 0],
        [0, 0, 3, 1, 1, 3, 3, 0, 0],
        [0, 0, 3, 3, 1, 1, 3, 0, 0],
        [0, 0, 0, 3, 3, 3, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

obs6 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 3, 3, 3, 0, 0],
        [0, 0, 3, 3, 1, 1, 3, 0, 0],
        [0, 0, 3, 1, 1, 3, 3, 0, 0],
        [0, 0, 3, 3, 3, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

obs7 = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 0, 0],
        [0, 3, 1, 3, 3, 0],
        [0, 3, 1, 1, 3, 0],
        [0, 3, 3, 1, 3, 0],
        [0, 0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

obs8 = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 3, 0],
        [0, 3, 3, 1, 3, 0],
        [0, 3, 1, 1, 3, 0],
        [0, 3, 1, 3, 3, 0],
        [0, 3, 3, 3, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]


obs9 = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 3, 3, 3, 0],
        [0, 3, 1, 3, 0],
        [0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]


obs10 = [[0, 0, 0, 0, 0, 0],
         [0, 3, 3, 3, 3, 0],
         [0, 3, 1, 1, 3, 0],
         [0, 3, 1, 1, 3, 0],
         [0, 3, 3, 3, 3, 0],
         [0, 0, 0, 0, 0, 0]]

obstacles = [obs1, obs2, obs3, obs4, obs5, obs6, obs7, obs8,obs9,obs10]


startBoard =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

mainBoard = [[3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3],
             [3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3],
             [3, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 3, 3],
             [3, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 3, 3],
             [3, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 3, 3],
             [3, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 3, 3],
             [2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2],
             [3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3],
             [3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3],
             [3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3],
             [3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3],
             [3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3],
             [2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2],
             [3, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 3, 3],
             [3, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 3, 3],
             [3, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 3, 3],
             [3, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 3, 3],
             [3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3],
             [3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]]


bossBoard = [[0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]]



def isLegalChange(board, obs, i, j):
    rows = len(obs)
    cols = len(obs[0])
    if (i + rows > len(board)) or (j + cols > len(board)):
        return False
    for row in range(rows):
        for col in range(cols):
            if board[i + row][j + col] != 0 and board[i + row][j + col] != 3:
                return False
    return True

def makeChange(board, obs, i, j):
    rows = len(obs)
    cols = len(obs[0])
    for row in range(rows):
        for col in range(cols):
            board[i + row][j + col] = obs[row][col]

def makeBoard(board, obstacles):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if ((i > 3) or (j > 3)) and ((i < len(board) - 7) or (j < len(board) - 6)):
                obs = random.choice(obstacles)
                if isLegalChange(board, obs, i, j):
                    makeChange(board, obs, i, j)
            if board[i][j] == 0:
                int = random.randint(0,100)
                if int%25 ==0:
                     board[i][j] = 4

    return board



class WallTop(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill((0,100,200))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class WallSide(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

class Floor(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

