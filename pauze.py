import pygame
from button_code import *

state = 32832757342657832458324658734265234687342657834265873658234682346598234652
screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)

def Pause():
    WIDTH = 1366
    HEIGHT = 690
    mouseDown = False

    while True:
        mouse = pygame.mouse.get_pos()

        buttonResume = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "resume", 'white', 50,
                              'white')
        buttonMenu = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                            'white')
        if button.check(buttonResume, mouse, mouseDown, screen):
            return state
        if button.check(buttonMenu, mouse, mouseDown, screen):
            screen.fill('black')
            mouseDown = False
            return "Menu"
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            else:
                mouseDown = False