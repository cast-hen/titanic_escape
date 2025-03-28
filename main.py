from fighting_functions import *
from parkour_functies import *
from button_code import *
from common import *
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
running = True
state = "Menu"

punch = move("punch", "Hits the opponent \n for 10 damage","")
comboPunch = move("combo punch", "Hits the opponent a \n random number of times","")
enrage = move("enrage", "Increases your damage on \n the next 3 turns",'')
poison = move("poison", "poisons your opponent to \n take damage over time",'')
lifeSteal = move("life steal", "Damages your opponent \n and gives you 30% \n back as health",'')
block = move("block", "Blocks your opponents \n next attack",'')
allMovesList = [punch, comboPunch, enrage, poison, lifeSteal, block]
player = character("bob", 5, (0, 255, 0), 100, 100, [punch, comboPunch], [], 5)


while running:
    if state == "Menu":
        screen.fill('black')
        player.lives, player.hitpoints, items = (5, 100, [])
        state, player.name = menu(player.name)

    # Hoofd code:
    elif state == "Playing":
        state = parkour(player)
        if type(state) == character:
            encounter = state
            result, player.hitpoints = fight(encounter, player, screen)
            if result == "loss":
                player.lives, state = game_over(player.lives)
                player.hitpoints = player.maxHitpoints
                if state is None:
                    state = "Playing"
                    playerObject.xpos += 120
            elif result == "win":
                newMove = chooseNewAttack(allMovesList, player)
                if newMove != "Menu":
                    if newMove is not None:
                        player.moveset.append(newMove)
                    state = "Playing"
                    playerObject.xpos += 120
                else:
                    state = newMove
            else:
                state = result
                playerObject.xpos += 120

    elif state == "quit":
        running = False

pygame.quit()