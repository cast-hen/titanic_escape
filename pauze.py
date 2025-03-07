import pygame
from button_code import *
from common import *


screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)

def Pause():
    WIDTH = 1366
    HEIGHT = 690
    mouseDown = False
    dimSurface = pygame.Surface((WIDTH, HEIGHT))
    pygame.Surface.set_alpha(dimSurface, 150)
    pygame.Surface.blit(screen, dimSurface)

    textPrint("Pause", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))

    while True:
        mouse = pygame.mouse.get_pos()

        button1 = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "resume", 'white', 50,
                              'white')
        button2 = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                            'white')
        if button.check(button1, mouse, mouseDown, screen):
            return None
        if button.check(button2, mouse, mouseDown, screen):
            screen.fill('black')
            return "Menu"
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None