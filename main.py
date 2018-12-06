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
import math
import shelve


class PygameGame(object):

    def init(self):

        # Sprite Groups
        self.playerGroup = pygame.sprite.Group()
        self.playerBulletsGroup = pygame.sprite.Group()
        self.bossBulletsGroup = pygame.sprite.Group()
        self.enemyBulletsGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.bossGroup = pygame.sprite.Group()
        self.obstaclesGroup = pygame.sprite.Group()
        self.wallsGroup = pygame.sprite.Group()
        self.floorGroup = pygame.sprite.Group()
        self.powerUpGroup = pygame.sprite.Group()
        self.portalGroup = pygame.sprite.Group()
        self.chopGroup = pygame.sprite.Group()
        self.coinGroup = pygame.sprite.Group()


        # Initializations for the player and enemies
        self.player1 = player.Player(self.width//2, self.height//2)
        self.playerGroup.add(self.player1)
        self.player1.preDraw()
        self.shotAngle = 0
        self.currPowerUp = None
        self.powerUps = [misc.CircleShot, misc.Invincibility, misc.Health, misc.Speed, misc.Strength]
        self.puTimer = 500
        self.enemies = [enemies.Chaser, enemies.Onion]

        # Initializations for the map
        self.boardList = [map.startBoard]
        self.room = 0
        self.currBoard = self.boardList[self.room]
        self.initializeBoard()

        # Initializations for game data
        self.font = pygame.font.Font('font\coolFont.ttf', 30)
        self.level = 1
        self.roomDead = {0: True}
        self.enemiesLeft = 0
        self.bossTimer = 0
        self.soup = 0
        self.spatulas = 0
        self.weapon = [projectile.TomatoBullet,projectile.Spatula,projectile.SoupBomb]
        self.weaponSelect = 0
        self.money = 0


        self.p1HealthImage = pygame.image.load("pics\health.png")
        self.p1HealthImage = pygame.transform.scale(self.p1HealthImage, (60, 60))
        self.p1HealthImageRect = self.p1HealthImage.get_rect(center=(self.width - 40, 150))

        self.p1TomsImage = pygame.image.load("pics\omatoAmmo.png")
        self.p1TomsImage = pygame.transform.scale(self.p1TomsImage, (60, 60))
        self.p1TomsImageRect = self.p1TomsImage.get_rect(center=(self.width - 40, self.height - 140))

        self.p1Toms = pygame.image.load("pics\infinity.png")
        self.p1Toms = pygame.transform.scale(self.p1Toms, (36,36))
        self.p1TomsRect = self.p1Toms.get_rect(center=(self.width-40, self.height - 140))


        self.soupImageRaw = pygame.image.load("pics\soupAmmo.png")
        self.soupImage = pygame.transform.scale(self.soupImageRaw, (60,60))
        self.soupImageRect = self.p1TomsImage.get_rect(center = (self.width - 40, self.height - 40))

        self.spatulaImageRaw = pygame.image.load("pics\spatulaAmmo.png")
        self.spatulaImageR = pygame.transform.scale(self.spatulaImageRaw,(15,60))
        self.spatulaImage = pygame.transform.rotate(self.spatulaImageR, 45)
        self.spatulaImageRect = self.spatulaImage.get_rect(center = (self.width - 40, self.height - 90))

        # Modes
        self.isMenu = True
        self.isPaused = False
        self.isInstr = False
        self.isPauseInstr = False
        self.isChop = False
        self.gameOver = False


        # Initializations for menu screen
        self.startBut = misc.Button((self.width // 2 - 75, 4 * self.height // 7, 150, 75), "Start!")
        self.quitBut = misc.Button((self.width // 2 - 75, 5 * self.height // 7, 150, 75), "Quit!")
        self.instrBut = misc.Button((self.width // 2 - 75, 6 * self.height // 7, 150, 75), "Instructions")
        self.menuBackground = pygame.image.load('pics\menuBackground.png')
        self.menuBackground = pygame.transform.scale(self.menuBackground, (self.width, self.height))
        self.menuBackRect = self.menuBackground.get_rect()

        # Initializations for instructions screen
        self.backBut = misc.Button((50, self.height - 115, 150, 75), "Back")
        self.startBut2 = misc.Button((self.width - 200, self.height - 115, 150, 75), "Start!")
        self.instruBackground = pygame.image.load('pics\instruction.png')
        self.instruBackground = pygame.transform.scale(self.instruBackground, (self.width, self.height))
        self.instrBackRect = self.instruBackground.get_rect()

        # Initializations for gameover screen
        self.quitBut2 = misc.Button((50, self.height - 115, 150, 75), "Quit!")
        self.restBut = misc.Button((self.width - 200, self.height - 115, 150, 75), "Continue")
        self.gameoverBackground = pygame.image.load('pics\gameOver.png')
        self.gameoverBackground = pygame.transform.scale(self.gameoverBackground, (self.width, self.height))
        self.gameoverBackRect = self.gameoverBackground.get_rect()

        #Initializations for pause screen
        self.menuBut = misc.Button((self.width//2 - 75, self.height//2 +100, 150,75),"Menu")
        self.continueBut = misc.Button((self.width//2 - 75, self.height //2 , 150, 75), "Resume")
        self.pInstrBut = misc. Button ((self.width//2 - 75, self.height//2 + 200, 150, 75),"Instructions")
        self.pauseBackground = pygame.image.load('pics\pause.png')
        self.pauseBackground = pygame.transform.scale(self.pauseBackground,(self.width,self.height))
        self.pauseBackgroundRect = self.pauseBackground.get_rect()

        #Initialization for pause screen instrutions
        self.backBut2 = misc.Button((50, self.height - 115, 150, 75), "Back")
        self.pInstrBackground = pygame.image.load('pics\instruction.png')
        self.pInstrBackground = pygame.transform.scale(self.pInstrBackground, (self.width, self.height))
        self.pInstrBackRect = self.pInstrBackground.get_rect()

        #Initialization for chop screen
        self.chopMenuImageRaw = pygame.image.load('pics\chopScreen.png')
        self.chopMenuImage = pygame.transform.scale(self.chopMenuImageRaw,(2*self.width//3,self.height))
        self.chopMenuImageRect = self.chopMenuImage.get_rect(center = (self.width//2, self.height//2))

        self.buySpatula = misc.Button((self.width//2 + 75, 165,75,50 ),"$15",150)
        self.buySoup = misc.Button((self.width//2 +75,235,75,50),"$25",150)
        self.buyHealth = misc.Button((self.width//2 + 75, 305, 75, 50),"$20",150)
        self.buyMaxStr = misc.Button((self.width//2 - 155,500,75,50),"$40",150)
        self.buyMaxSpe = misc.Button((self.width//2 - 30, 500, 75,50),"$30",150)
        self.buyMaxHea = misc.Button((self.width//2 + 97, 500, 75,50),"$50",150)
        self.closeChop = misc.Button((self.width//2 + 150,50,75,50 ),"Close",125)


    # sets up random obstacles and new board every room
    def initializeBoard(self):
        self.wallsGroup.empty()
        self.floorGroup.empty()
        width = self.width // len(self.currBoard)
        height = self.height // len(self.currBoard)
        for i in range(len(self.currBoard)):
            for j in range(len(self.currBoard)):
                x = j * (width)
                y = i * (height)
                if self.currBoard[i][j] == 2:
                    int = random.randint(0,10)
                    if 0 < int < 4:
                        imageNum = int
                    else:
                        imageNum = 0
                    wallTop = map.Wall(x, y, width, height * 2, imageNum)
                    self.wallsGroup.add(wallTop)
                elif self.currBoard[i][j] == 1:
                    obstacle = map.Wall(x, y, width, height*2, 0)
                    self.wallsGroup.add(obstacle)
                elif self.currBoard[i][j] == 0 or self.currBoard[i][j] == 3 or self.currBoard[i][j] == 4 or \
                        self.currBoard[i][j] == 5:
                    floor = map.Floor(x,y,width,height*1.4)
                    self.floorGroup.add(floor)
                elif self.currBoard[i][j] == 9:
                    chop = misc.Chop(x,y,50,70)
                    self.chopGroup.add(chop)
                if self.currBoard[i][j] == 4 and self.roomDead[self.room] == False:
                    if self.level >= 5:
                        enem = random.choice(self.enemies)
                        enemy = enem(x,y,self.level)
                    else:
                        enemy = enemies.Chaser(x,y,self.level)
                    self.enemyGroup.add(enemy)
                    self.enemiesLeft += 1
                if self.currBoard[i][j] == 5 and self.roomDead[self.room] == False:
                    boss = enemies.OnionBoss(x,y,self.level)
                    self.bossGroup.add(boss)
                    self.enemiesLeft += 1
        for wall in self.wallsGroup:
            stuckEnemies = pygame.sprite.spritecollide(wall, self.enemyGroup,True)
            for enemy in stuckEnemies:
                enemy.kill()
                self.enemiesLeft -= len(stuckEnemies)



    def nextLevel(self):
        self.level += 1
        self.boardList = [map.startBoard]
        self.room = 0
        self.currBoard = self.boardList[self.room]
        self.initializeBoard()
        self.player1.x = self.width//2
        self.player1.y = self.height//2
        self.roomDead = {0: True}
        self.powerUpGroup.empty()

        for portal in self.portalGroup:
            portal.kill()

    def startGame(self):
        self.isMenu = False
        self.isPaused = False
        self.isInstr = False
        self.isPauseInstr = False
        self.isChop = False

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

    def pauseInstrScreen(self):
        self.isPaused = False
        self.isPauseInstr = True
        self.isMenu = False

    def openChop(self):
        self.isChop = True

    def gameOverScren(self):

        self.isMenu = False
        self.isInstr = False
        self.isPaused = False
        self.gameOver = True


    def mousePressed(self, x, y,):

        if self.isMenu:
            if self.startBut.clickCheck(x,y):
                self.startGame()
            elif self.quitBut.clickCheck(x,y):
                self.inGame = False
            elif self.instrBut.clickCheck(x,y):
                self.instrScreen()

        elif self.isPaused:
            if self.menuBut.clickCheck(x,y):
                main()
            elif self.continueBut.clickCheck(x,y):
                self.startGame()
            elif self.pInstrBut.clickCheck(x,y):
                self.pauseInstrScreen()

        elif self.isInstr:
            if self.startBut2.clickCheck(x,y):
                self.startGame()
            elif self.backBut.clickCheck(x,y):
                self.menuScreen()

        elif self.isPauseInstr:
            if self.backBut2.clickCheck(x,y):
                self.pauseScreen()

        elif self.gameOver:
            if self.quitBut2.clickCheck(x,y):
                self.inGame = False
            elif self.restBut.clickCheck(x,y):
                main()

        elif self.isChop:
            if self.buySpatula.clickCheck(x,y):
                if self.money >= 15:
                    self.money -= 15
                    self.spatulas += 10
            elif self.buySoup.clickCheck(x,y):
                if self.money >= 25:
                    self.money -= 25
                    self.soup += 10
            elif self.buyHealth.clickCheck(x,y):
                if self.money >= 20 and (self.player1.maxHealth - self.player1.currHealth >= 1):
                    self.money -= 20
                    self.player1.currHealth += 1
            elif self.buyMaxStr.clickCheck(x,y):
                if self.money >= 40:
                    self.money -= 40
                    self.player1.basePower += 0.1
            elif self.buyMaxSpe.clickCheck(x,y):
                if self.money >= 30:
                    self.money -= 30
                    self.player1.baseSpeed += 0.25
            elif self.buyMaxHea.clickCheck(x,y):
                if self.money >= 50:
                    self.money -= 50
                    self.player1.maxHealth += 1
                    self.player1.currHealth += 1
            elif self.closeChop.clickCheck(x,y):
                self.startGame()

        else:
            self.shotAngle = misc.getAngle(self.player1.centerX, self.player1.centerY, x, y)
            int = self.weaponSelect %3
            bulletType = self.weapon[int]
            if isinstance(self.currPowerUp,misc.CircleShot):
                for i in range(8):
                    bullet = bulletType(self.player1.centerX, self.player1.centerY,self.shotAngle+(i/4*math.pi))
                    if isinstance(bullet, projectile.SoupBomb) and self.soup > 0 :
                        self.playerBulletsGroup.add(bullet)
                    elif isinstance(bullet,projectile.Spatula) and self.spatulas > 0:
                        self.playerBulletsGroup.add(bullet)
                    elif isinstance(bullet, projectile.TomatoBullet):
                        self.playerBulletsGroup.add(bullet)

            else:
                bullet = bulletType(self.player1.centerX,self.player1.centerY,self.shotAngle)
                if isinstance(bullet, projectile.SoupBomb) and self.soup > 0:
                    self.playerBulletsGroup.add(bullet)
                    self.soup -= 1
                elif isinstance(bullet, projectile.Spatula) and self.spatulas > 0:
                    self.playerBulletsGroup.add(bullet)
                    self.spatulas -= 1
                elif isinstance(bullet, projectile.TomatoBullet):
                    self.playerBulletsGroup.add(bullet)



    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        if self.isMenu:
            self.startBut.mouseCheck(x,y)
            self.quitBut.mouseCheck(x,y)
            self.instrBut.mouseCheck(x,y)

        elif self.isPaused:
            self.menuBut.mouseCheck(x,y)
            self.continueBut.mouseCheck(x,y)
            self.pInstrBut.mouseCheck(x,y)

        elif self.isInstr:
            self.startBut2.mouseCheck(x,y)
            self.backBut.mouseCheck(x,y)

        elif self.isPauseInstr:
            self.backBut2.mouseCheck(x,y)

        elif self.gameOver:
            self.quitBut2.mouseCheck(x,y)
            self.restBut.mouseCheck(x,y)

        elif self.isChop:
            self.buySpatula.mouseCheck(x,y)
            self.buySoup.mouseCheck(x,y)
            self.buyHealth.mouseCheck(x,y)
            self.buyMaxStr.mouseCheck(x,y)
            self.buyMaxSpe.mouseCheck(x,y)
            self.buyMaxHea.mouseCheck(x,y)
            self.closeChop.mouseCheck(x,y)

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

            if keyCode == 112:
                self.pauseScreen()

            elif keyCode == 113:
                self.weaponSelect -= 1

            elif keyCode == 101:
                self.weaponSelect += 1

            elif keyCode == 114:
                print(self.player1.x, self.player1.y)

            elif pygame.sprite.groupcollide(self.playerGroup,self.portalGroup,False,False) and keyCode == 32:
                self.nextLevel()

            elif pygame.sprite.groupcollide(self.playerGroup,self.chopGroup,False,False) and keyCode == 32:
                self.openChop()




    def keyReleased(self, keyCode, modifier):
        if self.isMenu:
            pass

        elif self.isPaused:
            pass

        else:

            if keyCode == 119: # W
                self.player1.isRight,self.player1.isLeft = False,False
                self.player1.velocity[1] = 0
            if keyCode == 97: # A
                self.player1.isLeft = False
                self.player1.isLookRight, self.player1.isLookLeft = False, True
                self.player1.velocity[0] = 0
            if keyCode == 115: # S
                self.player1.isLeft,self.player1.isRight = False,False
                self.player1.velocity[1] = 0
            if keyCode == 100: # D
                self.player1.isRight = False
                self.player1.isLookRight, self.player1.isLookLeft = True,False
                self.player1.velocity[0] = 0

    def timerFired(self, dt):

        if self.isMenu:
            pass

        elif self.isPaused:
            pass

        else:
            #player movement
            keyCode = pygame.key.get_pressed()
            if keyCode[119]:  # W
                if (self.player1.isLookRight):
                    self.player1.isRight = True
                else:
                    self.player1.isLeft =True
                self.player1.velocity[1] = -self.player1.speed
            if keyCode[97]:  # A
                self.player1.isLookRight = False
                self.player1.isLeft, self.player1.isLookLeft = True, True
                self.player1.velocity[0] = -self.player1.speed
            if keyCode[115]:  # S
                if (self.player1.isLookLeft):
                    self.player1.isLeft = True
                else:
                    self.player1.isRight = True
                self.player1.velocity[1] = self.player1.speed
            if keyCode[100]:  # D
                self.player1.isLookLeft = False
                self.player1.isRight, self.player1.isLookRight = True, True
                self.player1.velocity[0] = self.player1.speed

            # sets up room switch when player moves to side of the screen
            if self.player1.centerX > self.width:
                if self.roomDead[self.room] == True:
                    self.room += 1
                    if self.room < 4:
                        if self.room > len(self.boardList) - 1:
                            newBoard = map.makeBoard(copy.deepcopy(map.mainBoard),map.obstacles)
                            self.boardList.append(newBoard)
                        self.chopGroup.empty()
                    elif self.room ==4:
                        if self.room > len(self.boardList) - 1:
                            self.boardList.append(map.bossBoard)
                    enemiesDead = self.roomDead.get(self.room, None)
                    if enemiesDead == None:
                        self.roomDead[self.room] = False
                    self.currBoard = self.boardList[self.room]
                    self.initializeBoard()
                    self.player1.x = 0
                    self.player1.y = self.height//2
                    self.powerUpGroup.empty()
                else:
                    self.player1.x = self.width - self.player1.rect.width//2

            elif self.player1.centerX < 0:
                if self.roomDead[self.room] == True:
                    self.room -= 1
                    self.currBoard = self.boardList[self.room]
                    self.initializeBoard()
                    self.player1.x = self.width - self.player1.rect.width
                    self.player1.y = self.height//2
                    self.powerUpGroup.empty()
                else:
                    self.player1.x =  0- self.player1.rect.width//2
                    self.player1.rect.x = self.player1.x
            # only allows player to move between rooms if all enemies are dead
            if self.enemiesLeft <= 0:
                self.roomDead[self.room] = True

            # enemy movement
            for enemy in self.enemyGroup:
                #kills any enemies outside map
                if (enemy.rect.x  < 110 and  (enemy.rect.y < 210 or enemy.rect.y > 400)) or (enemy.rect.x > 630 and \
                                               (210 > enemy.rect.y  or enemy.rect.y > 400)):
                    enemy.kill()
                    self.enemiesLeft -= 1

                enemy.chase((self.player1.centerX, self.player1.centerY), self.wallsGroup)
                if isinstance(enemy, enemies.Onion):
                    if enemy.bullets == 0 and enemy.isClose(self.player1.centerX,self.player1.centerY):
                        enemyx = enemy.rect.x + (enemy.rect.width//2)
                        enemyy = enemy.rect.y + (enemy.rect.height//2)
                        angle = misc.getAngle(enemyx, enemyy, self.player1.centerX, self.player1.centerY)
                        bullet = projectile.OnionBullet(enemyx, enemyy, angle, enemy)
                        enemy.bullets += 1
                        self.enemyBulletsGroup.add(bullet)
                if pygame.sprite.spritecollide(enemy,self.wallsGroup,False) or enemy.rect.x < 0 \
                                                or enemy.rect.x > self.width:
                    if (isinstance(enemy, enemies.Chaser)):
                        enemy.switchDir()

            # boss movement
            for boss in self.bossGroup:
                if pygame.sprite.spritecollide(boss, self.wallsGroup, False) or boss.rect.x < 0 \
                        or boss.rect.x > self.width:
                    boss.switchDir()
                self.bossTimer += 1
                # Boss attack speed based on current level
                if self.bossTimer % (150 // (self.level/2)) == 0:
                    sX = boss.rect.x + boss.rect.width // 2
                    sY = boss.rect.y + boss.rect.height // 2
                    dX = self.player1.centerX
                    dY = self.player1.centerY
                    angle = misc.getAngle(sX, sY, dX, dY)
                    if isinstance(boss, enemies.OnionBoss):
                        int = random.randint(0,5)
                        # one sixth chance of bass spawning enemies and only spawns if total enemies is less than 10
                        if int == 0 and self.enemiesLeft < 10:
                            for i in range(0, 5):
                                angleDiff = i * (2 * math.pi / 5)
                                x = sX + 100*(math.cos(angle+angleDiff))
                                y = sY + 100*(math.sin(angle+angleDiff))
                                enemy = enemies.Onion(x,y,self.level)
                                self.enemyGroup.add(enemy)
                                self.enemiesLeft += 1
                            for enemy in self.enemyGroup:
                                if pygame.sprite.spritecollide(enemy,self.wallsGroup,False):
                                    enemy.kill()
                                    self.enemiesLeft -= 1
                                elif (enemy.rect.x < 110 and (enemy.rect.y < 210 or enemy.rect.y > 400)) or (
                                        enemy.rect.x > 630 and (210 > enemy.rect.y or enemy.rect.y > 400)):
                                    enemy.kill()
                                    self.enemiesLeft -= 1
                        # one third chance of boss firing in circle
                        elif 0 < int < 3:
                            for i in range(0, 8):
                                angleDiff = i * (2 * math.pi / 8)
                                bullet = projectile.BossOnionBullet(sX, sY, angle + angleDiff)
                                self.bossBulletsGroup.add(bullet)
                        # one half chance of a normal bullet fire
                        elif 3<= int <=5:
                            bullet = projectile.BossOnionBullet(sX, sY, angle)
                            self.bossBulletsGroup.add(bullet)





            # checks collisions between sprite groups
            for bullet in self.playerBulletsGroup:
                hitEnemies = pygame.sprite.spritecollide(bullet, self.enemyGroup, False)
                hitBoss = pygame.sprite.spritecollide(bullet,self.bossGroup,False)
                for enemy in hitEnemies:
                    enemy.health -= bullet.power * self.player1.power
                    bullet.kill() #TODO must change when different bullets are implemented
                    if enemy.health <= 0:
                        #sets up random chance of power up drop upon enemy death
                        int = random.randint(0,30)
                        if int == 30:
                            pu = random.choice(self.powerUps)
                            powerUp = pu(enemy.rect.center[0],enemy.rect.center[1])
                            self.powerUpGroup.add(powerUp)
                        enemy.kill()
                        self.enemiesLeft -= 1
                for boss in hitBoss:
                    boss.health -= bullet.power*self.player1.power
                    bullet.kill()
                    if boss.health <= 0:
                        # drops ladder to advance to next level
                        ladder = misc.Portal(boss.rect.x, boss.rect.y)
                        self.portalGroup.add(ladder)
                        coin = misc.Coin(boss.rect.x + boss.rect.width//2, boss.rect.y + boss.rect.height//2)
                        self.coinGroup.add(coin)
                        boss.kill()
                        self.enemiesLeft -= 1



            # deletes bullets that hit walls
            pygame.sprite.groupcollide(self.playerBulletsGroup, self.wallsGroup, True, False)
            pygame.sprite.groupcollide(self.bossBulletsGroup, self.wallsGroup, True, False)
            for bullet in self.enemyBulletsGroup:
                if pygame.sprite.spritecollide(bullet,self.wallsGroup,False):
                    onion = bullet.origin
                    onion.bullets -= 1
                    bullet.kill()


            #lowers player health if hit
            invincible = isinstance(self.currPowerUp,misc.Invincibility)
            hitPlayer = pygame.sprite.spritecollide(self.player1, self.enemyGroup, False)
            hitPlayerBoss = pygame.sprite.spritecollide(self.player1,self.bossGroup,False,pygame.sprite.collide_mask)
            for enemy in hitPlayer:
                if not invincible:
                    self.player1.currHealth -= enemy.power

            for boss in hitPlayerBoss:
                if not invincible:
                    self.player1.currHealth -= boss.power
            for boss in self.bossGroup:
                for bullet in self.bossBulletsGroup:
                    if pygame.sprite.spritecollide(self.player1, self.bossBulletsGroup, True) and not invincible:
                        self.player1.currHealth -= bullet.power + boss.power

            for bullet in self.enemyBulletsGroup:
                if pygame.sprite.spritecollide(self.player1,self.enemyBulletsGroup,False) and not invincible:
                    self.player1.currHealth -= bullet.power + bullet.origin.power
                    bullet.origin.bullets -= 1
                    bullet.kill()


            # player dies and game over screen appears
            if self.player1.currHealth <= 0.01:
                self.player1.kill()
                self.gameOverScren()


            #power up changes
            #sets up power up timer
            if self.currPowerUp != None:
                self.puTimer -= 1
                if self.puTimer == 0:
                    self.currPowerUp = None
            #checks for player collision with power up
            hitPU = pygame.sprite.spritecollide(self.player1, self.powerUpGroup,False)
            if hitPU:
                self.currPowerUp = hitPU[0]
                if isinstance(hitPU[0],misc.Health):
                    if self.player1.maxHealth - self.player1.currHealth > 3:
                        self.player1.currHealth += 3
                    else:
                        self.player1.currHealth = self.player1.maxHealth
                elif isinstance(hitPU[0],misc.Strength):
                    self.player1.power *= 5
                elif isinstance(hitPU[0],misc.Speed):
                    self.player1.speed *= 2
                hitPU[0].kill()
                self.puTimer = 500

            # resets stats if player does not have powerup
            if self.currPowerUp == None:
                self.player1.speed = self.player1.baseSpeed
                self.player1.power = self.player1.basePower

            #checks if player has picked up coin
            if pygame.sprite.spritecollide(self.player1,self.coinGroup,True):
                self.money += 100

            # group updates
            self.playerGroup.update(self.wallsGroup)
            self.playerBulletsGroup.update()
            self.enemyGroup.update(self.wallsGroup)
            self.bossGroup.update()
            self.bossBulletsGroup.update()
            self.enemyBulletsGroup.update()


    def redrawAll(self, screen):

        if self.isMenu:
            screen.blit(self.menuBackground,self.menuBackRect)
            self.startBut.draw(screen)
            self.quitBut.draw(screen)
            self.instrBut.draw(screen)

        elif self.isPaused:
            screen.blit(self.pauseBackground,self.pauseBackgroundRect)
            self.menuBut.draw(screen)
            self.continueBut.draw(screen)
            self.pInstrBut.draw(screen)
            self.currLevelDisp = misc.Text((self.width//2 - 150, self.height//2 - 100, 300, 75),
                                           "You are Currently at Level " + str(self.level) + ", Room " + \
                                           str(self.room), (255,0,0))
            self.currLevelDisp.draw(screen)

        elif self.isInstr:
            screen.blit(self.instruBackground,self.instrBackRect)
            self.startBut2.draw(screen)
            self.backBut.draw(screen)

        elif self.isPauseInstr:
            screen.blit(self.pInstrBackground, self.pInstrBackRect)
            self.backBut2.draw(screen)

        elif self.gameOver:
            self.leveldisp = misc.Text((self.width // 2 - 150, self.height // 2, 300, 75), "You Reached Level " \
                                       + str(self.level) + ", Room " + str(self.room), (255, 0, 0))
            screen.blit(self.gameoverBackground,self.gameoverBackRect)
            self.quitBut2.draw(screen)
            self.restBut.draw(screen)
            self.leveldisp.draw(screen)

            # Highscore
            currScore = (self.level,self.room)
            shelfFile = shelve.open("highscore")
            highScore = shelfFile.get('score',(0,0))
            if (currScore[0] >= highScore[0] and currScore[1] >= highScore[1]) or (currScore[0] >= highScore[0]):
                shelfFile['score'] = currScore
            shelfFile.close()

            self.hiScoreDisp = misc.Text((self.width // 2 - 150, self.height // 2 + 100, 300, 75),
                                         "The Highscore is Level " + str(highScore[0]) + ", Room " + str(highScore[1]),
                                         (255, 0, 0))
            self.hiScoreDisp.draw(screen)


        else:
            # setting up map attributes on screen
            self.currRoom = self.font.render("Rm:" + str(self.room), True, (255, 0, 0))
            self.currRoomRect = self.currRoom.get_rect(center=(self.width - 43, 100))
            self.currLevel = self.font.render("Lvl:" + str(self.level), True, (255, 0, 0))
            self.currLevelRect = self.currLevel.get_rect(center=(self.width - 43, 75))
            self.soupText = self.font.render(str(self.soup),True,(0,0,0))
            self.soupTextRect = self.soupText.get_rect(center = (self.width - 40, self.height - 40))
            self.spatulaText = self.font.render(str(self.spatulas),True,(0,0,0))
            self.spatulaTextRect = self.spatulaText.get_rect(center = (self.width - 40,self.height - 90))



            if self.currPowerUp != None:
                puttX = self.width - 43
                puttY = 37

                self.puTimerText = self.font.render(str(self.puTimer//50),True,(255,255,255))
                self.puTimerTextRect = self.puTimerText.get_rect(center = (puttX,puttY))

            # setting up player attributes on screen
            self.p1Health1 = pygame.Surface((80,20))
            self.p1Health1.fill((255,255,255))
            self.p1Health2 = pygame.Surface((7.6*self.player1.currHealth,16))
            self.p1Health2.fill((255,0,0))
            self.p1Health1Rect = self.p1Health1.get_rect(center=(self.width - 43, 150))
            self.p1Health2Rect = self.p1Health2.get_rect()
            self.p1Health2Rect.x, self.p1Health2Rect.y = self.p1Health1Rect.x+2, self.p1Health1Rect.y+2


            # setting up boss attributes on screen
            for boss in self.bossGroup:
                len = 296/boss.maxHealth
                self.bossHealth1 = pygame.Surface((len*boss.health,46))
                if boss.health / boss.maxHealth < 0.25:
                    self.bossHealth1.fill((255,0,0))
                else:
                    self.bossHealth1.fill((0,255,0))
                self.bossHealth2 = pygame.Surface((300,50))
                self.bossHealth2.fill((255,255,255))
                self.bossHealth2Rect = self.bossHealth2.get_rect(center = (self.width//2 + 100, 30))
                self.bossHealth1Rect = self.bossHealth1.get_rect()
                self.bossHealth1Rect.x , self.bossHealth1Rect.y = self.bossHealth2Rect.x+2 , self.bossHealth2Rect.y+2


            # draws map
            pygame.sprite.Group.draw(self.floorGroup, screen)
            pygame.sprite.Group.draw(self.wallsGroup, screen)
            pygame.sprite.Group.draw(self.chopGroup, screen)
            screen.blit(self.currRoom,self.currRoomRect)
            screen.blit(self.currLevel,self.currLevelRect)

            # draws coins
            pygame.sprite.Group.draw(self.coinGroup,screen)

            # draws portal
            pygame.sprite.Group.draw(self.portalGroup, screen)

            #draws player
            self.player1.draw(screen)

            #draws health and ammo
            if self.weaponSelect % 3 == 0:
                center = (self.width - 40, self.height - 140)
            elif self.weaponSelect % 3 == 1:
                center = (self.width - 40, self.height - 90)
            elif self.weaponSelect % 3 == 2:
                center = (self.width - 40, self.height - 40)

            screen.blit(self.p1HealthImage,self.p1HealthImageRect)
            screen.blit(self.p1TomsImage,self.p1TomsImageRect)
            screen.blit(self.p1Health1, self.p1Health1Rect)
            screen.blit(self.p1Health2, self.p1Health2Rect)
            screen.blit(self.soupImage,self.soupImageRect)
            screen.blit(self.spatulaImage,self.spatulaImageRect)
            pygame.draw.circle(screen,(0,200,0),center,20,5)
            screen.blit(self.p1Toms, self.p1TomsRect)
            screen.blit(self.soupText,self.soupTextRect)
            screen.blit(self.spatulaText,self.spatulaTextRect)



            #draws bullets
            pygame.sprite.Group.draw(self.playerBulletsGroup, screen)
            pygame.sprite.Group.draw(self.bossBulletsGroup, screen)
            pygame.sprite.Group.draw(self.enemyBulletsGroup,screen)

            #draws enemies
            pygame.sprite.Group.draw(self.enemyGroup, screen)

            #draws boss
            pygame.sprite.Group.draw(self.bossGroup,screen)
            #draws boss health
            for boss in self.bossGroup:
                screen.blit(self.bossHealth2,self.bossHealth2Rect)
                screen.blit(self.bossHealth1,self.bossHealth1Rect)

            #draws powerUps
            pygame.sprite.Group.draw(self.powerUpGroup, screen)
            if self.currPowerUp != None:
                wid = self.currPowerUp.image.get_width()
                hei = self.currPowerUp.image.get_height()
                if not isinstance(self.currPowerUp,misc.Health):
                    screen.blit(self.currPowerUp.image,(puttX - wid//2,puttY - hei//2,wid,hei))
                    screen.blit(self.puTimerText,self.puTimerTextRect)

        if self.isChop:
            self.moneyText = self.font.render(str(self.money), True, (0, 0, 0))
            self.moneyTextRect = self.moneyText.get_rect(center=(self.width // 2, 107))
            screen.blit(self.chopMenuImage,self.chopMenuImageRect)
            self.buySpatula.draw(screen)
            self.buySoup.draw(screen)
            self.buyHealth.draw(screen)
            self.buyMaxStr.draw(screen)
            self.buyMaxSpe.draw(screen)
            self.buyMaxHea.draw(screen)
            self.closeChop.draw(screen)
            screen.blit(self.moneyText,self.moneyTextRect)





    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=800, height=600, fps=50, title="John's TP"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        self.inGame = True
        pygame.init()

    def run(self):
        self.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE)
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        while self.inGame:

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
                    self.inGame = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()


