from common import *
import pygame
import random
from pygame import RESIZABLE
import time
gravity = 0.6
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
# image1 = pygame.transform.scale(pygame.image.load('resources/textures/titanic 3rd class interior backdrop.png').convert(), (pygame.display.get_window_size()))



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

#Enemies
enemyBOB_1 = character("BOB", 1, (255, 255, 0), 100, 100,["punch"], [], 0, True)
enemyJAN_1 = character("JAN", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyJANBOB_2 = character("JANBOB", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyBOBJAN_1 = character("BOBJAN", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyBOBBOBBOB_1 = character("BOBBOBBOB", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyBobbie_1 = character("Bobbie", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyWillem_1 = character("Willem", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyAlexander_1 = character("Alexander", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyWillem_Henk_1 = character("Willem-Henk", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyBoze_Janje_1 = character("Boze Jantje", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)
enemyKwaardaardige_BOB_1 = character("Kwaadaardige BOB", 1, (255, 255, 0), 10, 10,["punch"], [], 0, True)

#All objects
#Tijdelijke player objects, worden plaatjes
playerObject = Objects(game_manager.Player_posx, game_manager.Player_posy, 50, 50, 'green', 2, 0, 0, [1], "Player")
playerColor_Still = 'green'
playerColor_Left = 'yellow'
playerColor_Right = 'blue'
playerColor_Jump = 'red'


cube1_1 = Objects(-500, 500, 900, 1500, 'black', 1, 0, 0, [1], "Collider")
cube1_2 = Objects(400, 580, 570, 950, 'black', 1, 0, 0, [1], "Collider")
cube1_3 = Objects(833, 428, 600, 2430, 'black', 1, 0, 0, [1], "Collider")
cube1_Enemy_test = Objects(-200, 320, 80, 180, 'orange', 1, 0, 0, [1], enemyBOB_1)
cube1_Enemy1 = Objects(1050, 170, 130, 270, 'orange', 1, 0, 0, [1], enemyJAN_1)
cube1_5 = Objects(-550, 29, 250, 571, 'black', 1, 0, 0, [1], "Collider")

cube2_1 = Objects(461, 581, 412, 500, 'black', 1, 0, 0, [2], "Collider")
cube2_2 = Objects(-700, 428, 887, 500, 'black', 1, 0, 0, [2], "Collider")
cube2_3 = Objects(1109, 481, 350, 500, 'black', 1, 0, 0, [2], "Collider")
cube2_4 = Objects(700, 300, 131, 58, 'black', 1, 0, 0, [2], "Collider")
cube2_5 = Objects(344, 100, 213, 15, 'black', 1, 0, 0, [2], "Collider")

cube4_1 = Objects(564, 116, 3500, 2000, 'black', 1, 0, 0, [4], "Collider")
cube4_2 = Objects(-500, 530, 576, 500, 'black', 1, 0, 0, [4], "Collider")
cube4_3 = Objects(365, 420, 313, 500, 'black', 1, 0, 0, [4], "Collider")
cube4_4 = Objects(365, 430, 313, 54, 'black', 1, 0, 0, [4], "Collider")
cube4_5 = Objects(22, 200, 150, 54, 'black', 1, 0, 0, [4], "Collider")
cube4_6 = Objects(-417, 93, 150, 20, 'black', 1, 0, 0, [4], "Collider")
cube4_Enemy1 = Objects(1040, -190, 100, 300, 'orange', 1, 0, 0, [4], enemyBOBJAN_1)

cube5_1  = Objects(-500, 130, 218, 1000, 'black', 1, 0, 0, [5], "Collider")
cube5_2 =  Objects(-326, 400, 284, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_3 =  Objects(69, 200, 1000, 30, 'black', 1, 0, 0, [5], "Collider")
cube5_4 =  Objects(430, 467, 70, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_5 =  Objects(70, 630, 70, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_6 = Objects(850, 620, 110, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_7 = Objects(1223, 400, 200, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_Enemy1 = Objects(640, -100, 100, 300, 'orange', 1, 0, 0, [5], enemyBOBBOBBOB_1)

cube6_1 = Objects(-500, 410, 200, 700, 'black', 1, 0, 0, [6], "Collider")
cube6_2 = Objects(-27, 544, 150, 300, 'black', 1, 0, 0, [6], "Collider")
cube6_3 = Objects(425, 431, 150, 400, 'black', 1, 0, 0, [6], "Collider")
cube6_4 = Objects(828, 250, 150, 800, 'black', 1, 0, 0, [6], "Collider")
cube6_5 = Objects(1200, 380, 200, 500, 'black', 1, 0, 0, [6], "Collider")

cube7_1 = Objects(-500, 415, 300, 500, 'black', 1, 0, 0, [7], "Collider")
cube7_2 = Objects(35, 650, 830, 300, 'black', 1, 0, 0, [7], "Collider")
cube7_3 = Objects(1100, 430, 300, 500, 'black', 1, 0, 0, [7], "Collider")
cube7_Enemy1 = Objects(590, 360, 100, 300, 'orange', 1, 0, 0, [7], enemyBobbie_1)

cube8_1 = Objects(-500, 435, 300, 500, 'black', 1, 0, 0, [8], "Collider")
cube8_2 = Objects(-206, 525, 540, 400, 'black', 1, 0, 0, [8], "Collider")
cube8_3 = Objects(250, 630, 1500, 300, 'black', 1, 0, 0, [8], "Collider")
cube8_4 = Objects(1150, 0, 400, 440, 'black', 1, 0, 0, [8], "Collider")

cube10_1 = Objects(-500, 635, 2500, 445, 'black', 1, 0, 0, [10], "Collider")
cube10_2 = Objects(-200, 530, 470, 180, 'black', 1, 0, 0, [10], "Collider")
cube10_3 = Objects(125, 365, 525, 325, 'black', 1, 0, 0, [10], "Collider")
cube10_4 = Objects(625, 500, 430, 250, 'black', 1, 0, 0, [10], "Collider")
cube10_5 = Objects(1025, 280, 400, 475, 'black', 1, 0, 0, [10], "Collider")
cube10_Enemy1 = Objects(825, 85, 100, 400, 'orange', 1, 0, 0, [10], enemyWillem_1)

cube10_6 = Objects(460, 0, 60, 60, 'red', 1, 0, 0, [10], MoveObject((460, -100), (460, 2000), 0.5, 10, False, 100))
cube10_7 = Objects(1050, 600, 60, 60, 'red', 1, 0, 0, [10], MoveObject((1050, -100), (1050, 2000), 0.4, 10, False, 100))
cube10_8 = Objects(150, 300, 60, 60, 'red', 1, 0, 0, [10], MoveObject((150, -100), (150, 2000), 0.6, 10, False, 100))

cube11_1 = Objects(-500, 285, 400, 600, 'black', 1, 0, 0, [11], "Collider")
cube11_2 = Objects(216, 400, 475, 370, 'black', 1, 0, 0, [11], "Collider")
cube11_3 = Objects(1050, 500, 350, 300, 'black', 1, 0, 0, [11], "Collider")
cube11_Enemy1 = Objects(485, 93, 100, 300, 'orange', 1, 0, 0, [11], enemyAlexander_1)

cube11_4 = Objects(0, -100, 60, 60, 'red', 1, 0, 0, [11], MoveObject((0, -100), (0, 2000), 1, 10, False, 0))
cube11_5 = Objects(50, -250, 60, 60, 'red', 1, 0, 0, [11], MoveObject((50, -100), (50, 2000), 1, 10, False, 0))
cube11_6 = Objects(790, -100, 150, 150, 'red', 1, 0, 0, [11], MoveObject((790, -100), (790, 2000), 0.8, 10, False, 0))
cube11_7 = Objects(800, 1000, 150, 150, 'red', 1, 0, 0, [11], MoveObject((790, -100), (790, 2000), 0.8, 10, False, 0))

cube12_1 = Objects(-500, 505, 350, 300, 'black', 1, 0, 0, [12], "Collider")
cube12_2 = Objects(-160, 575, 600, 250, 'black', 1, 0, 0, [12], "Collider")
cube12_3 = Objects(285, 480, 540, 290, 'black', 1, 0, 0, [12], "Collider")
cube12_4 = Objects(810, 520, 560, 250, 'black', 1, 0, 0, [12], "Collider")
cube12_13_1 = Objects(335, 0, 150, 350, 'black', 1, 0, 0, [12, 13], "Collider")

cube12_13_2 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.63, 10, False, 200))
cube12_13_3 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.73, 10, False, 200))
cube12_13_4 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.5, 10, False, 200))
cube12_13_5 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.8, 10, False, 400))
cube12_13_6 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.75, 10, False, 400))
cube12_13_7 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.7, 10, False, 400))
cube12_13_8 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.55, 10, False, 400))
cube12_13_9 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.65, 10, False, 400))

