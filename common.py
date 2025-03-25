from pauze import *
from button_code import *
from firework_function import *
import pygame
import time
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()

class character:
    def __init__(self, name, lives, colour, hitpoints, maxHitpoints, moveset, items, heals):
        self.name = name
        self.lives = lives
        self.colour = colour
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.moveset = moveset
        self.items = items
        self.heals = heals

    def displayInfo(self):
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


class enemy:
    def __init__(self, name, colour, hitpoints, moveset, heals):
        self.name = name
        self.colour = colour
        self.hitpoints = hitpoints
        self.moveset = moveset
        self.heals = heals


def waitForInput(buttonList, keyEscape=None, buttonInfo=None):
    """
    Waits for input of the player in the form of pressing a button.
    :param buttonList: The buttons that are checked
    :param keyEscape: True if using the escape button is possible
    :param buttonInfo: If possible to type, tuple with (buttonToType, startText, textCenter, textSize)
    :return the index of the pressed button
    """
    typing = False
    if buttonInfo is not None:
        buttonToType, text, textCenter, textSize = buttonInfo
        font = pygame.font.Font("freesansbold.ttf", textSize)
    while True:
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and keyEscape is not None:
                    if buttonInfo is None:
                        return -1
                    else:
                        return -1, text

                if event.key == pygame.K_BACKSPACE and typing:
                    textPrint(text, textSize, 'black', textCenter, True)
                    text = text[:-1]
                    textPrint(text, textSize, 'white', textCenter)
                elif event.key == pygame.K_RETURN and typing:
                    typing = False
            elif event.type == pygame.TEXTINPUT and typing:
                textPrint(text, textSize, 'black', textCenter, True)
                if len(text) <= 10:
                    text += event.text
                    textPrint(text, textSize, 'white', textCenter)
                else:
                    textPrint("Too long!", textSize, 'red', textCenter)
                    pygame.display.flip()
                    time.sleep(1)
                    textPrint("Too long!", textSize, 'black', textCenter, True)
                    textPrint(text, textSize, 'white', textCenter)
                    break
        for i in range(len(buttonList)):
            if button.check(buttonList[i], mouseDown, screen):
                if buttonInfo is None:
                    return i
                else:
                    return i, text

        if buttonInfo is not None:
            if button.check(buttonToType, mouseDown, screen):
                typing = True
        pygame.display.flip()




def menu(name):
    """
    Shows the menu screen
    :return the pressed button (Start, Quit)
    """
    screen.fill('black')
    buttonBegin = button(WIDTH / 2 - 100, HEIGHT / 2, 200, 80, 'grey', 'darkgrey', "start", 'white', 50, 'white')
    buttonQuit = button(WIDTH / 2 - 100, HEIGHT / 2 + 125, 200, 80, 'grey', 'darkgrey', "quit", 'white', 50,'white')
    buttonName = button(WIDTH / 5 - 80, HEIGHT / 2 + 40, 160, 60, 'black', (40, 40, 40), "Change name", 'white', 20, 'black')
    textPrint("Titanic Escape", 100, 'white', (WIDTH / 2, HEIGHT // 4))
    textPrint(name, 40, 'white', (WIDTH / 5, HEIGHT / 2))

    index, name = waitForInput([buttonBegin, buttonQuit], buttonInfo=(buttonName, name, (WIDTH // 5, HEIGHT // 2), 40))
    possibleStates = ["begin", "quit"]
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
        possibleStates = ["begin", "Menu"]
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


def eind():
    """
    Shows the credit screen and waits until the menu button is pressed.
    :return none:
    """
    fireworkWord("Thanks for playing", 120)
    screen.fill('green')
    buttonMenu = button(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                        'white')
    textPrint("You won!!", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
    textPrint("Berend Sulman, Branko Opdam,", 40, 'white',
              (WIDTH / 2, HEIGHT / 2 - 20))
    textPrint("Maarten van Ammers & Stijn Zwart", 40, 'white',
              (WIDTH / 2, HEIGHT / 2 + 50))

    index = waitForInput([buttonMenu])
    possibleStates = ["Menu"]
    return possibleStates[index]


def Afstand(pos1, pos2):
    x_afstand = pos2[0] - pos1[0]
    y_afstand = pos2[1] - pos1[1]
    if x_afstand < 0:
        x_afstand *= -1
    if y_afstand < 0:
        y_afstand *= -1

    return (x_afstand ** 2 + y_afstand ** 2) **0.5