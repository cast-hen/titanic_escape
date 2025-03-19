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


def textPrint(text, textSize, textColour, center):
    """
    Prints the text on the screen.
    text: string of text you want to display
    textSize: the size of the text
    textColour: the colour of the text
    center: the center position of where the text should be placed
    return: none
    """
    font = pygame.font.Font("freesansbold.ttf", textSize)
    text = font.render(text, True, textColour)
    textRect = text.get_rect()
    textRect.center = center
    screen.blit(text, textRect)

def game_over(lives, state=None):
    """
    Function for if the player has died
    lives: the ammount of lives the player has left
    state: the current state of the FSM
    return: the new ammount of lives and the new state of the FSM
    """
    lives -= 1
    screen.fill('red')
    if lives == 0:
        lives = 5
        yesButton = button((WIDTH / 2 - 250), (2.5*HEIGHT/4), 200, 80, 'grey', 'darkgrey', "YES", 'white', 50,
                              'white')
        noButton = button((WIDTH / 2 + 50), (2.5*HEIGHT/4), 200, 80, 'grey', 'darkgrey', "NO", 'white', 50,
                            'white')
        while True:
            textPrint("Game over", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
            textPrint("Play again?", 60, 'white', (WIDTH / 2, HEIGHT / 2))

            mouse = pygame.mouse.get_pos()
            mouseDown = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
            if button.check(yesButton, mouseDown, screen):
                break
            if button.check(noButton, mouseDown, screen):
                state = "Menu"
                break
    else:
        textPrint("You died", 100, 'white', (WIDTH/2, HEIGHT/2))
        if lives == 1:
            textPrint("You have " + str(lives) + " live left", 40, 'white', (WIDTH / 2, HEIGHT / 2 + 100))
        else:
            textPrint("You have " + str(lives) + " lives left", 40, 'white', (WIDTH / 2, HEIGHT / 2 + 100))
        pygame.display.flip()
        time.sleep(2)
    return 200, 200, lives, state


def menu():
    """
    the opening menu of the game
    return: the action the player has made within the menu as a string
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
        if button.check(buttonBegin, mouseDown, screen):
            return "begin"
        if button.check(buttonQuit, mouseDown, screen):
            return "quit"


def LevelGehaald(screen):
    screen.fill('green')
    menuButton = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.5), 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                        'white')
    while True:
        textPrint("You won!!", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
        textPrint("Berend Sulman, Branko Opdam", 40, 'white',
                  (WIDTH / 2, HEIGHT / 2 - 20))
        textPrint("Maarten van Ammers & Stijn Zwart", 40, 'white',
                  (WIDTH / 2, HEIGHT / 2 + 50))
        mouse = pygame.mouse.get_pos()
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
        if button.check(menuButton, mouseDown, screen):
            return "Menu"
