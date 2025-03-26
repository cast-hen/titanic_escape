from pauze import *
from common import *
import pygame
import random
from pygame import RESIZABLE
import time
gravity = 0.6
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()




class Objects:
    def __init__(self, xpos, ypos, width, height, color, mass, xspeed, yspeed, ObjectScene, Type):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.mass = mass
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.Rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.on_ground = False
        self.ObjectScene = ObjectScene
        self.Type = Type

    def update_pos(self, platforms, CameraPosx, scene):

        Collider = []
        self.xpos += self.xspeed
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)

        for platform in platforms:
            if scene in platform.ObjectScene:
                if self.Rect.colliderect(platform.Rect):
                    if self.xspeed > 0:
                        self.xpos = platform.xpos - self.width
                    elif self.xspeed < 0:
                        self.xpos = platform.xpos + platform.width
                    self.xspeed = 0
                    self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
                    Collider.append(platform.Type)

        self.yspeed += self.mass * gravity

        self.ypos += self.yspeed
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
        self.on_ground = False

        # platformcollision
        for platform in platforms:
            if scene in platform.ObjectScene:
                if self.Rect.colliderect(platform.Rect):
                    if self.yspeed > 0:  # Falling
                        self.ypos = platform.ypos - self.height
                        self.yspeed = 0
                        self.on_ground = True
                    elif self.yspeed < 0:  # Hitting ceiling
                        self.ypos = platform.ypos + platform.height
                        self.yspeed = 0
                    self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
                    Collider.append(platform.Type)



        # wall en floor collision
        if self.ypos + self.height >= HEIGHT - 4:
            self.ypos = HEIGHT - self.height - 4
            self.yspeed = 0
            self.on_ground = True
            self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
            Collider.append(platform.Type)
        if self.xpos + self.width > WIDTH:
            self.xpos = WIDTH - self.width
            Collider.append(platform.Type)
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
        return Collider

    def draw(self, surface, CameraPosx):
        self.Rect = pygame.draw.rect(surface, self.color, (self.xpos - CameraPosx, self.ypos, self.width, self.height))

class MoveObject:
    def __init__(self, StartPos, EndPos, Speed, WaitTime, Teleport, Randomness):
        self.StartPos = StartPos
        self.EndPos = EndPos
        self.Speed = 100 / Speed
        self.WaitTime = WaitTime
        self.Teleport = Teleport
        self.Randomness = Randomness

        self.randomNumber = 0

        self.xDirection = self.EndPos[0] - self.StartPos[0]
        self.yDirection = self.EndPos[1] - self.StartPos[1]
        self.Direction = (self.xDirection / self.Speed, self.yDirection / self.Speed)

    def Move(self, pos):
        if self.randomNumber == 0:
            self.randomNumber = random.randint(-self.Randomness, self.Randomness)
        if pos == self.StartPos:
            xDirection = self.EndPos[0] - self.StartPos[0]
            yDirection = self.EndPos[1] - self.StartPos[1]
            self.Direction = (xDirection / self.Speed, yDirection / self.Speed)

        if 8 > (self.EndPos[0] - pos[0] + self.randomNumber) + (self.EndPos[1] - pos[1]) > -8 :
            if self.Teleport:
                endpos = self.EndPos
                self.EndPos = self.StartPos
                self.StartPos = endpos
                xDirection = self.EndPos[0] - self.StartPos[0]
                yDirection = self.EndPos[1] - self.StartPos[1]
                self.Direction = (xDirection / self.Speed, yDirection / self.Speed)
                self.randomNumber = 0

            else:
                self.randomNumber = random.randint(-self.Randomness, self.Randomness)
                pos = (self.StartPos[0]  + self.randomNumber, self.StartPos[1])



        TargetPos = pos[0] + self.Direction[0], pos[1] + self.Direction[1]

        return TargetPos


