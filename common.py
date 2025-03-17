from pauze import *
from button_code import *
import pygame
import time

class character:
    def __init__(self, name, lives, colour, hitpoints, maxHitpoints, moveset, items):
        self.name = name
        self.lives = lives
        self.colour = colour
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.moveset = moveset
        self.items = items
class enemy:
    def __init__(self, name, colour, hitpoints, moveset):
        self.name = name
        self.colour = colour
        self.hitpoints = hitpoints
        self.moveset = moveset
WIDTH = 1366
HEIGHT = 690

def eind():
    return None

def textPrint(text, textSize, textColour, center):
    """
    Prints the text on the screen. center is tuple.
    :param text: What text will print
    :param textSize: How big is the text
    :param textColour: What color is the text
    :param center: location of center text
    :return: None
    """
    font = pygame.font.Font("freesansbold.ttf", textSize)
    text = font.render(text, True, textColour)
    textRect = text.get_rect()
    textRect.center = center
    screen.blit(text, textRect)

def game_over(lives, state=None):
    """
    Shows the Game Over screen
    :param lives: the amount of lives left of the player
    :param state : The state of the game
    :return: None
    """
    lives -= 1
    screen.fill('red')
    if lives == 0:
        textPrint("Game over", 100, 'white', (WIDTH/2, HEIGHT/2 - 100))
        state = "Menu"
        lives = 5
    else:
        textPrint("You died", 100, 'white', (WIDTH/2, HEIGHT/2))
        textPrint("You have " + str(lives) + " live(s) left", 40, 'white', (WIDTH / 2, HEIGHT / 2 + 100))
    pygame.display.flip()
    time.sleep(2)
    return 200, 200, lives, state


def menu():
    """
    Shows the menu screen
    :return the pressed button (Start, Quit, Tuturial?):
    """
    screen.fill('black')
    mouseDown = False
    buttonBegin = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "start", 'white', 50, 'white')
    buttonQuit = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "quit", 'white', 50,'white')
    while True:
        textPrint("Titanic Escape", 100, 'white', (WIDTH / 2, HEIGHT / 4))
        mouse = pygame.mouse.get_pos()
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.QUIT:
                return "quit"
        if button.check(buttonBegin, mouse, mouseDown, screen):
            return "begin"
        if button.check(buttonQuit, mouse, mouseDown, screen):
            return "quit"
def LevelGehaald():

        """
        Shows the level complete screen and moves on to the next level
        :return none:
        """

        screen.fill((0, 0, 0))
        textPrint("Level gehaald", 100, 'white', (WIDTH / 2, HEIGHT / 4))
        textPrint("alle levens zijn hersteld", 100, 'white', (WIDTH / 2, HEIGHT / 4 + 300))
        pygame.display.update()
        time.sleep(3)