cube13_1 = Objects(-500, 530, 250, 300, 'black', 1, 0, 0, [13], "Collider")
cube13_2 = Objects(285, 480, 320, 380, 'black', 1, 0, 0, [13], "Collider")
cube13_3 = Objects(-50, 360, 150, 500, 'black', 1, 0, 0, [13], "Collider")
cube13_4 = Objects(910, 380, 500, 400, 'black', 1, 0, 0, [13], "Collider")

cube14_1 = Objects(-500, 385, 500, 400, 'black', 1, 0, 0, [14], "Collider")
cube14_2 = Objects(222, 450, 130, 30, 'black', 1, 0, 0, [14], "Collider")
cube14_3 = Objects(555, 360, 130, 30, 'black', 1, 0, 0, [14], "Collider")
cube14_4 = Objects(1165, 650,250 , 500, 'black', 1, 0, 0, [14], "Collider")
cube14_5 = Objects(888, 540, 130, 30, 'black', 1, 0, 0, [14], "Collider")
cube14_6 = Objects(1165, 0, 250, 350, 'black', 1, 0, 0, [14], "Collider")

cube14_7 = Objects(227, 1000, 120, 120, 'red', 1, 0, 0, [14], MoveObject((227, -100), (227, 2500), 0.7, 10, False, 0))
cube14_8 = Objects(888, 0, 120, 120, 'red', 1, 0, 0, [14], MoveObject((888, -100), (888, 2500), 0.7, 10, False, 0))
cube14_9 = Objects(555, 500, 120, 120, 'red', 1, 0, 0, [14], MoveObject((555, -100), (555, 2500), 0.7, 10, False, 0))

