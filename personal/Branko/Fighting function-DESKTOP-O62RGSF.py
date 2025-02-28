import pygame
import time
import random

allMovesList = ["punch", "heal", "combo punch", "enrage", "poison", "life steal", "block"]

running = True
health = 100
enimy1 = [(0, 0, 255), 100, ["punch", "block"]]
enimy2 = [(255, 0, 255), 500, ["combo punch", "heal", "block"]]


def fight(enimy):
    def draw_scene():
        background = pygame.image.load("../../sprint 1/fightBackground.jpg")
        background = pygame.transform.scale(background, (1300, 600))
        screen.blit(background, (0, 0))
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enimy[0], pygame.Rect(1000, 250, 100, 200))
        healthTextPlayer = healthFont.render(str(playerHealth) + "/" + str(health), True, (255, 255, 255))
        healthTextPlayerRect = healthTextPlayer.get_rect()
        healthTextPlayerRect.center = (250, 200)
        screen.blit(healthTextPlayer, healthTextPlayerRect)
        healthTextEnimy = healthFont.render(str(enimyHealth) + "/" + str(enimy[1]), True, (255, 255, 255))
        healthTextEnimyRect = healthTextPlayer.get_rect()
        healthTextEnimyRect.center = (1050, 200)
        screen.blit(healthTextEnimy, healthTextEnimyRect)
        pygame.display.update()

    playerHealth = health
    enimyHealth = enimy[1]
    fighting = True
    state = "turnPlayer"
    while fighting:
        draw_scene()
        if state = "turnPlayer":
            pass
        elif state = "turnEnemy":
            pass

    pygame.display.update()


screen = pygame.display.set_mode((1300, 600))
pygame.init()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                fight(enimy1)
            if event.key == pygame.K_r:
                fight(enimy2)
    time.sleep(0.1)
pygame.quit()