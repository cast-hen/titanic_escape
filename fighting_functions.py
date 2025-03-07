import pygame
import time
import random
from button_code import *
from pauze import *
class move:
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
    def displayMove(self, x, y):
        screen.blit(pygame.transform.scale(pygame.image.load("resources/textures/Kaart.png"), (400, 400)), (x - 100, y - 75))

        font = pygame.font.Font("freesansbold.ttf", 10)

        if not self.image == "":
            screen.blit(self.image, (x, y))
        text = font.render(self.description, True, (255, 255, 255))
        screen.blit(text, (x + 80 - int(len(self.description) * 1.3), y + 200))

        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, (x + 80 - len(self.name) * 5, y - 40))


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

def chooseNewAttack(options):
    screen.fill((100, 100, 100))
    options[0].displayMove(30, 110)
    options[1].displayMove(330, 110)
    options[2].displayMove(630, 110)

    buttonChoice1 = button(50, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')
    buttonChoice2 = button(350, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')
    buttonChoice3 = button(650, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')

    while True:
        mouse = pygame.mouse.get_pos()
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if Pause() == "Menu":
                        return "Menu"
                    else:
                        screen.fill((100, 100, 100))
                        options[0].displayMove(30, 110)
                        options[1].displayMove(330, 110)
                        options[2].displayMove(630, 110)
                    if event.type == pygame.QUIT:
                        return False
        if button.check(buttonChoice1, mouse, mouseDown, screen):
            return options[0]
        if button.check(buttonChoice2, mouse, mouseDown, screen):
            return options[1]
        if button.check(buttonChoice3, mouse, mouseDown, screen):
            return options[2]