from pauze import *
from fighting_functions import *
from parkour_functies import *
from button_code import *
from common import *
import pygame
import time
import random

screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)
running = True
pygame.init()
punch = move("punch", "Hits the opponent for 10 damage", "")
comboPunch = move("combo punch", "Hits the opponent a random number of times", "")
enrage = move("enrage", "Increases your damage on the next 3 turns", "")
poison = move("poison", "poisons your opponent to take damage over time", "")
lifeSteal = move("life steal", "Damages your opponent and gives you 30% back as health", "")
block = move("block", "Blocks your opponents next attack", "")
movesList = [punch, comboPunch, enrage, poison, lifeSteal, block]
player = player("bob", 5, (0, 255, 0), 100, 100, [punch, comboPunch], [])
WIDTH = 1366
HEIGHT = 690
state = "Menu"

while running:
    if state == "Menu":
        state = menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hoofd code:
    if state == "begin":
        encounter = parkour()
        if encounter == "Menu":
            state = "Menu"
        elif encounter == "quit":
            running = False

        else:
            result = fight(encounter, player, screen)
            player.hitpoints = result[1]
            if result[0] == "quit":
                running = False
            elif result[0] == "loss":
                game_over()
            elif result[0] == "win":
                player.moveset.append(chooseNewAttack([enrage, lifeSteal, block]))
    if state == "quit":
        running = False

    pygame.display.update()

pygame.quit()