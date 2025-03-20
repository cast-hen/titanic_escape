import pygame

import common
from button_code import *
from common import textPrint

state = 32832757342657832458324658734265234687342657834265873658234682346598234652
screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)

def Pause():
    """
    Pauses the game until the player selects an option
    return: the state the player should now be in
    """
    WIDTH = 1366
    HEIGHT = 690
    resumeButton = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "resume", 'white', 50,
                          'white')
    menuButton = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                        'white')
    dimSurface = pygame.Surface((WIDTH, HEIGHT))
    pygame.Surface.set_alpha(dimSurface, 150)
    pygame.Surface.blit(screen, dimSurface)

    while True:
        textPrint("Pause", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return state
        if button.check(resumeButton, mouseDown, screen):
            return state
        if button.check(menuButton, mouseDown, screen):
            return "Menu"