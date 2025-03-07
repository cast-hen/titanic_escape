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

def eind():
    return None

def game_over(lives):
    lives -= 1
    if lives == 0:
        print("oh no")
    screen.fill('red')
    font = pygame.font.Font("freesansbold.ttf", 100)
    text = font.render("You died", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH/2, HEIGHT/2)
    screen.blit(text, textRect)

    font = pygame.font.Font("freesansbold.ttf", 40)
    text = font.render("You have " + str(lives) + " lives left", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH / 2, HEIGHT / 2 + 100)
    screen.blit(text, textRect)
    pygame.display.flip()
    time.sleep(2)
    return 200, 200, lives


def menu():
    font = pygame.font.Font("freesansbold.ttf", 100)
    text = font.render("Titanic escape", True, (255, 255, 255))

    mouseDown = False
    buttonBegin = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "start", 'white', 50, 'white')
    buttonQuit = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "quit", 'white', 50,'white')
    screen.blit(text, (300, 50))
    while True:
        mouse = pygame.mouse.get_pos()
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.QUIT:
                return "quit"
        if button.check(buttonBegin, mouse, mouseDown, screen):
            return "begin"
        if button.check(buttonQuit, mouse, mouseDown, screen):
            return "quit"
