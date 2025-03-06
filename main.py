from pauze import *
from fighting_functions import *
from parkour_functies import *
from button_code import *
from player_functies import *
from common import *
import pygame
import time
import random

screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)
running = True
pygame.init()
Aanvallen = ["Slaan", "Genezen"]
punch = move("punch", "Hits the opponent for 10 damage")
comboPunch = move("combo punch", "Hits the opponent a random number of times")
enrage = move("enrage", "Increases your damage on the next 3 turns")
poison = move("poison", "poisons your opponent to take damage over time")
lifeSteal = move("life steal", "Damages your opponent and gives you 30% back as health")
block = move("block", "Blocks your opponents next attack")
player = player("bob", 5, (0, 255, 0), 100, 100, [punch, comboPunch], [])
WIDTH = 1366
HEIGHT = 690

"""
A_Bom = Aanval(pygame.transform.scale(pygame.image.load("resources/textures/Bom.png"), (200, 200)), "Bom",
               "Valt elke vijand aan voor 5 schade", 5, 5)
A_Zwaardslag = Aanval("", "Zwaard", "Valt 1 vijand aan voor 10 schade", 10, 0)
A_Genezen = Aanval("", "Genezen", "Genees 10 levens", 0, 10)
A_Blokkeren = Aanval("", "Blokkeren", "Blokkeer 80% van de schade", 0, 0)
"""
state = "Menu"

while running:
    if state == "Menu":
        state = menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hoofd code:
    if state == "Begin":
        Encounter = parkour()
        if Encounter == "Menu":
            state = "Menu"

        else:
            result = fight(Encounter, player, screen)
            player.hitpoints = result[1]
            if result[0] == "quit":
                running = False
            elif result[0] == "loss":
                game_over()
            """
            elif gewonnen:
                gekozenAanval = keuze(WillekeurigeAanvalKiezen([A_Bom, A_Zwaardslag, A_Genezen, A_Blokkeren]))
                if gekozenAanval == "Menu":
                    state = "Menu"
                elif not gekozenAanval == False:
                    Aanvallen.append(gekozenAanval)
            """

    if state == "Quit":
        running = False

    pygame.display.update()

pygame.quit()