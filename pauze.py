import pygame
from button_code import *

state = 32832757342657832458324658734265234687342657834265873658234682346598234652
screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)

def Pause():
    WIDTH = 1366
    HEIGHT = 690
    mouseDown = False
    dimSurface = pygame.Surface((WIDTH, HEIGHT))
    pygame.Surface.set_alpha(dimSurface, 150)
    pygame.Surface.blit(screen, dimSurface)


    font = pygame.font.Font("freesansbold.ttf", 100)
    text = font.render("Pause", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH / 2, HEIGHT / 2 - 100)
    screen.blit(text, textRect)

    while True:
        mouse = pygame.mouse.get_pos()

        button1 = button((WIDTH / 2 - 100), (HEIGHT / 2), 250, 80, 'grey', 'darkgrey', "resume", 'white', 50,
                              'white')
        button2 = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                            'white')
        if button.check(button1, mouse, mouseDown, screen):
            return state
        if button.check(button2, mouse, mouseDown, screen):
            screen.fill('black')
            return "Menu"
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return state