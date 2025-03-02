from parkour_functies import *
from button_code import *
import pygame
from pygame import RESIZABLE, Surface
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
        buttonTitle = button((WIDTH / 2 - 400), (HEIGHT / 6), 800, 160, 'grey', 'grey', "Titanic Escape", 'white',100, 'white')
        buttonStart = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "start", 'white', 50,'white')
        buttonQuit = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "quit", 'white', 50,'white')
        button.check(buttonTitle, mouse, mouseDown, screen)
        if button.check(buttonStart, mouse, mouseDown, screen):
            scene = "scene1"
        if button.check(buttonQuit, mouse, mouseDown, screen):
            running = False

    elif scene == "pause":
        buttonResume = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "resume", 'white', 50,'white')
        buttonMenu = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,'white')
        if button.check(buttonResume, mouse, mouseDown, screen):
            scene = "scene1"
        if button.check(buttonMenu, mouse, mouseDown, screen):
            scene = "main_menu"
            screen.fill('black')
            mouseDown = False

    elif scene == "scene1":
        clock.tick(fps)
        screen.fill((135, 206, 250))
        draw_floor()
        player.update_pos(platforms, CameraPosx=0)
        player.draw(screen, CameraPosx=0)
        cube1.draw(screen, CameraPosx=0)
        cube2.draw(screen, CameraPosx=0)
        cube3.draw(screen, CameraPosx=0)
        cube4.draw(screen, CameraPosx=0)
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
            elif event.key == pygame.K_ESCAPE and scene == "scene1":
                scene = "pause"
                dimSurface = pygame.Surface((WIDTH, HEIGHT))
                pygame.Surface.set_alpha(dimSurface, 150)
                pygame.Surface.blit(screen, dimSurface)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                keys["right"] = False
            elif event.key == pygame.K_a:
                keys["left"] = False

    pygame.display.flip()

pygame.quit()