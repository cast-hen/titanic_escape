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
    """
    Starts a fight between the player and a given enemy
    :param enemy: the enemy the player will fight
    :param player: the players stats
    :param screen: the screen where the fight should be displayed
    :return: a list with: the result of the fight as "win", "lose", "flee" or "quit"
                          the ammount of hitpoints the player has left
    """
    def draw_scene():
        """
        Draws the fighting scene with the characters and their health displayed
        :return: none
        """
        #tekent de achtergrond
        screen.fill((40, 255, 255))
        #maakt het font aan voor de hitpoints
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        #tekent de speler en de enemy
        pygame.draw.rect(screen, player.colour, pygame.Rect(200, 250, 100, 200))
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
    #variabelen en knoppen aanmaken
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
    #main loop
    while fighting:
        #beurt van de speler
        if state == "turnPlayer":
            #kijkt of healen een optie is en geeft de correcte texture
            if playerCurrentHealth < player.maxHitpoints:
                healButton = button(width / 2, int((height / 5) * 3), int(width / 2), int(height / 5), (255, 180, 0), (255, 255, 255),"Heal", (0, 0, 0), int(width / 12), (0, 0, 0))
            else:
                healButton = button(width / 2, int((height / 5) * 3), int(width / 2), int(height / 5), (50, 20, 0), (50, 20, 0),"Heal", (0, 0, 0), int(width / 12), (0, 0, 0))
            #checkt de events en past variabelen aan
            mouseDown = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fighting = False
                    result = "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if Pause() == "Menu":
                            return ["Menu", playerCurrentHealth]
                        else:
                            draw_scene()
            #aanvalsknop checken
            if button.check(attackButton, mouseDown, screen):
                #maakt nieuwe variabelen voor weergave van de moveopties
                draw_scene()
                buttonNextPage = button(int(width / 2), int((height / 7) * 6), int(width / 2), int(height / 7), (255, 180, 0), (255, 255, 255), "Next page", (0, 0, 0), int(width / 30), (0, 0, 0))
                buttonPrevPage = button(0, int((height / 7) * 6), int(width / 2), int(height / 7), (255, 180, 0), (255, 255, 255), "Previous page", (0, 0, 0), int(width / 30), (0, 0, 0))
                buttonBack = button(0, 0, int(width / 5), int(height / 7), (255, 180, 0), (255, 255, 255), "Back", (0, 0, 0), int(width / 25), (0, 0, 0))
                done = False
                pages = int((len(player.moveset) - 1) / 4)
                page = 0
                move = "none"
                #nieuwe loop waarin move wordt geselecteerd
                while not done:
                    #positie van de muis vinden en kijken of hij ingedrukt is
                    mouseDown = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseDown = True
                    #pagina selecteren
                    if page < pages:
                        if button.check(buttonNextPage, mouseDown, screen):
                            page += 1
                            draw_scene()
                    if page > 0:
                        if button.check(buttonPrevPage, mouseDown, screen):
                            page -= 1
                            draw_scene()
                    #tekent de moves die op een pagina worden weergeven en controleert of er een wordt geselecteerd
                    for i in range(0, 4):
                        if (page * 4) + i < len(player.moveset):
                            moveButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4), int((height / 7) * 2), (255, 180, 0), (255, 255, 255), player.moveset[(page * 4) + i].name, (0, 0, 0), int(width / 40), (0, 0, 0))
                            if button.check(moveButton, mouseDown, screen):
                                move = player.moveset[i].name
                                done = True
                    #checkt of de knop wordt ingedrukt om terug te gaan naar de andere opties
                    if button.check(buttonBack, mouseDown, screen):
                        done = True
                draw_scene()
                #als een move is geselecteerd wordt deze uitgevoerd
                if move != "none":
                    damage = 0
                    if move == "punch":
                        damage = 10 * damageMultiplierPlayer
                    elif move == "combo punch":
                        damage = 30
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
                    #controleert of de enemy dood is
                    if enemyCurrentHealth <= 0:
                        enemyCurrentHealth = 0
                        fighting = False
                        result = "win"
                    else:
                        state = "turnEnemy"
            #knop voor een item gebruiken
            elif button.check(itemButton, mouseDown, screen):
                pass
            #knop om te healen, werkt alleen als de speler heals overheeft en niet op max health is
            elif button.check(healButton, mouseDown, screen) and playerCurrentHealth < player.maxHitpoints:
                playerCurrentHealth += 20
                if playerCurrentHealth > player.maxHitpoints:
                    playerCurrentHealth = player.maxHitpoints
                state = "turnEnemy"
            #button of weg te rennen van het gevecht
            elif button.check(fleeButton, mouseDown, screen):
                #variabelen en knoppen aanmaken
                confirmFont = pygame.font.Font("freesansbold.ttf", int(width * 0.02))
                confirmText = confirmFont.render("Are you sure you want to leave?", True, (0, 0, 0))
                confirmRect = confirmText.get_rect()
                confirmRect.center = (int(width / 2), int((height / 12) * 5))
                pygame.draw.rect(screen, (255, 180, 0), [int(width / 3), int(height / 3), int(width / 3), int(height / 3)])
                screen.blit(confirmText, confirmRect)
                confirmed = False
                confirmButton = button(int(width / 3), int(height / 2), int(width / 6), int(height / 6), (255, 80, 0), (255, 255, 255), "confirm", (0, 0, 0), int(width / 30),  (0, 0, 0))
                cancelButton = button(int(width / 2), int(height / 2), int(width / 6), int(height / 6), (255, 80, 0),(255, 255, 255), "cancel", (0, 0, 0), int(width / 30), (0, 0, 0))
                #loop om te confirmen dat de speler het gevecht wil eindigen
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
        #beurt van de vijand
        elif state == "turnEnemy":
            draw_scene()
            #selecteert een move (op dit moment volledig random)
            selected = False
            while not selected:
                roll = random.randint(0, len(enemy.moveset) - 1)
                move = enemy.moveset[roll]
                if move != "heal" or enemyCurrentHealth < enemy.hitpoints:
                    selected = True
            #voert de move uit
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
            #controleert of de vijand heeft gewonnn
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