from parkour_functies import *
import pygame
from pygame import RESIZABLE
import time

pygame.init()

#global variables
WIDTH = 1366
HEIGHT = 690
font = pygame.font.Font("freesansbold.ttf", 100)
text = font.render("you ded", True, 'black')
textRect = text.get_rect()
textRect.center = (WIDTH/2, HEIGHT/2)
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
clock = pygame.time.Clock()
fps = 60
gravity = 0.6
jump_height = -25
speed = 10
running = True
scene = "main_menu"
mouseDown = False
keys = {"left": False, "right": False}

#objects
player = Objects(1000, 450, 50, 50, 'green', 2, 0, 0)
cube1 = Objects(580, 400, 60, 60, 'black', 1, 0, 0)
cube2 = Objects(690, 546, 600, 40, 'black', 1, 0, 0)
cube3 = Objects(0, 300, 400, 60, 'black', 1, 0, 0)
cube4 = Objects(600, 100, 80, 80, 'orange', 1, 0, 0)

#voeg hier nieuwe platformen to zodat ze collision krijgen.
platforms = [cube1, cube2, cube3, cube4]

#game loop
while running:
    mouse = pygame.mouse.get_pos()

    if scene == "main_menu":
        scene   = "scene1"

    elif scene == "scene1":
        clock.tick(fps)
        screen.fill((135, 206, 250))
        draw_floor()
        player.update_pos(platforms)
        player.draw(screen)
        cube1.draw(screen)
        cube2.draw(screen)
        cube3.draw(screen)
        cube4.draw(screen)
        player.xspeed = speed * (keys["right"] - keys["left"])

    if player.ypos >= 630:
        screen.fill((255, 0, 0))
        screen.blit(text, textRect)
        player.ypos = 450
        player.xpos = 1000
        pygame.display.flip()
        time.sleep(2)

#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        #movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                keys["right"] = True
            elif event.key == pygame.K_a:
                keys["left"] = True
            elif event.key == pygame.K_w and player.on_ground:
                player.yspeed = jump_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                keys["right"] = False
            elif event.key == pygame.K_a:
                keys["left"] = False

    pygame.display.flip()

pygame.quit()