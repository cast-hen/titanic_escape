from pauze import *
from button_code import *
import pygame

WIDTH = 1366
HEIGHT = 690

def eind():
    return None

def game_over():
    return None



def menu():
    font = pygame.font.Font("freesansbold.ttf", 100)
    text = font.render("Titanic escape", True, (255, 255, 255))

    mouseDown = False
    buttonKeuze1 = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "start", 'white', 50, 'white')
    buttonKeuze2 = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "quit", 'white', 50,'white')

    buttonCheck(buttonKeuze1, mouseDown)
    buttonCheck(buttonKeuze2, mouseDown)

    while True:
        for event in pygame.event.get():
            if buttonCheck(buttonKeuze1, mouseDown):
                return "Begin"
            if buttonCheck(buttonKeuze2, mouseDown):
                return "Quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            else:
                mouseDown = False

            if event.type == pygame.QUIT:
                return False

        screen.blit(text, (300, 50))

def gevecht(health, enemy):
    def draw_scene():
        screen.fill((100, 200, 0))
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(700, 250, 100, 200))
        healthTextPlayer = healthFont.render(str(playerHealth) + "/" + str(health), True, (255, 255, 255))
        healthTextPlayerRect = healthTextPlayer.get_rect()
        healthTextPlayerRect.center = (250, 200)
        screen.blit(healthTextPlayer, healthTextPlayerRect)
        healthTextEnemy = healthFont.render(str(enemyHealth) + "/" + str(enemy.hitpoints), True, (255, 255, 255))
        healthTextEnemyRect = healthTextEnemy.get_rect()
        healthTextEnemyRect.center = (750, 200)
        screen.blit(healthTextEnemy, healthTextEnemyRect)
        pygame.display.update()

    buttonKeuze1 = button(70, 500, 160, 80, (0, 0, 255), (255, 0, 0), "Aanval", 'white', 50, 'white')

    playerHealth = health
    enemyHealth = enemy.hitpoints
    fighting = True
    state = "turnPlayer"
    while fighting:
        mouse = pygame.mouse.get_pos()
        draw_scene()
        if state == "turnPlayer":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fighting = False
                    return "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
                    if buttonCheck(buttonKeuze1, mouseDown):
                        enemy.hitpoints -= 10
                    if enemy.hitpoints <= 0:
                        return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if Pause() == "Menu":
                            return "Menu"
        elif state == "turnEnemy":
            pass
        time.sleep(0.01)

    pygame.display.update()