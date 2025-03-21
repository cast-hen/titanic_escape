import pygame
import time
import random
from button_code import *
from pauze import *
from common import *
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()


class move:
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

    def displayMove(self, x, y):
        """
        Displays a card with a move and its description
        :param x: horizontal position of the center of the card
        :param y: vertical position of the center of the card
        :return: nothing
        """
        # Tekent de kaart op de achtergrond
        screen.blit(pygame.transform.scale(pygame.image.load("resources/textures/KaartCROP.png"), (288, 472)), (x - 144, y - 236))
        # Tekent het plaatje als er voor die move een is
        if not self.image == "":
            screen.blit(self.image, (x, y))
        # Print de tekst op de kaart
        textPrint(self.description, 20, 'white', (x, y + 150))
        textPrint(self.name, 35, 'white', (x, y - 200))


def fight(enemy, player, screen):
    def draw_scene():
        screen.fill((40, 255, 255))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enemy.colour, pygame.Rect(1000, 250, 100, 200))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(145, 175, 210, 60))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(945, 175, 210, 60))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(150, 180, 200 * (playerCurrentHealth / player.maxHitpoints), 50))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(950, 180, 200 * (enemyCurrentHealth / enemy.hitpoints), 50))

        textPrint(str(playerCurrentHealth), 40, 'white', (250, 205))
        textPrint(str(enemyCurrentHealth), 40, 'white', (1050, 205))

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

    attackButton = button(0, round((HEIGHT / 5) * 3), round(WIDTH / 2), round(HEIGHT/5), (255, 180, 0), (255, 255, 255), "Attack", (0, 0, 0), WIDTH // 12, (0, 0, 0))
    itemButton = button(0, round((HEIGHT / 5) * 4), round(WIDTH / 2), round(HEIGHT / 5), (255, 180, 0), (255, 255, 255), "Use item", (0, 0, 0), WIDTH // 12,  (0, 0, 0))
    fleeButton = button(WIDTH / 2, round((HEIGHT / 5) * 4), round(WIDTH / 2), round(HEIGHT / 5), (255, 80, 0), (255, 255, 255), "Flee", (0, 0, 0), WIDTH // 12,  (0, 0, 0))
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
                healButton = button(WIDTH / 2, round((HEIGHT / 5) * 3), round(WIDTH / 2), round(HEIGHT / 5), (255, 180, 0), (255, 255, 255),"Heal", (0, 0, 0), round(WIDTH / 12), (0, 0, 0))
            else:
                healButton = button(WIDTH / 2, round((HEIGHT / 5) * 3), round(WIDTH / 2), round(HEIGHT / 5), (50, 20, 0), (50, 20, 0),"Heal", (0, 0, 0), round(WIDTH / 12), (0, 0, 0))
            mouseDown = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fighting = False
                    result = "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
            if button.check(attackButton, mouseDown, screen):
                draw_scene()
                buttonNextPage = button(round(WIDTH / 2), round((HEIGHT / 7) * 6), round(WIDTH / 2), round(HEIGHT / 7), (255, 180, 0), (255, 255, 255), "Next page", (0, 0, 0), round(WIDTH / 30), (0, 0, 0))
                buttonPrevPage = button(0, round((HEIGHT / 7) * 6), round(WIDTH / 2), round(HEIGHT / 7), (255, 180, 0), (255, 255, 255), "Previous page", (0, 0, 0), round(WIDTH / 30), (0, 0, 0))
                buttonBack = button(0, 0, round(WIDTH / 5), round(HEIGHT / 7), (255, 180, 0), (255, 255, 255), "Back", (0, 0, 0), round(WIDTH / 25), (0, 0, 0))
                done = False
                pages = round(len(player.moveset) / 4)
                page = 0
                move = None
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
                            moveButton = button(round((WIDTH / 4) * i), round((HEIGHT / 7) * 4), round(WIDTH / 4), round((HEIGHT / 7) * 2), (255, 180, 0), (255, 255, 255), player.moveset[(page * 4) + i].name, (0, 0, 0), round(WIDTH / 40), (0, 0, 0))
                            if button.check(moveButton, mouseDown, screen):
                                move = player.moveset[i].name
                                done = True
                    if button.check(buttonBack, mouseDown, screen):
                        done = True
                draw_scene()
                if move is not None:
                    if move == "punch":
                        damage = 10 * damageMultiplierPlayer
                        enemyCurrentHealth -= damage
                        scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                    elif move == "combo punch":
                        while True:
                            damage = 3 * damageMultiplierPlayer
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                            if random.randint(0, 1) == 0:
                                break
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
                    healed = round(player.maxHitpoints - playerCurrentHealth)
                    playerCurrentHealth = player.maxHitpoints
                else:
                    playerCurrentHealth += healed
                scrollText(str(healed), (0, 255, 0), "player", 80, 20)
                if poisonTurnsLeftPlayer > 0:
                    poisonTurnsLeftPlayer = 0
                    scrollText("poison cleared", (0, 255, 0), "player")
                state = "turnEnemy"

            elif button.check(fleeButton, mouseDown, screen):
                dimSurface = pygame.Surface((WIDTH, HEIGHT))
                pygame.Surface.set_alpha(dimSurface, 150)
                pygame.Surface.blit(screen, dimSurface)

                pygame.draw.rect(screen, (255, 180, 0), [WIDTH // 3, HEIGHT // 3, WIDTH // 3, HEIGHT // 3])
                textPrint("Are you sure you want to leave?", WIDTH // 50, 'black',(WIDTH // 2, HEIGHT * 5 // 12))
                confirmButton = button(WIDTH // 3, HEIGHT // 2, round(WIDTH / 6), HEIGHT // 6, (255, 80, 0), (255, 255, 255), "confirm", (0, 0, 0), WIDTH // 30,  (0, 0, 0))
                cancelButton = button(WIDTH // 2, HEIGHT // 2, round(WIDTH / 6), HEIGHT // 6, (255, 80, 0),(255, 255, 255), "cancel", (0, 0, 0), WIDTH // 30, (0, 0, 0))

                index = waitForInput([confirmButton, cancelButton], True)
                if index == 0:
                    fighting = False
                    result = "begin"
                else:
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
                while True:
                    damage = 3 * damageMultiplierEnemy
                    playerCurrentHealth -= damage
                    scrollText(str(damage), (255, 0, 0), "player", 80, 20)
                    if random.randint(0, 1) == 0:
                        break
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
                    healed = round(enemy.hitpoints - enemyCurrentHealth)
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
    return result, playerCurrentHealth

def chooseNewAttack(options):
    """
    Displays 3 moves the player can choose from to add to their deck
    :param options: list of 3 moves the player can choose from
    :return: the chosen move or the new state
    """
    # Tekent de 3 opties als kaarten
    screen.fill((100, 100, 100))
    options[0].displayMove(WIDTH/2 - 288 - 40, HEIGHT/2 - 50)
    options[1].displayMove(WIDTH/2, HEIGHT/2 - 50)
    options[2].displayMove(WIDTH/2 + 288 + 40, HEIGHT/2 - 50)
    # Maakt drie knoppen aan om je keuze te maken
    buttonChoice1 = button(WIDTH/2 - 288 - 40 - 105, 590, 210, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')
    buttonChoice2 = button(WIDTH/2 - 105, 590, 210, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')
    buttonChoice3 = button(WIDTH/2 + 288 + 40 - 105, 590, 210, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white')
    # Loop waarin gekeken wordt welke knop wordt ingedrukt
    while True:
        index = waitForInput([buttonChoice1, buttonChoice2, buttonChoice3], True)
        if index == -1:
            if Pause() == "Menu":
                return "Menu"
            else:
                screen.fill((100, 100, 100))
                options[0].displayMove(WIDTH / 2 - 288 - 40, HEIGHT / 2 - 50)
                options[1].displayMove(WIDTH / 2, HEIGHT / 2 - 50)
                options[2].displayMove(WIDTH / 2 + 288 + 40, HEIGHT / 2 - 50)
        else:
            return options[index]
