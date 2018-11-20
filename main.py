'''
File Created By John Martins for 112 Term Project
AndrewID: johnmart

Credits:
framework created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15

Description: This is the main framework that joins other files and
allows them to interact to make a game

'''

import pygame
import player
import projectile
import enemies
import map
import misc
import math
import random


class PygameGame(object):

    def init(self):
        #Sprite Groups
        self.playerGroup = pygame.sprite.Group()
        self.bulletsGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.obstaclesGroup = pygame.sprite.Group()
        self.wallsGroup = pygame.sprite.Group()
        self.floorGroup = pygame.sprite.Group()


        self.player1 = player.Player(self.width//7, self.height//2)
        self.player1.preDraw()
        self.playerGroup.add(self.player1)
        self.startBoard = map.startBoard
        self.shotAngle = 0
        self.timer = 0
        self.currBoard = map.startBoard
        self.initializeBoard()




    def initializeBoard(self):
        pygame.sprite.Group.empty(self.wallsGroup)
        for i in range(len(self.currBoard)):
            for j in range(len(self.currBoard)):
                width = self.width//len(self.currBoard)
                height = self.height//len(self.currBoard)
                x = j * (width)
                y = i * (height)
                if self.currBoard[i][j] == 2:
                    wallTop = map.WallTop(x,y,width,height)
                    self.wallsGroup.add(wallTop)
                elif self.currBoard[i][j] == 1:
                    wallSide = map.WallSide(x,y,width,height)
                    self.wallsGroup.add(wallSide)
                else:
                    floor = map.Floor(x,y,width,height)
                    self.floorGroup.add(floor)




    def mousePressed(self, x, y):
        if self.player1.rect != None:
            self.shotAngle = misc.getAngle(self.player1.x, self.player1.y, x, y)
            bullet = projectile.Projectile(self.player1.x,self.player1.y,self.shotAngle)
            self.bulletsGroup.add(bullet)


    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass
    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        if keyCode == 119: # W
            self.player1.isRight = False
            self.player1.isLookRight, self.player1.isLookLeft = True, False
        if keyCode == 97: # A
            self.player1.isLeft = False
            self.player1.isLookRight, self.player1.isLookLeft = False, True
        if keyCode == 115: # S
            self.player1.isLeft = False
            self.player1.isLookRight, self.player1.isLookLeft = False, True
        if keyCode == 100: # D
            self.player1.isRight = False
            self.player1.isLookRight, self.player1.isLookLeft = True, False

    def timerFired(self, dt):
        self.timer += 1
        keyCode = pygame.key.get_pressed()
        if keyCode[119]:  # W
            if (self.player1.isLeft, self.player1.isRight) == (False, False):
                self.player1.isRight = True
                #TODO Fix the collision so that player can still move after touching wall
            if not pygame.sprite.groupcollide(self.playerGroup,self.wallsGroup,False,False):
                self.player1.velocity[1] = -self.player1.speed
                self.player1.velocity[0] = 0
                self.playerGroup.update()

        if keyCode[97]:  # A
            self.player1.isLeft, self.player1.isLookLeft = True, True
            if not pygame.sprite.groupcollide(self.playerGroup,self.wallsGroup,False,False):
                self.player1.velocity[0] = -self.player1.speed
                self.player1.velocity[1] = 0
                self.playerGroup.update()

        if keyCode[115]:  # S
            if (self.player1.isLeft, self.player1.isRight) == (False, False):
                self.player1.isLeft = True
            if not pygame.sprite.groupcollide(self.playerGroup,self.wallsGroup,False,False):
                self.player1.velocity[1] = self.player1.speed
                self.player1.velocity[0] = 0
                self.playerGroup.update()
        if keyCode[100]:  # D
            self.player1.isRight, self.player1.isLookRight = True, True
            if not pygame.sprite.groupcollide(self.playerGroup,self.wallsGroup,False,False):
                self.player1.velocity[0] = self.player1.speed
                self.player1.velocity[1] = 0
                self.playerGroup.update()

        for enemy in self.enemyGroup:
            if isinstance(enemy, enemies.Chaser):
                enemy.chase((self.player1.x, self.player1.y))

        self.bulletsGroup.update()
        self.enemyGroup.update()

        if self.timer % 200 == 200:
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            enemy = enemies.Chaser(x,y)
            self.enemyGroup.add(enemy)





    def redrawAll(self, screen):


        pygame.sprite.Group.draw(self.wallsGroup,screen)
        pygame.sprite.Group.draw(self.floorGroup,screen)

        #draws player
        self.player1.preDraw()
        pygame.sprite.Group.draw(self.playerGroup,screen)

        # checks collisions between sprite groups
        if (pygame.sprite.groupcollide(self.bulletsGroup, self.enemyGroup, True, True)):
            print("yeaaaahhhaa")
        pygame.sprite.groupcollide(self.bulletsGroup, self.wallsGroup,True,False)

        #draws bullets
        pygame.sprite.Group.draw(self.bulletsGroup, screen)

        #draws enemies
        pygame.sprite.Group.draw(self.enemyGroup, screen)




    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=800, height=600, fps=50, title="John's TP"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        pygame.init()

    def run(self):
        self.init()
        inGame = True
        inMenu = False
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        while inMenu:
            screen.fill((255,255,255))
            misc.createButton(screen,(100,500,100,50),(255,0,255),(255,0,200))
            pygame.display.update()


        # call game-specific initialization

        while inGame:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                    self.redrawAll(screen)
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    inGame = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()


