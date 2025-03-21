import pygame
import time
import random
from button_code import *

class character:
    def __init__(self, name, lives, colour, hitpoints, maxHitpoints, moveset, items, heals):
        self.name = name
        self.lives = lives
        self.colour = colour
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.moveset = moveset
        self.items = items
        self.heals = heals
class enemy:
    def __init__(self, name, colour, hitpoints, moveset, heals):
        self.name = name
        self.colour = colour
        self.hitpoints = hitpoints
        self.moveset = moveset
        self.heals = heals
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

player = character("greg", 5,(0, 0, 255), 100, 100,[punch, comboPunch, enrage, poison, lifeSteal, block], [], 5)

running = True
screen = pygame.display.set_mode((1300, 600))
mouseDown = False
health = 100
enemy1 = enemy("Bob", (0, 0, 255), 100, ["punch"], 5)
enemy2 = enemy("ASHRddgteGEtek, destroyer of lightbulbs", (255, 0, 255), 20, ["punch", "combo punch", "enrage"], 0)
buttonEnemy1 = button(100, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy1", (255, 255, 255), 80,  (255, 0, 0))
buttonEnemy2 = button(800, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy2", (255, 255, 255), 80, (255, 0, 0))

def fight(enemy, player, screen):
    def draw_scene():
        screen.fill((40, 255, 255))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enemy.colour, pygame.Rect(1000, 250, 100, 200))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(145, 175, 210, 60))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(945, 175, 210, 60))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(150, 180, 200 * (playerCurrentHealth / player.maxHitpoints), 50))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(950, 180, 200 * (enemyCurrentHealth / enemy.hitpoints), 50))
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        healthTextPlayer = healthFont.render(str(playerCurrentHealth), True, (255, 255, 255))
        healthTextEnemy = healthFont.render(str(enemyCurrentHealth), True, (255, 255, 255))
        healthTextPlayerRect = healthTextPlayer.get_rect()
        healthTextEnemyRect = healthTextEnemy.get_rect()
        healthTextPlayerRect.center = (250, 205)
        healthTextEnemyRect.center = (1050, 205)
        screen.blit(healthTextPlayer, healthTextPlayerRect)
        screen.blit(healthTextEnemy, healthTextEnemyRect)
    def scrollText(text, colour, location, size, scrollTime):
        font = pygame.font.Font("freesansbold.ttf", size)
        toScrollText = font.render(text, True, colour)
        if location == "player":
            x = 400
            y = 150
        elif location == "enemy":
            x = 900 - toScrollText.get_rect().width
            y = 150
        elif location == "center":
            x = screen.get_width() - (toScrollText.get_rect().width / 2)
            y = 200
        for i in range(0, scrollTime):
            draw_scene()
            screen.blit(toScrollText, (x, y - i))
            pygame.display.update()
            time.sleep(0.01)
        draw_scene()
        pygame.display.update()
    width = screen.get_width()
    height = screen.get_height()
    attackButton = button(0, int((height / 5) * 3), int(width / 2), int(height/5), (255, 180, 0), (255, 255, 255), "Attack", (0, 0, 0), int(width / 12), (0, 0, 0))
    itemButton = button(0, int((height / 5) * 4), int(width / 2), int(height / 5), (255, 180, 0), (255, 255, 255), "Use item", (0, 0, 0), int(width / 12),  (0, 0, 0))
    fleeButton = button(width / 2, int((height / 5) * 4), int(width / 2), int(height / 5), (255, 80, 0), (255, 255, 255), "Flee", (0, 0, 0), int(width / 12),  (0, 0, 0))
    playerCurrentHealth = player.hitpoints
    enemyCurrentHealth = enemy.hitpoints
    playerHeals = player.heals
    enemyHeals = enemy.heals
    damageMultiplierPlayer = 1
    damageMultiplierEnemy = 1
    enrageTurnsLeftPlayer = 0
    enrageTurnsLeftEnemy = 0
    poisonTurnsLeftPlayer = 0
    poisonTurnsLeftEnemy = 0
    fighting = True
    state = "turnPlayer"
    draw_scene()
    pygame.mixer.init()
    pygame.mixer.music.load("resources/sound/battle_theme.mp3")
    pygame.mixer.music.play(loops=-1)
    while fighting:
        if state == "turnPlayer":
            if playerCurrentHealth < player.maxHitpoints and playerHeals > 0:
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
            if button.check(attackButton, mouseDown, screen):
                draw_scene()
                buttonNextPage = button(int(width / 2), int((height / 7) * 6), int(width / 2), int(height / 7), (255, 180, 0), (255, 255, 255), "Next page", (0, 0, 0), int(width / 30), (0, 0, 0))
                buttonPrevPage = button(0, int((height / 7) * 6), int(width / 2), int(height / 7), (255, 180, 0), (255, 255, 255), "Previous page", (0, 0, 0), int(width / 30), (0, 0, 0))
                buttonBack = button(0, 0, int(width / 5), int(height / 7), (255, 180, 0), (255, 255, 255), "Back", (0, 0, 0), int(width / 25), (0, 0, 0))
                done = False
                pages = int(len(player.moveset) / 4)
                page = 0
                move = "none"
                while not done:
                    mouseDown = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseDown = True
                    if page < pages:
                        if button.check(buttonNextPage, mouseDown, screen):
                            page += 1
                            draw_scene()
                    if page > 0:
                        if button.check(buttonPrevPage, mouseDown, screen):
                            page -= 1
                            draw_scene()
                    for i in range(0, 4):
                        if (page * 4) + i < len(player.moveset):
                            moveButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4), int((height / 7) * 2), (255, 180, 0), (255, 255, 255), player.moveset[(page * 4) + i].name, (0, 0, 0), int(width / 40), (0, 0, 0))
                            if button.check(moveButton, mouseDown, screen):
                                move = player.moveset[i].name
                                done = True
                    if button.check(buttonBack, mouseDown, screen):
                        done = True
                draw_scene()
                if move != "none":
                    if move == "punch":
                        damage = int(10 * damageMultiplierPlayer)
                        enemyCurrentHealth -= damage
                        scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                    elif move == "combo punch":
                        done = False
                        while not done:
                            damage = int(3 * damageMultiplierPlayer)
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                            if random.randint(0, 1) == 0:
                                done = True
                    elif move == "enrage":
                        pass
                    elif move == "poison":
                        poisonTurnsLeftEnemy = random.randint(2, 5)
                        scrollText("poisoned for " + str(poisonTurnsLeftEnemy) + " turns", (255, 0, 255), "enemy", 20, 50)
                    elif move == "life steal":
                        pass
                    elif move == "block":
                        pass
                    if enemyCurrentHealth <= 0:
                        enemyCurrentHealth = 0
                        fighting = False
                        result = "win"
                    else:
                        state = "turnEnemy"
            elif button.check(itemButton, mouseDown, screen):
                pass
            elif button.check(healButton, mouseDown, screen) and playerCurrentHealth < player.maxHitpoints and playerHeals > 0:
                playerHeals -= 1
                healed = 20
                if playerCurrentHealth + healed > player.maxHitpoints:
                    healed = int(player.maxHitpoints - playerCurrentHealth)
                    playerCurrentHealth = player.maxHitpoints
                else:
                    playerCurrentHealth += healed
                scrollText(str(healed), (0, 255, 0), "player")
                if poisonTurnsLeftPlayer > 0:
                    poisonTurnsLeftPlayer = 0
                    scrollText("poison cleared", (0, 255, 0), "player")
                state = "turnEnemy"
            elif button.check(fleeButton, mouseDown, screen):
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
                    mouseDown = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseDown = True
                    if button.check(confirmButton, mouseDown, screen):
                        fighting = False
                        result = "flee"
                        confirmed = True
                    elif button.check(cancelButton, mouseDown, screen):
                        confirmed = True
                        draw_scene()
        elif state == "turnEnemy":
            draw_scene()
            selected = False
            while not selected:
                roll = random.randint(0, len(enemy.moveset))
                if roll == len(enemy.moveset):
                    move = "heal"
                else:
                    move = enemy.moveset[roll]
                if move != "heal" or enemyCurrentHealth < enemy.hitpoints and enemyHeals > 0:
                    selected = True
            damage = 0
            if move == "punch":
                damage = 10 * damageMultiplierEnemy
                playerCurrentHealth -= damage
                scrollText(str(damage), (255, 0, 0), "player", 80, 20)
            elif move == "combo punch":
                done = False
                while not done:
                    damage = int(3 * damageMultiplierEnemy)
                    playerCurrentHealth -= damage
                    scrollText(str(damage), (255, 0, 0), "player", 80, 20)
                    if random.randint(0, 1) == 0:
                        done = True
            elif move == "enrage":
                pass
            elif move == "poison":
                pass
            elif move == "life steal":
                pass
            elif move == "block":
                pass
            elif move == "heal":
                enemyHeals -= 1
                healed = 20
                if enemyCurrentHealth + healed > enemy.hitpoints:
                    healed = int(enemy.hitpoints - enemyCurrentHealth)
                    enemyCurrentHealth = enemy.hitpoints
                else:
                    enemyCurrentHealth += healed
                scrollText(str(healed), (0, 255, 0), "enemy", 80, 20)
                if poisonTurnsLeftEnemy > 0:
                    poisonTurnsLeftEnemy = 0
                    scrollText("poison cleared", (0, 255, 0), "enemy", 40, 40)
            if playerCurrentHealth <= 0:
                playerCurrentHealth = 0
                fighting = False
                result = "loss"
            time.sleep(0.5)
            draw_scene()
            pygame.display.update()
            time.sleep(1)
            state = "turnPlayer"
        time.sleep(0.01)
        pygame.display.update()
    pygame.mixer.quit()
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
    if button.check(buttonEnemy1, mouseDown, screen):
        result = fight(enemy1, player, screen)
        screen.fill((0, 0, 0))
    elif button.check(buttonEnemy2, mouseDown, screen):
        result = fight(enemy2, player, screen)
        screen.fill((0, 0, 0))
    if result[0] == "win":
        screen.fill((0, 255, 0))
    elif result[0] == "quit":
        running = False

    time.sleep(0.01)
pygame.quit()