cube15_16_1 = Objects(-500, 650, 2000, 500, 'black', 1, 0, 0, [15,16], "Collider")
cube15_2 = Objects(-500, 190, 2000, 250, 'black', 1, 0, 0, [15], "Collider")
cube15_3 = Objects(-500, 0, 300, 350, 'black', 1, 0, 0, [15], "Collider")
cube15_4 = Objects(1100, 0, 300, 350, 'black', 1, 0, 0, [15], "Collider")
cube15_Enemy1 = Objects(69, 440, 100, 400, 'orange', 1, 0, 0, [15], enemyWillem_Henk_1)
cube15_Enemy2 = Objects(880, 440, 100, 400, 'orange', 1, 0, 0, [15], enemyBoze_Janje_1)

cube15_5 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 4, 10, False, 500))
cube15_6 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 4.5, 10, False, 500))
cube15_7 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 5.5, 10, False, 500))

cube16_1 = Objects(-500, 0, 300, 400, 'black', 1, 0, 0, [16], "Collider")
cube16_2 = Objects(1200, 100, 270, 570, 'black', 1, 0, 0, [16], "Collider")
cube16_3 = Objects(1100, 100, 270, 385, 'black', 1, 0, 0, [16], "Collider")
cube16_4 = Objects(640, 410, 175, 40, 'black', 1, 0, 0, [16], "Collider")
cube16_5 = Objects(210, 330, 175, 40, 'black', 1, 0, 0, [16], "Collider")
cube16_6 = Objects(-210, 280, 180, 120, 'black', 1, 0, 0, [16], "Collider")
cube16_7 = Objects(-215, 0, 130, 160, 'black', 1, 0, 0, [16], "Collider")
cube16_8 = Objects(615, 90, 175, 40, 'black', 1, 0, 0, [16], "Collider")

