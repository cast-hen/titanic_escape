from pauze import *
from fighting_functions import *
from parkour_functies import *
from button_code import *
from common import *
import pygame
import time

screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
running = True
pygame.init()
punch = move("punch", "Hits the opponent for 10 damage", "")
comboPunch = move("combo punch", "Hits the opponent a \n random number of times", "")
enrage = move("enrage", "Increases your damage on \n the next 3 turns", "")
poison = move("poison", "poisons your opponent to \n take damage over time", "")
lifeSteal = move("life steal", "Damages your opponent \n and gives you 30% back \n as health", "")
block = move("block", "Blocks your opponents \n next attack", "")
movesList = [punch, comboPunch, enrage, poison, lifeSteal, block]
player = character("bob", 5, (0, 255, 0), 100, 100, [punch, comboPunch], [], 5)

state = "Menu"


while running:
    if state == "Menu":
        screen.fill('black')
        state = menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hoofd code:
    if state == "begin":
        player.lives, player.hitpoints, items = (5, 100, [])
        state = parkour(player)
        if type(state) == enemy:
            encounter = state
            result, player.hitpoints = fight(encounter, player, screen)
            if result == "loss":
                gameOverList = game_over(player.lives)
                player.lives = gameOverList[2]
                state = gameOverList[3]
                player.hitpoints = 100
            elif result == "win":
                nieuweAanval = chooseNewAttack([enrage, lifeSteal, block])
                if type(nieuweAanval) == move:
                    player.moveset.append(nieuweAanval)
                    state = "begin"
                else:
                    state = nieuweAanval
            else:
                state = result
    if state == "quit":
        running = False


    pygame.display.update()

pygame.quit()