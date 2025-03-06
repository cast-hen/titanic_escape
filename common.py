from parkour_functies import *
from pauze import *
from button_code import *
import pygame

WIDTH = 1366
HEIGHT = 690

def eind():
    return None

def game_over():
    backgroundColour = (255, 0, 0)
    screen.fill(backgroundColour)
    lives = 0

    font1 = pygame.font.Font("freesansbold.ttf", 100)
    font2 = pygame.font.Font("freesansbold.ttf", 50)
    text1 = font1.render("You're dead", True, 'black')
    text2 = font2.render("Lives: " + str(lives), True, 'black')
    text1Rect = text1.get_rect()
    text2Rect = text2.get_rect()
    text1Rect.center = (WIDTH/2, HEIGHT/2)
    text2Rect.center = (WIDTH / 2, HEIGHT / 2 + 100)
    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)

    pygame.display.flip()
    time.sleep(2)

    return 200, 200, lives


def menu():
    font = pygame.font.Font("freesansbold.ttf", 100)
    text = font.render("Titanic escape", True, (255, 255, 255))

    buttonKeuze1 = button((WIDTH / 2 - 100), (HEIGHT / 2), 200, 80, 'grey', 'darkgrey', "start", 'white', 50, 'white')
    buttonKeuze2 = button((WIDTH / 2 - 100), (HEIGHT / 4 * 2.8), 200, 80, 'grey', 'darkgrey', "quit", 'white', 50,'white')

    mouse = pygame.mouse.get_pos()
    mouseDown = False
    button.check(buttonKeuze1, mouse, mouseDown, screen)
    button.check(buttonKeuze2, mouse, mouseDown, screen)

    while True:
        for event in pygame.event.get():
            if button.check(buttonKeuze1, pygame.mouse.get_pos(), mouseDown, screen):
                return "Begin"
            if button.check(buttonKeuze2, pygame.mouse.get_pos(), mouseDown, screen):
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
                    if button.check(buttonKeuze1, pygame.mouse.get_pos(), mouseDown, screen):
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