cube16_9 = Objects(0, -400, 300, 300, 'red', 1, 0, 0, [16], MoveObject((0, -400), (0, 2500), 0.5, 10, False, 0))
cube16_10 = Objects(350, -400, 300, 300, 'red', 1, 0, 0, [16], MoveObject((350, -400), (350, 2500), 0.5, 10, False, 0))
cube16_11 = Objects(700, -400, 300, 300, 'red', 1, 0, 0, [16], MoveObject((700, -400), (700, 2500), 0.5, 10, False, 0))

cube17_1 = Objects(-500, 100, 270, 770, 'black', 1, 0, 0, [17], "Collider")
cube17_2 = Objects(-500, 330, 1000, 500, 'black', 1, 0, 0, [17], "Collider")
cube17_3 = Objects(465, 530, 1000, 500, 'black', 1, 0, 0, [17], "Collider")
cube17_4 = Objects(300, 0, 1200, 75, 'black', 1, 0, 0, [17], "Collider")
cube17_Enemy1 = Objects(950, 164, 160, 370, 'orange', 1, 0, 0, [17], enemyKwaardaardige_BOB_1)

cube19_1 = Objects(-500, 530, 1500, 300, 'black', 1, 0, 0, [19], "Collider")

cube_RisingWater = Objects(-500, 800, 2000, 1000, 'blue', 1, 0, 0, [19], MoveObject((800, 1000), (800, 0), 0.1, 10, False, 0))

# voeg hier nieuwe platformen to zodat ze collision krijgen.
platforms = [cube1_1, cube1_2, cube1_3, cube1_Enemy_test, cube1_Enemy1, cube1_5,
             cube2_1, cube2_1, cube2_2, cube2_3, cube2_4, cube2_5,
             cube4_1, cube4_2, cube4_3, cube4_4, cube4_5, cube4_6, cube4_Enemy1,
             cube5_1, cube5_2, cube5_3, cube5_4, cube5_5, cube5_6, cube5_7, cube5_Enemy1,
             cube6_1, cube6_2, cube6_3, cube6_4, cube6_5,
             cube7_1, cube7_2, cube7_3, cube7_Enemy1,
             cube8_1, cube8_2, cube8_3, cube8_4,
             cube10_1, cube10_2, cube10_3, cube10_4, cube10_5, cube10_6, cube10_7, cube10_8, cube10_Enemy1,
             cube11_1, cube11_2, cube11_3, cube11_4, cube11_5, cube11_6, cube11_7, cube11_Enemy1,
             cube12_1, cube12_2, cube12_3, cube12_4,
             cube12_13_1, cube12_13_2, cube12_13_3, cube12_13_4, cube12_13_5, cube12_13_6, cube12_13_7, cube12_13_8, cube12_13_9,
             cube13_1, cube13_2, cube13_3, cube13_4,
             cube14_1, cube14_2, cube14_3, cube14_4, cube14_5, cube14_6, cube14_7, cube14_8, cube14_9,
             cube15_16_1, cube15_2, cube15_3,cube15_4, cube15_5, cube15_6, cube15_7, cube15_Enemy1, cube15_Enemy2,
             cube16_1, cube16_2, cube16_3, cube16_4, cube16_5, cube16_6, cube16_7, cube16_8, cube16_9, cube16_10, cube16_11,
             cube17_1, cube17_2, cube17_3, cube17_4, cube17_Enemy1,
             cube19_1, cube_RisingWater]

# Other contstants
clock = pygame.time.Clock()
fps = 60
jump_height = -25
speed = 11

