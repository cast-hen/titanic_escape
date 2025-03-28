from button_code import *
from firework_function import *
import pygame
import time
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()

class character:
    def __init__(self, name, lives, colour, hitpoints, maxHitpoints, moveset, items, heals):
        """
        Initializes a character with attributes like name, lives, health, moves, and items.

        :param name: The name of the character.
        :param lives: The number of lives the character has.
        :param colour: The color associated with the character.
        :param hitpoints: The current health points of the character.
        :param maxHitpoints: The maximum health points the character can have.
        :param moveset: The set of moves the character can perform.
        :param items: The list of items the character possesses.
        :param heals: The number of healing items the character has.
        """
        self.name = name
        self.lives = lives
        self.colour = colour
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.moveset = moveset
        self.items = items
        self.heals = heals

    def displayInfo(self):
        """
        Displays information about the object.
        """
        pygame.draw.rect(screen, (0, 0, 0, 50), pygame.Rect(20, 65, 210, 60))
        pygame.draw.rect(screen, (255, 0, 0, 50), pygame.Rect(25, 70, 200 * (self.hitpoints / self.maxHitpoints), 50))
        textPrint(str(self.hitpoints), 40, 'white', (125, 95))
        textPrint(self.name, 40, 'black', (125, 45))

        lifeImage = pygame.transform.scale(pygame.image.load("resources/textures/life.png"), (38,38))
        nolifeImage = pygame.transform.scale(pygame.image.load("resources/textures/nolife.png"), (38, 38))
        for i in range(5):
            if self.lives >= i + 1:
                screen.blit(lifeImage, (20 + 43 * i, 140))
            else:
                screen.blit(nolifeImage, (20 + 43 * i, 140))


def menu(name):
    """
    Shows the menu screen
    :return the pressed button (Start, Quit)
    """
    screen.fill('black')
    buttonPlaying = button(WIDTH / 2 - 100, HEIGHT / 2, 200, 80, 'grey', 'darkgrey', "start", 'white', 50, 'white')
    buttonQuit = button(WIDTH / 2 - 100, HEIGHT / 2 + 125, 200, 80, 'grey', 'darkgrey', "quit", 'white', 50,'white')
    buttonName = button(WIDTH / 5 - 80, HEIGHT / 2 + 40, 160, 60, 'black', (40, 40, 40), "Change name", 'white', 20, 'black')
    textPrint("Titanic Escape", 100, 'white', (WIDTH / 2, HEIGHT // 4))
    textPrint(name, 40, 'white', (WIDTH / 5, HEIGHT / 2))

    index, name = waitForInput([buttonPlaying, buttonQuit], typeInfo=(buttonName, name, (WIDTH // 5, HEIGHT // 2), 40))
    possibleStates = ["Playing", "quit"]
    return possibleStates[index], name



def Pause():
    """
    Pauses the game until the player selects an option
    :return the state the player should now be in
    """
    buttonResume = button(WIDTH / 2 - 100, HEIGHT / 2, 200, 80, 'grey', 'darkgrey', "resume", 'white', 50,'white')
    buttonMenu = button(WIDTH / 2 - 100, HEIGHT / 2 + 125, 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,'white')
    dimSurface = pygame.Surface((WIDTH, HEIGHT))
    pygame.Surface.set_alpha(dimSurface, 150)
    pygame.Surface.blit(screen, dimSurface)
    textPrint("Pause", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))

    index = waitForInput([buttonResume, buttonMenu], True)
    possibleStates = [None, "Menu", None]
    return possibleStates[index]


def game_over(lives, state=None):
    """
    Shows the Game Over screen
    :param lives: the amount of lives left of the player
    :param state : The state of the game
    :return: lives, state
    """
    lives -= 1
    screen.fill('red')
    if lives == 0:
        textPrint("Game over", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
        textPrint("Play again?", 50, 'white', (WIDTH / 2, HEIGHT / 2))
        buttonYes = button(WIDTH / 2 - 150, HEIGHT / 2 + 50, 125, 75, 'grey', 'darkgrey', "YES", 'white', 40, 'white')
        buttonNo = button(WIDTH / 2 + 25, HEIGHT / 2 + 50, 125, 75, 'grey', 'darkgrey', "NO", 'white', 40, 'white')

        index = waitForInput([buttonYes, buttonNo])
        possibleStates = ["Playing", "Menu"]
        state = possibleStates[index]
        lives = 5
    else:
        textPrint("You died", 100, 'white', (WIDTH / 2, HEIGHT / 2))
        message = "You have " + str(lives) + " lives left"
        if lives == 1:
            message = message[:-8] + "fe left"
        textPrint(message, 40, 'white', (WIDTH / 2, HEIGHT / 2 + 100))
        pygame.display.flip()
        time.sleep(2)
    return lives, state


def LevelGehaald():
    """
    Shows the level complete screen and moves on to the next level
    :return none:
    """
    screen.fill((0, 0, 0))
    textPrint("Level gehaald", 100, 'white', (WIDTH / 2, HEIGHT // 4))
    textPrint("alle levens zijn hersteld", 100, 'white', (WIDTH / 2, HEIGHT // 4 + 300))
    pygame.display.update()
    time.sleep(3)


def eind(name):
    """
    Shows the credit screen and waits until the menu button is pressed.
    :return possibleStates[index]:
    """
    screen.fill('black')
    fireworkWord("Thanks for playing", 120)
    buttonMenu = button(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                        'white')
    textPrint(name, 100, 'white', (WIDTH / 2, HEIGHT / 2 - 220))
    textPrint("escaped the Titanic", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
    textPrint("Berend Sulman, Branko Opdam,", 40, 'white',
              (WIDTH / 2, HEIGHT / 2 - 20))
    textPrint("Maarten van Ammers & Stijn Zwart", 40, 'white',
              (WIDTH / 2, HEIGHT / 2 + 50))

    index = waitForInput([buttonMenu])
    possibleStates = ["Menu"]
    return possibleStates[index]


def Afstand(pos1, pos2):
    """
    Calculates the absolute distance between two positions.

    :param pos1: The first position as a tuple (x, y).
    :param pos2: The second position as a tuple (x, y).
    :return: The absolute x and y distance as a tuple.
    """
    x_afstand = pos2[0] - pos1[0]
    y_afstand = pos2[1] - pos1[1]
    if x_afstand < 0:
        x_afstand *= -1
    if y_afstand < 0:
        y_afstand *= -1

    return (x_afstand ** 2 + y_afstand ** 2) **0.5