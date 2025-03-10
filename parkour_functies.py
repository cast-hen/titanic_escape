from pauze import *
from common import *
import pygame
from pygame import RESIZABLE
import time
import time
WIDTH = 1366
HEIGHT = 690
gravity = 0.6
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)



class Objects:
    def __init__(self, xpos, ypos, width, height, color, mass, xspeed, yspeed, ObjectScene):
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

    def update_pos(self, platforms, CameraPosx, scene):


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
                    return platform.color == "orange"

        # wall en floor collision
        if self.ypos + self.height >= HEIGHT - 4:
            self.ypos = HEIGHT - self.height - 4
            self.yspeed = 0
            self.on_ground = True
            self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
        if self.xpos + self.width > WIDTH:
            self.xpos = WIDTH - self.width
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)

    def draw(self, surface, CameraPosx):
        self.Rect = pygame.draw.rect(surface, self.color, (self.xpos - CameraPosx, self.ypos, self.width, self.height))


# maakt vloer
def draw_floor():
    pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 25)

def parkour(player):
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

    playerObject = Objects(300, 200, 50, 50, 'green', 2, 0, 0, 1)
    cube1 = Objects(580, 400, 60, 60, 'black', 1, 0, 0, 1)
    cube2 = Objects(690, 546, 600, 40, 'black', 1, 0, 0, 1)
    cube3 = Objects(-800, 546, 1200, 60, 'black', 1, 0, 0, 1)
    cube4 = Objects(800, 300, 80, 80, 'orange', 1, 0, 0, 1)
    cube5 = Objects(630, 374, 80, 80, 'black', 1, 0, 0, 2)
    cube7 = Objects(970, 320, 80, 80, 'black', 1, 0, 0, 2)
    cube8 = Objects(1200, 180, 80, 80, 'black', 1, 0, 0, 2)
    cube6 = Objects(-800, 546, 1200, 60, 'black', 1, 0, 0, 2)
    cube9 = Objects(-500, 546, 5000, 40, 'black', 1, 0, 0, 4)

    # voeg hier nieuwe platformen to zodat ze collision krijgen.
    platforms = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9]

    # random ahhh movement fix, couldn't bother om een betere oplossig te vinden.
    keys = {"left": False, "right": False}
    EnemyCollider = False

    L_border = 0
    R_border = 500

    # game loop
    while running:
        mouse = pygame.mouse.get_pos()
        clock.tick(fps)
        screen.fill((135, 206, 250))
        EnemyCollider = playerObject.update_pos(platforms, CameraPosx, scene)


        if scene == 1:
            RespawnPos = (200, 300)
            playerObject.draw(screen, CameraPosx)
            cube1.draw(screen, CameraPosx)
            cube2.draw(screen, CameraPosx)
            cube3.draw(screen, CameraPosx)
            cube4.draw(screen, CameraPosx)
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
            RespawnPos = (-360, 500)
            playerObject.draw(screen, CameraPosx)
            cube9.draw(screen, CameraPosx)



        draw_floor()

        playerObject.xspeed = speed * (keys["right"] - keys["left"])

        if playerObject.ypos >= 630:
            playerObject.xpos, playerObject.ypos, player.lives, state = game_over(player.lives)
            (playerObject.xpos, playerObject.ypos) = RespawnPos
            if state == "Menu":
                return "Menu"

        if EnemyCollider:
            return enemy("greg", (255, 0, 0), 50, ["punch"])
        if L_border <= playerObject.xpos <= R_border:
            CameraPosx = playerObject.xpos - 500


        elif L_border - 500 > playerObject.xpos and not scene  in [1, 4]:
            playerObject.xpos = R_border + 700
            CameraPosx = R_border - 500
            scene -= 1

        elif playerObject.xpos > R_border + 750:
            playerObject.xpos = L_border - 450
            CameraPosx = L_border - 500
            scene += 1

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                print(mouse[0] + CameraPosx, mouse[1])
            # movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keys["right"] = True
                elif event.key == pygame.K_a:
                    keys["left"] = True
                elif event.key == pygame.K_w and playerObject.on_ground:
                    playerObject.yspeed = jump_height

                elif event.key == pygame.K_ESCAPE:
                    if Pause() == "Menu":
                        return "Menu"
                    else:
                        keys = {"left": False, "right": False}
                    screen.fill((0, 0, 0))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keys["right"] = False
                elif event.key == pygame.K_a:
                    keys["left"] = False

        pygame.display.flip()