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

        Collider = ""
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
                    Collider = platform.Type

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
                    Collider = platform.Type



        # wall en floor collision
        if self.ypos + self.height >= HEIGHT - 4:
            self.ypos = HEIGHT - self.height - 4
            self.yspeed = 0
            self.on_ground = True
            self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
            Collider = platform.Type
        if self.xpos + self.width > WIDTH:
            self.xpos = WIDTH - self.width
            Collider = platform.Type
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



# maakt vloer
def draw_floor():
    """
    Draws the floor
    :return:
    """
    pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 25)

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
    RespawnPos = (0, 0)
    pos1 = (0, 0)

    playerObject = Objects(300, 200, 50, 50, 'green', 2, 0, 0, 1, "Player")
    cube1 = Objects(580, 400, 60, 60, 'Red', 1, 0, 0, 1, MoveObject((580, 400), (580, 0), 1, 0))
    cube2 = Objects(690, 546, 600, 40, 'black', 1, 0, 0, 1, "Collider")
    cube3 = Objects(-800, 546, 1200, 60, 'black', 1, 0, 0, 1, "Collider")
    cube4 = Objects(800, 300, 80, 80, 'orange', 1, 0, 0, 1, enemy("greg", (255, 0, 0), 50, ["punch"], 0))
    cube10 = Objects(-200, 300, 80, 80, 'orange', 1, 0, 0, 1, enemy("BOB", (255, 255, 0), 500, ["punch"], 0))
    cube5 = Objects(630, 374, 80, 80, 'black', 1, 0, 0, 2, "Collider")
    cube7 = Objects(970, 320, 80, 80, 'black', 1, 0, 0, 2, "Collider")
    cube8 = Objects(1200, 180, 80, 80, 'black', 1, 0, 0, 2, "Collider")
    cube6 = Objects(-800, 546, 1200, 60, 'black', 1, 0, 0, 2, "Collider")
    cube9 = Objects(-300, 550, 5000, 100, 'black', 1, 0, 0, 4, "Collider")

    cube11 = Objects(-500, 275, 200, 400, 'black', 1, 0, 0, 4, "Collider")
    cube12 = Objects(330, 415, 230, 10, 'black', 1, 0, 0, 4, "Collider")
    cube13 = Objects(750, 0, 230, 450, 'black', 1, 0, 0, 4, "Collider")
    cube14 = Objects(1240, 400, 120, 250, 'black', 1, 0, 0, 4, "Collider")
    cube15 = Objects(-285, 450, 60, 120, 'Red', 1, 0, 0, 4, MoveObject((-285, 500), (1220, 500), 1.5, 0))

    cube16 = Objects(-494, 29, 202, 571, 'black', 1, 0, 0, 1, "Collider")
    # voeg hier nieuwe platformen to zodat ze collision krijgen.
    platforms = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10, cube11, cube12, cube13, cube14, cube15, cube16]

    # random ahhh movement fix, couldn't bother om een betere oplossig te vinden.
    keys = {"left": False, "right": False, "up": False}

    L_border = 0
    R_border = 500

    # game loop
    while running:
        mouse = pygame.mouse.get_pos()
        clock.tick(fps)
        screen.fill((135, 206, 250))
        Collider = playerObject.update_pos(platforms, CameraPosx, scene)


        if scene == 1:
            RespawnPos = (200, 300)
            playerObject.draw(screen, CameraPosx)
            cube1.draw(screen, CameraPosx)
            cube10.draw(screen, CameraPosx)
            cube2.draw(screen, CameraPosx)
            cube3.draw(screen, CameraPosx)
            cube4.draw(screen, CameraPosx)

            cube16.draw(screen, CameraPosx)
        if scene == 2:
            RespawnPos = (665, 320)
            playerObject.draw(screen, CameraPosx)
            cube6.draw(screen, CameraPosx)
            cube5.draw(screen, CameraPosx)
            cube7.draw(screen, CameraPosx)
            cube8.draw(screen, CameraPosx)
        if scene == 3:
            LevelGehaald()
            scene += 1
            player.lives = 5
        if scene == 4:
            RespawnPos = (-360, 100)
            playerObject.draw(screen, CameraPosx)
            cube9.draw(screen, CameraPosx)
            cube11.draw(screen, CameraPosx)
            cube12.draw(screen, CameraPosx)
            cube13.draw(screen, CameraPosx)
            cube14.draw(screen, CameraPosx)
            cube15.draw(screen, CameraPosx)




        draw_floor()

        playerObject.xspeed = speed * (keys["right"] - keys["left"])

        if playerObject.ypos >= 630 or Collider == "Death" or type(Collider) == MoveObject:
            playerObject.xpos, playerObject.ypos, player.lives, state = game_over(player.lives)
            (playerObject.xpos, playerObject.ypos) = RespawnPos
            if state == "Menu":
                return "Menu"

        if type(Collider) == enemy:
            return Collider


        (cube1.xpos, cube1.ypos) = cube1.Type.Move((cube1.xpos, cube1.ypos))
        (cube15.xpos, cube15.ypos) = cube15.Type.Move((int(cube15.xpos), int(cube15.ypos)))



        if L_border <= playerObject.xpos <= R_border:
            CameraPosx = playerObject.xpos - 500
        elif L_border >= playerObject.xpos:
            CameraPosx = L_border - 500
        elif playerObject.xpos >= R_border:
            CameraPosx = R_border - 500


        if L_border - 500 > playerObject.xpos and not scene  in [1, 4]:
            playerObject.xpos = R_border + 700
            CameraPosx = R_border - 500
            scene -= 1

        elif playerObject.xpos > R_border + 800:
            playerObject.xpos = L_border - 450
            CameraPosx = L_border - 500
            scene += 1

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