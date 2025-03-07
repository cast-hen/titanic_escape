import pygame
import time
import random
from button_code import *

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
class move:
    def __init__(self, name, description):
        self.name = name
        self.description = description

punch = move("punch", "Hits the opponent for 10 damage")
comboPunch = move("combo punch", "Hits the opponent a random number of times")
enrage = move("enrage", "Increases your damage on the next 3 turns")
poison = move("poison", "poisons your opponent to take damage over time")
lifeSteal = move("life steal", "Damages your opponent and gives you 30% back as health")
block = move("block", "Blocks your opponents next attack")

player = character("greg", 5,(0, 0, 255), 100, 100,[punch, comboPunch, enrage, poison, lifeSteal, block], [])

running = True
screen = pygame.display.set_mode((1300, 600))
mouseDown = False
health = 100
enemy1 = enemy("Bob", (0, 0, 255), 100, ["punch", "heal"])
enemy2 = enemy("ASHRddgteGEtek, destroyer of lightbulbs", (255, 0, 255), 20, ["punch", "combo punch", "enrage"])
buttonEnemy1 = button(100, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy1", (255, 255, 255), 80,  (255, 0, 0))
buttonEnemy2 = button(800, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy2", (255, 255, 255), 80, (255, 0, 0))

def fight(enemy, player, screen):
    def draw_scene():
        screen.fill((40, 255, 255))
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enemy.colour, pygame.Rect(1000, 250, 100, 200))
        healthTextPlayer = healthFont.render(str(playerCurrentHealth) + "/" + str(player.maxHitpoints), True, (255, 255, 255))
        healthTextPlayerRect = healthTextPlayer.get_rect()
        healthTextPlayerRect.center = (250, 200)
        screen.blit(healthTextPlayer, healthTextPlayerRect)
        healthTextEnemy = healthFont.render(str(enemyCurrentHealth) + "/" + str(enemy.hitpoints), True, (255, 255, 255))
        healthTextEnemyRect = healthTextEnemy.get_rect()
        healthTextEnemyRect.center = (1050, 200)
        screen.blit(healthTextEnemy, healthTextEnemyRect)
        pygame.display.update()
    width = screen.get_width()
    height = screen.get_height()
    attackButton = button(0, int((height / 5) * 3), int(width / 2), int(height/5), (255, 180, 0), (255, 255, 255), "Attack", (0, 0, 0), int(width / 12), (0, 0, 0))
    itemButton = button(0, int((height / 5) * 4), int(width / 2), int(height / 5), (255, 180, 0), (255, 255, 255), "Use item", (0, 0, 0), int(width / 12),  (0, 0, 0))
    fleeButton = button(width / 2, int((height / 5) * 4), int(width / 2), int(height / 5), (255, 80, 0), (255, 255, 255), "Flee", (0, 0, 0), int(width / 12),  (0, 0, 0))
    playerCurrentHealth = player.hitpoints
    enemyCurrentHealth = enemy.hitpoints
    damageMultiplierPlayer = 1
    damageMultiplierEnemy = 1
    fighting = True
    state = "turnPlayer"
    draw_scene()
    while fighting:
        mouse = pygame.mouse.get_pos()
        if state == "turnPlayer":
            if playerCurrentHealth < player.maxHitpoints:
                healButton = button(width / 2, int((height / 5) * 3), int(width / 2), int(height / 5), (255, 180, 0), (255, 255, 255),"Heal", (0, 0, 0), int(width / 12), (0, 0, 0))
            else:
                healButton = button(width / 2, int((height / 5) * 3), int(width / 2), int(height / 5), (50, 20, 0), (50, 20, 0),"Heal", (0, 0, 0), int(width / 12), (0, 0, 0))
            mouseDown = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fighting = False
                    result = "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
            if button.check(attackButton, mouse, mouseDown, screen):
                draw_scene()
                buttonNextPage = button(int(width / 2), int((height / 7) * 6), int(width / 2), int(height / 7), (255, 180, 0), (255, 255, 255), "Next page", (0, 0, 0), int(width / 30), (0, 0, 0))
                buttonPrevPage = button(0, int((height / 7) * 6), int(width / 2), int(height / 7), (255, 180, 0), (255, 255, 255), "Previous page", (0, 0, 0), int(width / 30), (0, 0, 0))
                buttonBack = button(0, 0, int(width / 5), int(height / 7), (255, 180, 0), (255, 255, 255), "Back", (0, 0, 0), int(width / 25), (0, 0, 0))
                done = False
                pages = int(len(player.moveset) / 4)
                page = 0
                move = "none"
                while not done:
                    mouse = pygame.mouse.get_pos()
                    mouseDown = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseDown = True
                    if page < pages:
                        if button.check(buttonNextPage, mouse, mouseDown, screen):
                            page += 1
                            draw_scene()
                    if page > 0:
                        if button.check(buttonPrevPage, mouse, mouseDown, screen):
                            page -= 1
                            draw_scene()
                    for i in range(0, 4):
                        if (page * 4) + i < len(player.moveset):
                            moveButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4), int((height / 7) * 2), (255, 180, 0), (255, 255, 255), player.moveset[(page * 4) + i].name, (0, 0, 0), int(width / 40), (0, 0, 0))
                            if button.check(moveButton, mouse, mouseDown, screen):
                                move = player.moveset[i].name
                                done = True
                    if button.check(buttonBack, mouse, mouseDown, screen):
                        done = True
                draw_scene()
                if move != "none":
                    damage = 0
                    if move == "punch":
                        damage = 10 * damageMultiplierPlayer
                    elif move == "combo punch":
                        pass
                    elif move == "enrage":
                        pass
                    elif move == "poison":
                        pass
                    elif move == "life steal":
                        pass
                    elif move == "block":
                        pass
                    elif move == "heal":
                        enemyCurrentHealth += 20
                        if enemyCurrentHealth > enemy.hitpoints:
                            enemyCurrentHealth = enemy.hitpoints
                    enemyCurrentHealth -= damage
                    if enemyCurrentHealth <= 0:
                        enemyCurrentHealth = 0
                        fighting = False
                        result = "win"
                    else:
                        state = "turnEnemy"
            elif button.check(itemButton, mouse, mouseDown, screen):
                pass
            elif button.check(healButton, mouse, mouseDown, screen) and playerCurrentHealth < player.maxHitpoints:
                playerCurrentHealth += 20
                if playerCurrentHealth > player.maxHitpoints:
                    playerCurrentHealth = player.maxHitpoints
                state = "turnEnemy"
            elif button.check(fleeButton, mouse, mouseDown, screen):
                confirmFont = pygame.font.Font("freesansbold.ttf", int(width * 0.02))
                confirmText = confirmFont.render("Are you sure you want to leave?", True, (0, 0, 0))
                confirmRect = confirmText.get_rect()
                confirmRect.center = (int(width / 2), int((height / 12) * 5))
                pygame.draw.rect(screen, (255, 180, 0), [int(width / 3), int(height / 3), int(width / 3), int(height / 3)])
                screen.blit(confirmText, confirmRect)
                confirmed = False
                confirmButton = button(int(width / 3), int(height / 2), int(width / 6), int(height / 6), (255, 80, 0), (255, 255, 255), "confirm", (0, 0, 0), int(width / 30),  (0, 0, 0))
                cancelButton = button(int(width / 2), int(height / 2), int(width / 6), int(height / 6), (255, 80, 0),(255, 255, 255), "cancel", (0, 0, 0), int(width / 30), (0, 0, 0))
                while not confirmed:
                    mouse = pygame.mouse.get_pos()
                    mouseDown = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseDown = True
                    if button.check(confirmButton, mouse, mouseDown, screen):
                        fighting = False
                        result = "flee"
                        confirmed = True
                    elif button.check(cancelButton, mouse, mouseDown, screen):
                        confirmed = True
                        draw_scene()
        elif state == "turnEnemy":
            draw_scene()
            selected = False
            while not selected:
                roll = random.randint(0, len(enemy.moveset) - 1)
                move = enemy.moveset[roll]
                if move != "heal" or enemyCurrentHealth < enemy.hitpoints:
                    selected = True
            damage = 0
            if move == "punch":
                damage = 10 * damageMultiplierEnemy
            elif move == "combo punch":
                pass
            elif move == "enrage":
                pass
            elif move == "poison":
                pass
            elif move == "life steal":
                pass
            elif move == "block":
                pass
            elif move == "heal":
                enemyCurrentHealth += 20
                if enemyCurrentHealth > enemy.hitpoints:
                    enemyCurrentHealth = enemy.hitpoints
            playerCurrentHealth -= damage
            if playerCurrentHealth <= 0:
                playerCurrentHealth = 0
                fighting = False
                result = "loss"
            time.sleep(0.5)
            draw_scene()
            time.sleep(1)
            state = "turnPlayer"
        time.sleep(0.01)
        pygame.display.update()
    return [result, playerCurrentHealth]

pygame.init()
while running:
    mouse = pygame.mouse.get_pos()
    result = "pass"
    mouseDown = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
    if button.check(buttonEnemy1, mouse, mouseDown, screen):
        result = fight(enemy1, player, screen)
        screen.fill((0, 0, 0))
    elif button.check(buttonEnemy2, mouse, mouseDown, screen):
        result = fight(enemy2, player, screen)
        screen.fill((0, 0, 0))
    if result[0] == "win":
        screen.fill((0, 255, 0))
    elif result[0] == "quit":
        running = False

    time.sleep(0.01)
pygame.quit()