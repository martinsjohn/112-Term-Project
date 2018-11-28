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
import copy
import random


class PygameGame(object):

    def init(self):
        #Modes
        self.isMenu = True
        self.isPaused = False
        self.isInstr = False

        #Sprite Groups
        self.playerGroup = pygame.sprite.Group()
        self.bulletsGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.obstaclesGroup = pygame.sprite.Group()
        self.wallsGroup = pygame.sprite.Group()
        self.floorGroup = pygame.sprite.Group()

        # Initializations for menu screen
        self.startBut = misc.Button((self.width//2 - 75, 4*self.height//7,150,75),"Start!")
        self.quitBut = misc.Button((self.width//2 - 75, 5*self.height//7,150,75),"Quit!")
        self.instrBut = misc.Button((self.width//2 - 75, 6*self.height//7,150,75),"Instructions")
        self.menuBackground = pygame.image.load('pics\menuBackground.png')
        self.menuBackground = pygame.transform.scale(self.menuBackground, (self.width,self.height))
        self.menuBackRect = self.menuBackground.get_rect()

        # Initializations for the player and enemies
        self.player1 = player.Player(self.width//2, self.height//2)
        self.player1.preDraw()
        self.playerGroup.add(self.player1)
        self.shotAngle = 0
        self.timer = 0

        # Initializations for the map
        self.boardList = [map.startBoard]
        self.room = 0
        self.currBoard = self.boardList[self.room]
        self.initializeBoard()

        # Initializations for game data
        self.font = pygame.font.Font('font\coolFont.ttf', 30)
        self.level = 1

        self.p1HealthImage = pygame.image.load("pics\health.png")
        self.p1HealthImage = pygame.transform.scale(self.p1HealthImage, (60, 60))
        self.p1HealthImageRect = self.p1HealthImage.get_rect(center=(self.width - 40, 150))

        self.p1TomsImage = pygame.image.load("pics\omatoAmmo.png")
        self.p1TomsImage = pygame.transform.scale(self.p1TomsImage, (50, 50))
        self.p1TomsImageRect = self.p1TomsImage.get_rect(center=(self.width - 40, self.height - 120))

        self.p1Toms = pygame.image.load("pics\infinity.png")
        self.p1Toms = pygame.transform.scale(self.p1Toms, (36,36))
        self.p1TomsRect = self.p1Toms.get_rect(center=(self.width-40, self.height - 120))



    def initializeBoard(self):
        self.wallsGroup.empty()
        self.floorGroup.empty()
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




    def startGame(self):
        self.isMenu = False
        self.isPaused = False
        self.isInstr = False

    def instrScreen(self):
        self.isMenu = False
        self.isPaused = False
        self.isInstr = True

    def menuScreen(self):
        self.isMenu = True
        self.isPaused = False
        self.isInstr = False

    def pauseScreen(self):
        self.isMenu = False
        self.isPaused = True
        self.isInstr = False



    def mousePressed(self, x, y,):
        if self.isMenu:
            if self.startBut.clickCheck(x,y):
                self.startGame()

            elif self.quitBut.clickCheck(x,y):
                pygame.quit()

            elif self.instrBut.clickCheck(x,y):
                self.instrScreen()

        elif self.isPaused:
            pass

        elif self.isInstr:
            pass
        # TODO Create Instruction Screen and Pause Screen for MVP

        else:
            self.shotAngle = misc.getAngle(self.player1.centerX, self.player1.centerY, x, y)
            bullet = projectile.Projectile(self.player1.centerX,self.player1.centerY,self.shotAngle)
            self.bulletsGroup.add(bullet)



    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        if self.isMenu:
            self.startBut.mouseCheck(x,y)
            self.quitBut.mouseCheck(x,y)
            self.instrBut.mouseCheck(x,y)

        elif self.isPaused:
            pass

        elif self.isInstr:
            pass
        else:

            pass
    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if self.isMenu:
            pass

        elif self.isPaused:
            pass

        else:
            if keyCode == 114:
                main()


    def keyReleased(self, keyCode, modifier):
        if self.isMenu:
            pass

        elif self.isPaused:
            pass

        else:

            if keyCode == 119: # W
                self.player1.isRight = False
                self.player1.isLookRight, self.player1.isLookLeft = True, False
                self.player1.velocity[1] = 0
            if keyCode == 97: # A
                self.player1.isLeft = False
                self.player1.isLookRight, self.player1.isLookLeft = False, True
                self.player1.velocity[0] = 0
            if keyCode == 115: # S
                self.player1.isLeft = False
                self.player1.isLookRight, self.player1.isLookLeft = False, True
                self.player1.velocity[1] = 0
            if keyCode == 100: # D
                self.player1.isRight = False
                self.player1.isLookRight, self.player1.isLookLeft = True, False
                self.player1.velocity[0] = 0

    def timerFired(self, dt):
        keyCode = pygame.key.get_pressed()

        if self.isMenu:
            pass

        elif self.isPaused:
            pass

        else:
            if keyCode[119]:  # W
                if (self.player1.isLeft, self.player1.isRight) == (False, False):
                    self.player1.isRight = True
                self.player1.velocity[1] = -self.player1.speed


            if keyCode[97]:  # A
                self.player1.isLeft, self.player1.isLookLeft = True, True
                self.player1.velocity[0] = -self.player1.speed


            if keyCode[115]:  # S
                if (self.player1.isLeft, self.player1.isRight) == (False, False):
                    self.player1.isLeft = True
                self.player1.velocity[1] = self.player1.speed


            if keyCode[100]:  # D
                self.player1.isRight, self.player1.isLookRight = True, True
                self.player1.velocity[0] = self.player1.speed


            self.playerGroup.update(self.wallsGroup)


            if self.player1.centerX >= self.width:
                self.room += 1
                if self.room < 4:
                    if self.room > len(self.boardList) - 1:
                        newBoard = map.makeBoard(copy.deepcopy(map.mainBoard),map.obstacles)
                        self.boardList.append(newBoard)

                elif self.room ==4:
                    if self.room > len(self.boardList) - 1:
                        self.boardList.append(map.bossBoard)

                self.currBoard = self.boardList[self.room]
                self.initializeBoard()
                self.player1.x = 0
                self.player1.y = self.height//2

            elif self.player1.centerX <= 0:
                self.room -= 1
                self.currBoard = self.boardList[self.room]
                self.initializeBoard()
                self.player1.x = self.width - self.player1.rect.width
                self.player1.y = self.height//2





            '''
            if pygame.sprite.groupcollide(self.playerGroup, self.wallsGroup, False, False):
                wall = pygame.sprite.spritecollideany(self.player1, self.wallsGroup)
                halfPlayerH = self.player1.rect.height//2
                halfPlayerW = self.player1.rect.width//2
                tY = self.player1.y - self.player1.rect.height//2
                tX = self.player1.x - self.player1.rect.width//2
                bY = self.player1.y + self.player1.rect.height//2
                bX = self.player1.x + self.player1.rect.width//2
                wtY = wall.rect.y
                wtX = wall.rect.x
                wbY = wall.rect.y + wall.rect.height
                wbX = wall.rect.x + wall.rect.width


                if tY < wbY and bY > wbY:
                    self.player1.y = wbY + halfPlayerH
                elif tY < wtY and bY > wtY:
                    self.player1.y = wtY - halfPlayerH
                elif tX < wbX and bX > wbX:
                    self.player1.x = wbX + halfPlayerW +1
                elif tX < wtX and bX > wtX:
                    self.player1.x = wtX - 2*halfPlayerW -1
            '''


            for enemy in self.enemyGroup:
                if isinstance(enemy, enemies.Chaser):
                    enemy.chase((self.player1.centerX, self.player1.centerY))

            self.bulletsGroup.update()
            self.enemyGroup.update()


            self.timer += 1
            if self.timer % 200 == 50:
                x = random.randint(100, 400)
                y = random.randint(100, 400)
                enemy = enemies.Chaser(x,y)
                self.enemyGroup.add(enemy)


    def redrawAll(self, screen):

        if self.isMenu:
            # draws buttons
            screen.blit(self.menuBackground,self.menuBackRect)
            self.startBut.draw(screen)
            self.quitBut.draw(screen)
            self.instrBut.draw(screen)

        elif self.isPaused:
            pass

        elif self.isInstr:
            pass

        else:
            # setting up map attributes on screen
            self.currRoom = self.font.render("Rm:" + str(self.room), True, (255, 0, 0))
            self.currRoomRect = self.currRoom.get_rect(center=(self.width - 43, 50))

            self.currLevel = self.font.render("Lvl:" + str(self.level), True, (255, 0, 0))
            self.currLevelRect = self.currLevel.get_rect(center=(self.width - 43, 100))

            # setting up player attributes on screen
            self.p1Health1 = pygame.Surface((80,20))
            self.p1Health1.fill((255,255,255))
            self.p1Health2 = pygame.Surface((7.6*self.player1.currHealth,16))
            self.p1Health2.fill((255,0,0))
            self.p1Health1Rect = self.p1Health1.get_rect(center=(self.width - 43, 150))
            self.p1Health2Rect = self.p1Health2.get_rect()
            self.p1Health2Rect.x, self.p1Health2Rect.y = self.p1Health1Rect.x+2, self.p1Health1Rect.y+2


            # draws map
            pygame.sprite.Group.draw(self.wallsGroup, screen)
            pygame.sprite.Group.draw(self.floorGroup, screen)
            screen.blit(self.currRoom,self.currRoomRect)
            screen.blit(self.currLevel,self.currLevelRect)

            #draws player
            self.player1.preDraw()
            pygame.sprite.Group.draw(self.playerGroup,screen)
            screen.blit(self.p1HealthImage,self.p1HealthImageRect)
            screen.blit(self.p1TomsImage,self.p1TomsImageRect)
            screen.blit(self.p1Health1, self.p1Health1Rect)
            screen.blit(self.p1Health2, self.p1Health2Rect)
            screen.blit(self.p1Toms, self.p1TomsRect)
            # checks collisions between sprite groups
            pygame.sprite.groupcollide(self.bulletsGroup, self.enemyGroup, False, False)
            for bullet in self.bulletsGroup:
                hitEnemies = pygame.sprite.spritecollide(bullet,self.enemyGroup,False)
                for enemy in hitEnemies:
                    enemy.health -= bullet.power
                    bullet.kill()
                    if enemy.health <= 0:
                        enemy.kill()

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
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

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


