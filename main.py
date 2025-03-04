from pauze import *
from enemy_functions import *
from parkour_functies import *
from button_code import *
from player_functies import *
from common import *
import pygame
import time
import random

# pygame.image.load("Bom.png")

screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)
running = True
pygame.init()
Aanvallen = ["Slaan", "Genezen"]

Speler = [10, Aanvallen, [0, 0]]
levens = 10

WIDTH = 1366
HEIGHT = 690

# Speler = [Levens, Aanvallen, positie]

A_Bom = Aanval(pygame.transform.scale(pygame.image.load("resources/textures/Bom.png"), (200, 200)), "Bom",
               "Valt elke vijand aan voor 5 schade", 5, 5)
A_Zwaardslag = Aanval("", "Zwaard", "Valt 1 vijand aan voor 10 schade", 10, 0)
A_Genezen = Aanval("", "Genezen", "Genees 10 levens", 0, 10)
A_Blokkeren = Aanval("", "Blokkeren", "Blokkeer 80% van de schade", 0, 0)

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
            gewonnen = gevecht(100, Vijand("", "", 100, 10))
            if gewonnen == "Menu":
                state = "Menu"
            elif gewonnen:
                gekozenAanval = keuze(WillekeurigeAanvalKiezen([A_Bom, A_Zwaardslag, A_Genezen, A_Blokkeren]))
                if gekozenAanval == "Menu":
                    state = "Menu"
                elif not gekozenAanval == False:
                    Aanvallen.append(gekozenAanval)
                else:
                    running = False
            else:
                game_over()

    if state == "Quit":
        running = False

    pygame.display.update()

pygame.quit()