def parkour(player, game_manager):
    """
    The entire code of the platforming part of the game
    :param player: The active player
    :return: the new state or the enemy that is encountered
    """
    running = True
    scene = game_manager.scene
    mouseDown = False
    CameraPosx = 0
    RespawnPos = (-900, 450)
    playerObject.xpos = game_manager.Player_posx + 20
    playerObject.ypos = game_manager.Player_posy
    pos1 = (0, 0)
    CollisionGlitch = True
    InvisibilityFrames = 5

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
        # screen.blit(image1, (0 ,0))
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


        if playerObject.yspeed != 0:
            playerObject.color = playerColor_Jump
        elif playerObject.xspeed < 0:
            playerObject.color = playerColor_Left
        elif playerObject.xspeed > 0:
            playerObject.color = playerColor_Right
        else:
            playerObject.color = playerColor_Still

        #spawnt alle objects

        for platform in platforms:
            if scene in platform.ObjectScene:
                platform.draw(screen, CameraPosx)
            if type(platform.Type) == MoveObject:
                (platform.xpos, platform.ypos) = platform.Type.Move((int(platform.xpos), int(platform.ypos)))
            elif type(platform.Type) == character:
                if not platform.Type.alive:
                    platforms.remove(platform)
        if scene == 1:
            RespawnPos = (270, 450)
            playerObject.draw(screen, CameraPosx)

            cube1_1.draw(screen, CameraPosx)
        elif scene == 2:
            RespawnPos = (-35, 300)
            playerObject.draw(screen, CameraPosx)

        elif scene == 3:
            scene += 1
        elif scene == 4:
            RespawnPos = (-170, 400)
            playerObject.draw(screen, CameraPosx)

        elif scene == 5:
            RespawnPos = (-175, 300)
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
            RespawnPos = (-440, 600)
            playerObject.draw(screen, CameraPosx)
        elif scene == 17:
            RespawnPos = (-440, 600)
            playerObject.draw(screen, CameraPosx)
        elif scene == 18:
            LevelGehaald()
            scene += 1
            player.lives = 5
            cube_RisingWater.ypos = 900
        elif scene == 19:
            RespawnPos = (-440, 600)
            playerObject.draw(screen, CameraPosx)

        elif scene == 20:
            eind(player.name)
            return "Menu"


        player.displayInfo()

        playerObject.xspeed = speed * (keys["right"] - keys["left"])

        # maakt de speler dood
        for Collider in Colliders:
            if (playerObject.ypos >= HEIGHT - playerObject.height - 10 or Collider == "Death" or type(Collider) == MoveObject) and InvisibilityFrames == 0:
                player.lives, state = game_over(player.lives)
                player.hitpoints = player.maxHitpoints
                playerObject.xpos = RespawnPos[0]
                playerObject.ypos = RespawnPos[1]
                CollisionGlitch = False
                InvisibilityFrames += 50

                cube_RisingWater.ypos = 800
                if state is not None:
                    return state

            #returns enemy waarmee je collide
            if type(Collider) == character:
                if Collider.alive == True and InvisibilityFrames == 0:
                    return Collider
        #print(InvisibilityFrames)


        # verandert camera position
        if L_border <= playerObject.xpos <= R_border:
            CameraPosx = playerObject.xpos - 500
        elif L_border >= playerObject.xpos:
            CameraPosx = L_border - 500
        elif playerObject.xpos >= R_border:
            CameraPosx = R_border - 500

        # linker scene transition
        if L_border - 500 > playerObject.xpos and not scene  in [1, 10, 19]:
            playerObject.xpos = R_border + 700
            CameraPosx = R_border - 500
            playerObject.ypos -= 30
            scene -= 1
            CollisionGlitch = False
            InvisibilityFrames = 25
        #rechter scene transition
        elif playerObject.xpos > R_border + 800:
            playerObject.xpos = L_border - 450
            playerObject.ypos -= 30
            CameraPosx = L_border - 500
            scene += 1
            CollisionGlitch = False
            InvisibilityFrames = 25

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
        game_manager.scene = scene
        (game_manager.Player_posx, game_manager.Player_posy) = (playerObject.xpos, playerObject.ypos)

