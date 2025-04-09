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
logo = pygame.image.load('resources/textures/logo.png')
pygame.display.set_caption("Titanic escape")
pygame.display.set_icon(logo)
mainFont = 'resources/MinecraftTen-VGORe.ttf'
punch = move("punch", "Hits the opponent \n for 10 damage","")
comboPunch = move("combo punch", "Hits the opponent a \n random number of times","")
enrage = move("enrage", "Increases your damage on \n the next 3 turns",'')
poison = move("poison", "Poisons your opponent to \n take damage over time",'')
lifeSteal = move("life steal", "Damages your opponent \n and gives you 30% \n back as health",'')
block = move("block", "Blocks your opponents' \n next attack",'')
player = character("bob", 5, pygame.transform.scale(pygame.image.load('resources/textures/rat_idle.png'), (200, 80)), 100, 100, [punch, comboPunch], [
    item("Full Restore", 2),
    item("Bomb", 5),
    item("Poison bottle", 0),
    item("Immunizing elixir", 0),
    item("Giantkiller", 2),
    item("Orb of absorption", 2)
], 5, True)





while running:
    if state == "Menu":
        screen.fill('black')
        game_manager.Set(25, -450, 450)
        player.lives, player.hitpoints, items = (5, 100, [])
        state, player.name = menu(player.name)

    # Hoofd code:
    elif state == "Playing":
        state = parkour(player, game_manager)
        if type(state) == character:
            encounter = state
            result, player.hitpoints, player.items = fight(encounter, player, screen)
            if result == "loss":
                player.lives, state = game_over(player.lives)
                player.hitpoints = player.maxHitpoints
                if state is None:
                    state = "Playing"
            elif result == "win":
                encounter.alive = False
                allMovesList = [punch, comboPunch, enrage, poison, lifeSteal, block]
                newMove = chooseNewAttack(allMovesList, player)
                if newMove is not None:
                    if newMove != "Menu":
                        player.moveset.append(newMove)
                        state = "Playing"
                    else:
                        state = newMove
                else:
                    state = "Playing"
            else:
                state = result
            playerObject.xpos += 120

    elif state == "quit":
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()