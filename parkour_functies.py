from pauze import *
from common import *
import pygame
from pygame import RESIZABLE
import time
WIDTH = 1366
HEIGHT = 690
gravity = 0.6
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)



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
            if platform.ObjectScene == scene:
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
            if platform.ObjectScene == scene:
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
            Collider = platform.Type
        if self.xpos + self.width > WIDTH:
            self.xpos = WIDTH - self.width
            Collider.append(platform.Type)
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
        return Collider

    def draw(self, surface, CameraPosx):
        self.Rect = pygame.draw.rect(surface, self.color, (self.xpos - CameraPosx, self.ypos, self.width, self.height))

class MoveObject:
    def __init__(self, StartPos, EndPos, Speed, WaitTime):
        self.StartPos = StartPos
        self.EndPos = EndPos
        self.Speed = 100 / Speed
        self.WaitTime = WaitTime

        self.xDirection = self.EndPos[0] - self.StartPos[0]
        self.yDirection = self.EndPos[1] - self.StartPos[1]
        self.Direction = (self.xDirection / self.Speed, self.yDirection / self.Speed)

    def Move(self, pos):

        if pos == self.StartPos:
            xDirection = self.EndPos[0] - self.StartPos[0]
            yDirection = self.EndPos[1] - self.StartPos[1]
            self.Direction = (xDirection / self.Speed, yDirection / self.Speed)

        if 8 > (self.EndPos[0] - pos[0]) + (self.EndPos[1] - pos[1]) > -8 :
            endpos = self.EndPos
            self.EndPos = self.StartPos
            self.StartPos = endpos
            xDirection = self.EndPos[0] - self.StartPos[0]
            yDirection = self.EndPos[1] - self.StartPos[1]
            self.Direction = (xDirection / self.Speed, yDirection / self.Speed)

        TargetPos = pos[0] + self.Direction[0], pos[1] + self.Direction[1]

        return TargetPos


