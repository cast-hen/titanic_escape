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

screen.fill('black')
fireworkWord("Thanks for playing", 100)


def displayInfo(self):
    """
    Displays the info of the character on screen. Info consist of name, hitpoints and lives.
    :return Nothing
    """
    infoSurface = pygame.Surface((230, 200), pygame.SRCALPHA)
    infoSurface.set_alpha(200)
    pygame.draw.rect(infoSurface, 'black', pygame.Rect(20, 65, 210, 60))
    pygame.draw.rect(infoSurface, 'red', pygame.Rect(25, 70, 200 * (self.hitpoints / self.maxHitpoints), 50))

    lifeImage = pygame.transform.scale(pygame.image.load("resources/textures/life.png"), (38, 38))
    nolifeImage = pygame.transform.scale(pygame.image.load("resources/textures/life_empty.png"), (38, 38))
    for i in range(5):
        if self.lives >= i + 1:
            infoSurface.blit(lifeImage, (20 + 43 * i, 140))
        else:
            infoSurface.blit(nolifeImage, (20 + 43 * i, 140))
    screen.blit(infoSurface)

    textPrint(str(self.hitpoints), 40, 'white', (125, 95))
    # Gives the name a white outline
    center = (125, 45)
    textPrint(self.name, 40, 'white', (center[0] - 2, center[1] - 2))
    textPrint(self.name, 40, 'white', (center[0] - 2, center[1] + 2))
    textPrint(self.name, 40, 'white', (center[0] + 2, center[1] - 2))
    textPrint(self.name, 40, 'white', (center[0] + 2, center[1] + 2))
    textPrint(self.name, 40, 'black', center)
