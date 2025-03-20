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
        """
        Displays a card with a move and its description
        :param x: position of the left side of the card
        :param y: position of the top side of the card
        :return: nothing
        """
        #teken de kaart op de achtergrond
        screen.blit(pygame.transform.scale(pygame.image.load("resources/textures/Kaart.png"), (400, 400)), (x - 100, y - 75))
        #maakt de font voor de beschrijving
        font = pygame.font.Font("freesansbold.ttf", 10)
        #tekent het plaatje als er voor die move een is
        if not self.image == "":
            screen.blit(self.image, (x, y))
        #tekent de beschrijving
        text = font.render(self.description, True, (255, 255, 255))
        screen.blit(text, (x + 80 - int(len(self.description) * 1.3), y + 200))
        #tekent de naam van de move
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, (x + 80 - len(self.name) * 5, y - 40))


def fight(enemy, player, screen):
    def draw_scene():
        screen.fill((40, 255, 255))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enemy.colour, pygame.Rect(1000, 250, 100, 200))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(145, 175, 210, 60))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(945, 175, 210, 60))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(150, 180, 200 * (playerCurrentHealth / player.hitpoints), 50))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(950, 180, 200 * (enemyCurrentHealth / enemy.hitpoints), 50))
        pygame.display.update()
    def scrollText(text, colour, location):
        font = pygame.font.Font("freesansbold.ttf", 80)
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
        for i in range(0, 20):
            draw_scene()
            screen.blit(toScrollText, (x, y - i))
            pygame.display.update()
            time.sleep(0.01)
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
                        scrollText(str(damage), (255, 0, 0), "enemy")
                    elif move == "combo punch":
                        done = False
                        while not done:
                            damage = int(3 * damageMultiplierPlayer)
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy")
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
                scrollText(str(damage), (255, 0, 0), "player")
            elif move == "combo punch":
                done = False
                while not done:
                    damage = int(3 * damageMultiplierEnemy)
                    playerCurrentHealth -= damage
                    scrollText(str(damage), (255, 0, 0), "player")
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
                scrollText(str(healed), (0, 255, 0), "enemy")
                if poisonTurnsLeftEnemy > 0:
                    poisonTurnsLeftEnemy = 0
                    scrollText("poison cleared", (0, 255, 0), "enemy")
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
    """
    Displays 3 moves the player can choose from to add to their deck
    :param options: list of 3 moves the player can choose from
    :return: the chosen move
    """
    #tekent de 3 opties als kaarten
    screen.fill((100, 100, 100))
    options[0].displayMove(270, 160)
    options[1].displayMove(570, 160)
    options[2].displayMove(870, 160)
    #maakt drie knoppen aan om je keuze te maken
    buttonChoice1 = button(300, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')
    buttonChoice2 = button(600, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')
    buttonChoice3 = button(900, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')
    #loop waarin gekeken wordt welke knop wordt ingedrukt
    while True:
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.QUIT:
                return "quit"
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
        #kijkt welke knopper worden ingedrukt en returnt de corresponderende move
        if button.check(buttonChoice1, mouseDown, screen):
            return options[0]
        if button.check(buttonChoice2, mouseDown, screen):
            return options[1]
        if button.check(buttonChoice3, mouseDown, screen):
            return options[2]