def parkour(player):
    """
    The entire code of the platforming part of the game
    :param player: The active player
    :return: the new state or the enemy that is encountered
    """
    clock = pygame.time.Clock()
    fps = 60
    gravity = 0.6
    jump_height = -25
    speed = 11
    running = True
    scene = 1
    mouseDown = False
    CameraPosx = 0
    RespawnPos = (-900, 450)
    pos1 = (0, 0)
    CollisionGlitch = True
    InvisibilityFrames = 0

    playerObject = Objects(-90 , 450, 50, 50, 'green', 2, 0, 0, [1], "Player")
    cube1 = Objects(-500, 500, 900, 1500, 'black', 1, 0, 0, [1], "Collider")
    cube2 = Objects(400, 580, 570, 950, 'black', 1, 0, 0, [1], "Collider")
    cube3 = Objects(833, 428, 600, 2430, 'black', 1, 0, 0, [1], "Collider")
    cube10 = Objects(-200, 320, 80, 180, 'orange', 1, 0, 0, [1], enemy("BOB", (255, 255, 0), 100, ["punch"], 0))

    cube5 = Objects(461, 581, 412, 500, 'black', 1, 0, 0, [2], "Collider")
    cube7 = Objects(-700, 428, 887, 500, 'black', 1, 0, 0, [2], "Collider")
    cube8 = Objects(1109, 481, 350, 500, 'black', 1, 0, 0, [2], "Collider")
    cube6 = Objects(700, 300, 131, 58, 'black', 1, 0, 0, [2], "Collider")
    cube4 = Objects(344, 100, 213, 15, 'black', 1, 0, 0, [2], "Collider")

    cube9 = Objects(564, 116, 3500, 2000, 'black', 1, 0, 0, [4], "Collider")
    cube11 = Objects(-500, 530, 576, 500, 'black', 1, 0, 0, [4], "Collider")
    cube12 = Objects(365, 420, 313, 500, 'black', 1, 0, 0, [4], "Collider")
    cube13 = Objects(365, 430, 313, 54, 'black', 1, 0, 0, [4], "Collider")
    cube14 = Objects(22, 200, 150, 54, 'black', 1, 0, 0, [4], "Collider")
    cube15 = Objects(-417, 93, 150, 20, 'black', 1, 0, 0, [4], "Collider")

    cube16 = Objects(-550, 29, 250, 571, 'black', 1, 0, 0, [1], "Collider")

    cube17  = Objects(-500, 130, 218, 1000, 'black', 1, 0, 0, [5], "Collider")
    cube18 =  Objects(-326, 400, 284, 500, 'black', 1, 0, 0, [5], "Collider")
    cube19 =  Objects(69, 200, 1000, 30, 'black', 1, 0, 0, [5], "Collider")
    cube20 =  Objects(430, 467, 70, 500, 'black', 1, 0, 0, [5], "Collider")
    cube21 =  Objects(70, 630, 70, 500, 'black', 1, 0, 0, [5], "Collider")
    cube22 = Objects(850, 620, 110, 500, 'black', 1, 0, 0, [5], "Collider")
    cube23 = Objects(1223, 400, 200, 500, 'black', 1, 0, 0, [5], "Collider")

    cube24 = Objects(-500, 410, 200, 700, 'black', 1, 0, 0, [6], "Collider")
    cube25 = Objects(-27, 544, 150, 300, 'black', 1, 0, 0, [6], "Collider")
    cube26 = Objects(425, 431, 150, 400, 'black', 1, 0, 0, [6], "Collider")
    cube27 = Objects(828, 250, 150, 800, 'black', 1, 0, 0, [6], "Collider")
    cube28 = Objects(1200, 380, 200, 500, 'black', 1, 0, 0, [6], "Collider")

    cube29 = Objects(-500, 415, 300, 500, 'black', 1, 0, 0, [7], "Collider")
    cube30 = Objects(35, 650, 830, 300, 'black', 1, 0, 0, [7], "Collider")
    cube31 = Objects(1100, 430, 300, 500, 'black', 1, 0, 0, [7], "Collider")

    cube32 = Objects(-500, 435, 300, 500, 'black', 1, 0, 0, [8], "Collider")
    cube33 = Objects(-206, 525, 540, 400, 'black', 1, 0, 0, [8], "Collider")
    cube34 = Objects(250, 630, 1500, 300, 'black', 1, 0, 0, [8], "Collider")
    cube35 = Objects(1150, 0, 400, 440, 'black', 1, 0, 0, [8], "Collider")

    cube36 = Objects(-500, 635, 2500, 445, 'black', 1, 0, 0, [10], "Collider")
    cube37 = Objects(-200, 530, 470, 180, 'black', 1, 0, 0, [10], "Collider")
    cube38 = Objects(125, 365, 525, 325, 'black', 1, 0, 0, [10], "Collider")
    cube39 = Objects(625, 500, 430, 250, 'black', 1, 0, 0, [10], "Collider")
    cube40 = Objects(1025, 280, 400, 475, 'black', 1, 0, 0, [10], "Collider")

    cube41 = Objects(460, 0, 60, 60, 'red', 1, 0, 0, [10], MoveObject((460, -100), (460, 2000), 0.5, 10, False, 100))
    cube42 = Objects(1050, 600, 60, 60, 'red', 1, 0, 0, [10], MoveObject((1050, -100), (1050, 2000), 0.4, 10, False, 100))
    cube43 = Objects(150, 300, 60, 60, 'red', 1, 0, 0, [10], MoveObject((150, -100), (150, 2000), 0.6, 10, False, 100))

    cube44 = Objects(-500, 285, 400, 600, 'black', 1, 0, 0, [11], "Collider")
    cube45 = Objects(216, 400, 475, 370, 'black', 1, 0, 0, [11], "Collider")
    cube48 = Objects(1050, 500, 350, 300, 'black', 1, 0, 0, [11], "Collider")

    cube46 = Objects(0, -100, 60, 60, 'red', 1, 0, 0, [11], MoveObject((0, -100), (0, 2000), 1, 10, False, 0))
    cube47 = Objects(50, -250, 60, 60, 'red', 1, 0, 0, [11], MoveObject((50, -100), (50, 2000), 1, 10, False, 0))
    cube49 = Objects(790, -100, 150, 150, 'red', 1, 0, 0, [11], MoveObject((790, -100), (790, 2000), 0.8, 10, False, 0))
    cube50 = Objects(800, 1000, 150, 150, 'red', 1, 0, 0, [11], MoveObject((790, -100), (790, 2000), 0.8, 10, False, 0))

    cube51 = Objects(-500, 505, 350, 300, 'black', 1, 0, 0, [12], "Collider")
    cube52 = Objects(-160, 575, 600, 250, 'black', 1, 0, 0, [12], "Collider")
    cube53 = Objects(285, 480, 540, 290, 'black', 1, 0, 0, [12], "Collider")
    cube54 = Objects(335, 0, 150, 350, 'black', 1, 0, 0, [12, 13], "Collider")
    cube55 = Objects(810, 520, 560, 250, 'black', 1, 0, 0, [12], "Collider")

    cube56 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.63, 10, False, 200))
    cube57 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.73, 10, False, 200))
    cube58 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.5, 10, False, 200))
    cube59 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.8, 10, False, 400))
    cube60 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.75, 10, False, 400))
    cube61 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.7, 10, False, 400))
    cube62 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.55, 10, False, 400))
    cube63 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.65, 10, False, 400))

    cube64 = Objects(-500, 525, 250, 300, 'black', 1, 0, 0, [13], "Collider")
    cube65 = Objects(285, 480, 320, 380, 'black', 1, 0, 0, [13], "Collider")
    cube66 = Objects(-50, 360, 150, 500, 'black', 1, 0, 0, [13], "Collider")
    cube67 = Objects(910, 380, 500, 400, 'black', 1, 0, 0, [13], "Collider")

    cube68 = Objects(-500, 385, 500, 400, 'black', 1, 0, 0, [14], "Collider")
    cube69 = Objects(222, 450, 130, 30, 'black', 1, 0, 0, [14], "Collider")
    cube70 = Objects(555, 360, 130, 30, 'black', 1, 0, 0, [14], "Collider")
    cube71 = Objects(1165, 650,250 , 500, 'black', 1, 0, 0, [14], "Collider")
    cube72 = Objects(888, 540, 130, 30, 'black', 1, 0, 0, [14], "Collider")
    cube73 = Objects(1165, 0, 250, 350, 'black', 1, 0, 0, [14], "Collider")

    cube74 = Objects(227, 1000, 120, 120, 'red', 1, 0, 0, [14], MoveObject((227, -100), (227, 2500), 0.7, 10, False, 0))
    cube75 = Objects(888, 0, 120, 120, 'red', 1, 0, 0, [14], MoveObject((888, -100), (888, 2500), 0.7, 10, False, 0))
    cube76 = Objects(555, 500, 120, 120, 'red', 1, 0, 0, [14], MoveObject((555, -100), (555, 2500), 0.7, 10, False, 0))

    cube77 = Objects(-500, 650, 2000, 500, 'black', 1, 0, 0, [15], "Collider")
    cube78 = Objects(-500, 190, 2000, 250, 'black', 1, 0, 0, [15], "Collider")
    cube79 = Objects(-500, 0, 300, 350, 'black', 1, 0, 0, [15], "Collider")
    cube80 = Objects(1100, 0, 300, 350, 'black', 1, 0, 0, [15], "Collider")

    cube81 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 4, 10, False, 500))
    cube82 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 4.5, 10, False, 500))
    cube83 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 5.5, 10, False, 500))

    # voeg hier nieuwe platformen to zodat ze collision krijgen.
    platforms = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10,
                 cube11, cube12, cube13, cube14, cube15, cube16, cube17, cube18, cube19, cube20,
                 cube21, cube22, cube23, cube24, cube25, cube26, cube27, cube28, cube29, cube30,
                 cube31, cube32, cube33, cube34, cube35, cube36, cube37, cube38, cube39, cube40,
                 cube41, cube42, cube43, cube44, cube45, cube46, cube47, cube48, cube49, cube50,
                 cube51, cube52, cube53, cube54, cube55, cube56, cube57, cube58, cube59, cube60,
                 cube61, cube62, cube63, cube64, cube65, cube66, cube67, cube68, cube69, cube70,
                 cube71, cube72, cube73, cube74, cube75, cube76, cube77, cube78, cube79, cube80,
                 cube81, cube82, cube83]

    PlayerPos2 = (playerObject.xpos, playerObject.ypos)
    PlayerPos1 = PlayerPos2

    # random ahhh movement fix, couldn't bother om een betere oplossig te vinden.
    keys = {"left": False, "right": False, "up": False}

    L_border = 0
    R_border = 500

    # game loop
    while running:
        mouse = pygame.mouse.get_pos()
        clock.tick(fps)
        screen.fill((135, 206, 250))
        Colliders = playerObject.update_pos(platforms, CameraPosx, scene)

        #Collision glitch fix
        if CollisionGlitch:

            if Afstand(PlayerPos1, PlayerPos2) < 50 or Afstand(PlayerPos1, PlayerPos2) > 500 :
                PlayerPos1 = PlayerPos2
            else:
                (playerObject.xpos, playerObject.ypos) = PlayerPos1


            PlayerPos2 = (playerObject.xpos, playerObject.ypos)
        else:
            PlayerPos2 = (playerObject.xpos, playerObject.ypos)
            PlayerPos1 = PlayerPos2
            CollisionGlitch = True


        #spawnt alle objects

        for platform in platforms:
            if scene in platform.ObjectScene:
                platform.draw(screen, CameraPosx)
            if type(platform.Type) == MoveObject:
                (platform.xpos, platform.ypos) = platform.Type.Move((int(platform.xpos), int(platform.ypos)))
        if scene == 1:
            RespawnPos = (270, 450)
            playerObject.draw(screen, CameraPosx)

            cube16.draw(screen, CameraPosx)
        elif scene == 2:
            RespawnPos = (-35, 400)
            playerObject.draw(screen, CameraPosx)

        elif scene == 3:
            scene += 1
        elif scene == 4:
            RespawnPos = (-170, 500)
            playerObject.draw(screen, CameraPosx)

        elif scene == 5:
            RespawnPos = (-175, 370)
            playerObject.draw(screen, CameraPosx)

        elif scene == 6:
            RespawnPos = (-380, 385)
            playerObject.draw(screen, CameraPosx)

        elif scene == 7:
            RespawnPos = (-340, 350)
            playerObject.draw(screen, CameraPosx)

        elif scene == 8:
            RespawnPos = (-340, 350)
            playerObject.draw(screen, CameraPosx)

        elif scene == 9:
            LevelGehaald()
            scene += 1
            player.lives = 5

        elif scene == 10:
            RespawnPos = (-340, 350)
            playerObject.draw(screen, CameraPosx)

        elif scene == 11:
            RespawnPos = (-340, 150)
            playerObject.draw(screen, CameraPosx)

        elif scene == 12:
            RespawnPos = (-320, 400)
            playerObject.draw(screen, CameraPosx)
        elif scene == 13:
            RespawnPos = (-340, 400)
            playerObject.draw(screen, CameraPosx)
        elif scene == 14:
            RespawnPos = (-340, 300)
            playerObject.draw(screen, CameraPosx)
        elif scene == 15:
            RespawnPos = (-340, 400)
            playerObject.draw(screen, CameraPosx)



        elif scene == 16:
            eind()

        elif scene == 13:
            eind(player.name)

            return "Menu"

        player.displayInfo()

        playerObject.xspeed = speed * (keys["right"] - keys["left"])

        # maakt de speler dood
        for Collider in Colliders:
            if (playerObject.ypos >= HEIGHT - playerObject.height - 10 or Collider == "Death" or type(Collider) == MoveObject) and InvisibilityFrames == 0:
                player.lives, state = game_over(player.lives)
                playerObject.xpos = RespawnPos[0]
                playerObject.ypos = RespawnPos[1]
                CollisionGlitch = False
                InvisibilityFrames += 50
                if state is not None:
                    return state

            #returns enemy waarmee je collide
            if type(Collider) == enemy:
                return Collider


        # verandert camera position
        if L_border <= playerObject.xpos <= R_border:
            CameraPosx = playerObject.xpos - 500
        elif L_border >= playerObject.xpos:
            CameraPosx = L_border - 500
        elif playerObject.xpos >= R_border:
            CameraPosx = R_border - 500

        # linker scene transition
        if L_border - 500 > playerObject.xpos and not scene  in [1, 10]:
            playerObject.xpos = R_border + 700
            CameraPosx = R_border - 500
            playerObject.ypos -= 20
            scene -= 1
            CollisionGlitch = False
        #rechter scene transition
        elif playerObject.xpos > R_border + 800:
            playerObject.xpos = L_border - 450
            playerObject.ypos -= 20
            CameraPosx = L_border - 500
            scene += 1
            CollisionGlitch = False

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                if pos1 == (0, 0):
                    pos1 = (mouse[0] + CameraPosx, mouse[1])
                else:
                    print(pos1[0], pos1[1], mouse[0] + CameraPosx - pos1[0], mouse[1] - pos1[1])
                    pos1 = (0, 0)

            # movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keys["right"] = True
                elif event.key == pygame.K_a:
                    keys["left"] = True
                elif event.key == pygame.K_w:
                    keys["up"] = True

                elif event.key == pygame.K_ESCAPE:
                    if Pause() == "Menu":
                        return "Menu"
                    else:
                        keys = {"left": False, "right": False, "up": False}
                    screen.fill((0, 0, 0))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keys["right"] = False
                elif event.key == pygame.K_a:

                    keys["left"] = False
                elif event.key == pygame.K_w:
                    keys["up"] = False


            if keys["up"] == True and playerObject.on_ground:
                playerObject.yspeed = jump_height

        pygame.display.flip()

        if InvisibilityFrames > 0:
            InvisibilityFrames -= 1

