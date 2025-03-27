import pygame
import math
from button_code import *
from firework_function import *

screen = pygame.display.set_mode((1366, 668), pygame.RESIZABLE)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.font.init()


def textOutline(text, textSize, textColour, outlineColour, outlineThickness, center):
    textPrint(text, textSize, outlineColour, (center[0] - outlineThickness, center[1] - outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] - outlineThickness, center[1] + outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] + outlineThickness, center[1] - outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] + outlineThickness, center[1] + outlineThickness))
    textPrint(text, textSize, textColour, center)

pygame.draw.line(screen, 'white', (12.31, 32.9), (-238, 33.4))

textOutline("yippeee", 120, 'black', 'white', 2, (WIDTH/2, HEIGHT/2))
pygame.display.flip()
alpha = 0
while True:
    pygame.draw.arc(screen, 'red', pygame.Rect(100, 100, 200, 200), 0, alpha , 5)
    alpha += 6 * math.pi / 180
    pygame.display.flip()
    time.sleep(0.1)
    break
screen.fill('black')
fireworkWord("Thanks for playing", 100)

