import pygame
import random
from button_code import *

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

class move:
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

    def __str__(self):
        return f"{self.name}"

    def displayMove(self, x, y):
        """
        Displays a card with a move and its description
        :param x: horizontal position of the center of the card
        :param y: vertical position of the center of the card
        :return: nothing
        """
        # Tekent het plaatje als er voor die move een is
        if not self.image == "":
            screen.blit(self.image, (x, y))
        # Print de tekst op de kaart
        textPrint(self.description, 20, 'white', (x, y + 150))
        textPrint(self.name, 35, 'white', (x, y - 200))

punch = move("punch", "Hits the opponent \n for 10 damage","")
comboPunch = move("combo punch", "Hits the opponent a \n random number of times","")
enrage = move("enrage", "Increases your damage on \n the next 3 turns",'')
poison = move("poison", "poisons your opponent to \n take damage over time",'')
lifeSteal = move("life steal", "Damages your opponent \n and gives you 30% \n back as health",'')
block = move("block", "Blocks your opponents \n next attack",'')
player = character("bob", 5, (0, 255, 0), 100, 100, [punch, comboPunch], [], 5)
allMovesList = [punch, comboPunch, enrage, poison, lifeSteal, block]

def chooseNewAttack(allMovesList, player):
    """
    Displays 3 moves the player can choose from to add to their deck
    player: the player character
    :return: the chosen move or the new state
    """
    allMoves = allMovesList
    if len(allMoves) != len(player.moveset):
        options = []
        for i in range(3):
            selected = False
            while not selected:
                selected = True
                move = random.randint(0, len(allMoves) - 1)
                for i in range(len(player.moveset)):
                    if allMoves[move] == player.moveset[i]:
                        selected = False
                if selected:
                    options.append(allMoves[move])
                    allMoves.pop(move)
                elif len(allMoves) == len(player.moveset):
                    selected = True
        screen.fill((100, 100, 100))
        buttonList = []
        width = screen.get_width()
        height = screen.get_height()
        for i in range(len(options)):
            options[i].displayMove(width/2 + 328 * (i - 1), height/2 - 50)
            buttonList.append(button(width/2 + 328 * (i - 1) - 105, 590, 210, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white'))
        # Loop waarin gekeken wordt welke knop wordt ingedrukt
        while True:
            index = waitForInput(buttonList, True)
            if index == -1:
                if Pause() == "Menu":
                    return "Menu"
            else:
                return options[index]
    else:
        return None

screen = pygame.display.set_mode((1300, 600), pygame.FULLSCREEN)
running = True

pygame.init()
while running:
    screen.fill((0, 0, 0))
    pygame.display.update()
    time.sleep(1)
    for i in range(len(player.moveset)):
        print(player.moveset[i])
    print("yay")
    newMove = chooseNewAttack(allMovesList, player)
    if newMove is not None:
        player.moveset.append(newMove)