def parkour(player):
    """
    The entire code of the platforming part of the game
    :param player: The active player
    :return:
    """
    clock = pygame.time.Clock()
    fps = 60
    gravity = 0.6
    jump_height = -25
    speed = 10
    running = True
    scene = 1
    mouseDown = False
    CameraPosx = 0
    RespawnPos = (-900, 450)
    pos1 = (0, 0)
    CollisionGlitch = True

    playerObject = Objects(-90 , 450, 50, 50, 'green', 2, 0, 0, 1, "Player")
    cube1 = Objects(-500, 500, 900, 1500, 'black', 1, 0, 0, 1, "Collider")
    cube2 = Objects(400, 580, 570, 950, 'black', 1, 0, 0, 1, "Collider")
    cube3 = Objects(833, 428, 600, 2430, 'black', 1, 0, 0, 1, "Collider")
    cube10 = Objects(-200, 320, 80, 180, 'orange', 1, 0, 0, 1, enemy("BOB", (255, 255, 0), 50, ["punch"], 0))

    cube5 = Objects(461, 581, 412, 500, 'black', 1, 0, 0, 2, "Collider")
    cube7 = Objects(-700, 428, 887, 500, 'black', 1, 0, 0, 2, "Collider")
    cube8 = Objects(1109, 481, 350, 500, 'black', 1, 0, 0, 2, "Collider")
    cube6 = Objects(700, 300, 131, 58, 'black', 1, 0, 0, 2, "Collider")
    cube4 = Objects(344, 100, 213, 15, 'black', 1, 0, 0, 2, "Collider")

    cube9 = Objects(564, 116, 3500, 2000, 'black', 1, 0, 0, 4, "Collider")
    cube11 = Objects(-500, 530, 576, 500, 'black', 1, 0, 0, 4, "Collider")
    cube12 = Objects(365, 420, 313, 500, 'black', 1, 0, 0, 4, "Collider")
    cube13 = Objects(365, 430, 313, 54, 'black', 1, 0, 0, 4, "Collider")
    cube14 = Objects(22, 200, 150, 54, 'black', 1, 0, 0, 4, "Collider")
    cube15 = Objects(-417, 93, 150, 20, 'black', 1, 0, 0, 4, "Collider")

    cube16 = Objects(-550, 29, 250, 571, 'black', 1, 0, 0, 1, "Collider")

    cube17  = Objects(-500, 130, 218, 1000, 'black', 1, 0, 0, 5, "Collider")
    cube18 =  Objects(-326, 400, 284, 500, 'black', 1, 0, 0, 5, "Collider")
    cube19 =  Objects(69, 200, 1000, 30, 'black', 1, 0, 0, 5, "Collider")
    cube20 =  Objects(430, 467, 70, 500, 'black', 1, 0, 0, 5, "Collider")
    cube21 =  Objects(70, 630, 70, 500, 'black', 1, 0, 0, 5, "Collider")
    cube22 = Objects(850, 620, 110, 500, 'black', 1, 0, 0, 5, "Collider")
    cube23 = Objects(1223, 400, 200, 500, 'black', 1, 0, 0, 5, "Collider")

    cube24 = Objects(-500, 410, 200, 700, 'black', 1, 0, 0, 6, "Collider")
    cube25 = Objects(-27, 544, 150, 300, 'black', 1, 0, 0, 6, "Collider")
    cube26 = Objects(425, 431, 150, 400, 'black', 1, 0, 0, 6, "Collider")
    cube27 = Objects(828, 500, 150, 400, 'black', 1, 0, 0, 6, "Collider")
    cube28 = Objects(1200, 380, 200, 500, 'black', 1, 0, 0, 6, "Collider")

    # voeg hier nieuwe platformen to zodat ze collision krijgen.
    platforms = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10, cube11, cube12, cube13, cube14, cube15, cube16, cube17, cube18, cube19, cube20, cube21, cube22, cube23, cube24, cube25, cube26, cube27, cube28]

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
        if scene == 1:
            RespawnPos = (270, 450)
            playerObject.draw(screen, CameraPosx)
            cube1.draw(screen, CameraPosx)
            cube10.draw(screen, CameraPosx)
            cube2.draw(screen, CameraPosx)
            cube3.draw(screen, CameraPosx)

            cube16.draw(screen, CameraPosx)
        if scene == 2:
            RespawnPos = (350, 380)
            playerObject.draw(screen, CameraPosx)
            cube4.draw(screen, CameraPosx)
            cube6.draw(screen, CameraPosx)
            cube5.draw(screen, CameraPosx)
            cube7.draw(screen, CameraPosx)
            cube8.draw(screen, CameraPosx)
        if scene == 3:
            LevelGehaald()
            scene += 1
            player.lives = 5
        if scene == 4:
            RespawnPos = (300, 450)
            playerObject.draw(screen, CameraPosx)
            cube9.draw(screen, CameraPosx)
            cube11.draw(screen, CameraPosx)
            cube12.draw(screen, CameraPosx)
            cube13.draw(screen, CameraPosx)
            cube14.draw(screen, CameraPosx)
            cube15.draw(screen, CameraPosx)
        if scene == 5:
            RespawnPos = (200, 335)
            playerObject.draw(screen, CameraPosx)
            cube17.draw(screen, CameraPosx)
            cube18.draw(screen, CameraPosx)
            cube19.draw(screen, CameraPosx)
            cube20.draw(screen, CameraPosx)
            cube21.draw(screen, CameraPosx)
            cube22.draw(screen, CameraPosx)
            cube23.draw(screen, CameraPosx)
        if scene == 6:
            RespawnPos = (200, 335)
            playerObject.draw(screen, CameraPosx)
            cube24.draw(screen, CameraPosx)
            cube25.draw(screen, CameraPosx)
            cube26.draw(screen, CameraPosx)
            cube27.draw(screen, CameraPosx)
            cube28.draw(screen, CameraPosx)



        if scene == 7:
            eind()
            return "Menu"




        playerObject.xspeed = speed * (keys["right"] - keys["left"])
        # maakt de speler dood
        for Collider in Colliders:
            if playerObject.ypos >= 630 or Collider == "Death" or type(Collider) == MoveObject:
                player.lives, state = game_over(player.lives)
                playerObject.xpos -= RespawnPos[0]
                playerObject.ypos -= RespawnPos[1]
                if state is not None:
                    return state

            #returns enemy waarmee je collide
            if type(Collider) == enemy:
                return Collider



        #(cube15.xpos, cube15.ypos) = cube15.Type.Move((int(cube15.xpos), int(cube15.ypos)))


        # veranderd camera position
        if L_border <= playerObject.xpos <= R_border:
            CameraPosx = playerObject.xpos - 500
        elif L_border >= playerObject.xpos:
            CameraPosx = L_border - 500
        elif playerObject.xpos >= R_border:
            CameraPosx = R_border - 500

        # linker scene transition
        if L_border - 500 > playerObject.xpos and not scene  in [1, 4]:
            playerObject.xpos = R_border + 700
            CameraPosx = R_border - 500
            scene -= 1
            CollisionGlitch = False
        #rechter scene transition
        elif playerObject.xpos > R_border + 800:
            playerObject.xpos = L_border - 450
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