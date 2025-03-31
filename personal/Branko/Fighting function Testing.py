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
    def __init__(self, name, colour, hitpoints, moveset, items, heals):
        self.name = name
        self.colour = colour
        self.hitpoints = hitpoints
        self.moveset = moveset
        self.items = items
        self.heals = heals
class move:
    def __init__(self, name, description):
        self.name = name
        self.description = description
class item:
    def __init__(self, name, ammount):
        self.name = name
        self.ammount = ammount

punch = move("punch", "Hits the opponent for 10 damage")
comboPunch = move("combo punch", "Hits the opponent a random number of times")
enrage = move("enrage", "Increases your damage on the next 3 turns")
poison = move("poison", "poisons your opponent to take damage over time")
lifeSteal = move("life steal", "Damages your opponent and gives you 30% back as health")
block = move("block", "Blocks your opponents next attack")

player = character("greg", 5,(0, 0, 255), 100, 100,[punch, comboPunch, enrage, poison, lifeSteal, block], [
    item("Full Restore", 2),
    item("Bomb", 5)
], 5)

running = True
screen = pygame.display.set_mode((1300, 600), pygame.FULLSCREEN)
mouseDown = False
health = 100
enemy1 = enemy("Bob", (0, 0, 255), 100, ["punch"], [], 5)
enemy2 = enemy("ASHRddgteGEtek, destroyer of lightbulbs", (255, 0, 255), 20, ["punch", "combo punch", "enrage"], [], 0)
buttonEnemy1 = button(100, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy1", (255, 255, 255), 80,  (255, 0, 0))
buttonEnemy2 = button(800, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy2", (255, 255, 255), 80, (255, 0, 0))

def fight(enemy, player, screen):
    """
    Starts a fight with a given enemy and returns the result
    enemy: an enemy following the enemy class that will be fought
    player: the player following the player class fighting
    screen: the screen where everything should be drawn
    return: a list containing the result of the fight as a string and the hitpoints the player has remaining as an integer
    """
    def draw_scene():
        """
        Draws the fighting scene
        return: none
        """
        #draws the background
        screen.fill((40, 255, 255))
        #draws the player and the enemy
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enemy.colour, pygame.Rect(1000, 250, 100, 200))
        #draws the healthbars
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
        """
        Scrolls a given text across the screen for a given time
        text: a string of text you want to scroll
        colour: the colour of the text as 3 integers
        location: the location of the text as a string with 2 options: "player" or "enemy"
        size: "the size of the text as an integer"
        scrollTime: the ammount of time the text will scroll for as an integer
        return: none
        """
        #sets the text to be scrolled
        font = pygame.font.Font("freesansbold.ttf", size)
        toScrollText = font.render(text, True, colour)
        #defines the x value depending on the given location
        if location == "player":
            x = 400
        elif location == "enemy":
            x = 900 - toScrollText.get_rect().width
        #for loop where the text is slowly moved upwards
        for i in range(0, scrollTime):
            draw_scene()
            screen.blit(toScrollText, (x, 150 - i))
            pygame.display.update()
            time.sleep(0.01)
        #resets the screen
        draw_scene()
        pygame.display.update()
    def blocked(location):
        """
        Function to show an attack has been blocked
        location: a string, either "player or "enemy" of which character blocked the move
        return: none
        """
        #sets the blocked text to be scrolled
        font = pygame.font.Font("freesansbold.ttf", 40)
        blockedText = font.render("blocked", True, (100, 100, 255))
        #sets the x value and rectangle position depending on the given location
        if location == "player":
            x = 400
            blockedRect = pygame.Rect(400, 200, 30, 250)
        elif location == "enemy":
            x = 900 - blockedText.get_rect().width
            blockedRect = pygame.Rect(870, 200, 30, 250)
        #for loop where the text is scrolled upwards
        for i in range(0, 20):
            draw_scene()
            pygame.draw.rect(screen, (100, 100, 255), blockedRect)
            screen.blit(blockedText, (x, 150 - i))
            pygame.display.update()
            time.sleep(0.01)
        time.sleep(0.5)
        draw_scene()
        pygame.display.update()
    #defining the variables before the fight starts
    width = screen.get_width()
    height = screen.get_height()
    attackButton = button(0, (height / 5) * 3, width / 2, height/5, (255, 180, 0), (255, 255, 255), "Attack", (0, 0, 0), width // 12, (0, 0, 0))
    fleeButton = button(width / 2, (height / 5) * 4, width / 2, height / 5, (255, 80, 0), (255, 255, 255), "Flee", (0, 0, 0), width // 12,  (0, 0, 0))
    buttonNextPage = button(width / 2, (height / 7) * 6, width / 2, height / 7, (255, 180, 0), (255, 255, 255), "Next page", (0, 0, 0), width // 30, (0, 0, 0))
    buttonPrevPage = button(0, (height / 7) * 6, width / 2, height / 7, (255, 180, 0), (255, 255, 255), "Previous page",(0, 0, 0), width // 30, (0, 0, 0))
    buttonBack = button(0, 0, width / 5, height / 7, (255, 180, 0), (255, 255, 255), "Back", (0, 0, 0), width // 25,(0, 0, 0))
    playerCurrentHealth = player.hitpoints
    enemyCurrentHealth = enemy.hitpoints
    playerHeals = player.heals
    enemyHeals = enemy.heals
    playerBlocks = 3
    enemyBlocks = 3
    damageMultiplierPlayer = 1
    damageMultiplierEnemy = 1
    enrageTurnsLeftPlayer = 0
    enrageTurnsLeftEnemy = 0
    poisonTurnsLeftPlayer = 0
    poisonTurnsLeftEnemy = 0
    immunityTurnsLeftPlayer = 0
    immunityTurnsLeftEnemy = 0
    fighting = True
    state = "turnPlayer"
    draw_scene()
    #the main fighting loop
    while fighting:
        #the players turn
        if state == "turnPlayer":
            #sets the texture of the buttons depending on whether its an available option or not
            if (playerCurrentHealth < player.maxHitpoints or poisonTurnsLeftPlayer > 0) and playerHeals > 0:
                healButton = button(width / 2, (height / 5) * 3, width / 2, height / 5, (255, 180, 0), (255, 255, 255),"Heal", (0, 0, 0), width // 12, (0, 0, 0))
            else:
                healButton = button(width / 2, (height / 5) * 3, width / 2, height / 5, (100, 40, 0), (100, 40, 0),"Heal", (0, 0, 0), width // 12, (0, 0, 0))
            if len(player.items) > 0:
                itemButton = button(0, (height / 5) * 4, width / 2, height / 5, (255, 180, 0),(255, 255, 255), "Use item", (0, 0, 0), width // 12, (0, 0, 0))
            else:
                itemButton = button(0, (height / 5) * 4, width / 2, height / 5, (100, 40, 0),(100, 40, 0), "Use item", (0, 0, 0), width // 12, (0, 0, 0))
            #checks whether the mousebutton is down
            mouseDown = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
            #the code for when the attackbutton is pressed
            if button.check(attackButton, mouseDown, screen):
                #defining new variables
                draw_scene()
                done = False
                pages = len(player.moveset) // 4
                page = 0
                move = None
                #loop where a move is selected
                while not done:
                    #checks if the mousebutton is down
                    mouseDown = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseDown = True
                    #checks the buttons to change pages
                    if page < pages:
                        if button.check(buttonNextPage, mouseDown, screen):
                            page += 1
                            draw_scene()
                    if page > 0:
                        if button.check(buttonPrevPage, mouseDown, screen):
                            page -= 1
                            draw_scene()
                    #for loop drawing the buttons and checking if theyre pressed
                    for i in range(0, 4):
                        if (page * 4) + i < len(player.moveset):
                            if  player.moveset[page * 4 + i].name == "block" and playerBlocks == 0:
                                moveButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4), int((height / 7) * 2), (100, 40, 0), (100, 40, 0), player.moveset[(page * 4) + i].name, (0, 0, 0), width // 40,(0, 0, 0))
                            else:
                                moveButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4), int((height / 7) * 2), (255, 180, 0), (255, 255, 255), player.moveset[(page * 4) + i].name, (0, 0, 0), width // 40, (0, 0, 0))
                            if button.check(moveButton, mouseDown, screen) and not(player.moveset[page * 4 + i].name == "block" and playerBlocks == 0):
                                move = player.moveset[page * 4 + i].name
                                done = True
                    #checks whether the button to return to the main options is pressed
                    if button.check(buttonBack, mouseDown, screen):
                        done = True
                draw_scene()
                #checks if a move is selected or whether to return to the main options
                if move is not None:
                    #the punch move
                    if move == "punch":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            damage = int(10 * damageMultiplierPlayer)
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                    #the combo punch move
                    elif move == "combo punch":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            done = False
                            while not done:
                                damage = int(3 * damageMultiplierPlayer)
                                enemyCurrentHealth -= damage
                                scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                                if random.randint(0, 2) == 0:
                                    done = True
                    #the enrage move
                    elif move == "enrage":
                        if enrageTurnsLeftPlayer == 0:
                            scrollText("1.5x damage", (255, 0, 0), "player", 40, 20)
                            damageMultiplierPlayer *= 1.5
                        enrageTurnsLeftPlayer = 3
                    #the poison move
                    elif move == "poison":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            roll = random.randint(2, 5)
                            if poisonTurnsLeftEnemy < roll:
                                poisonTurnsLeftEnemy = roll
                            scrollText("poisoned for " + str(poisonTurnsLeftEnemy) + " turns", (255, 0, 255), "enemy", 30, 50)
                    #the life steal move
                    elif move == "life steal":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            damage = int(5 * damageMultiplierPlayer)
                            healed = int(damage * (enemyCurrentHealth / enemy.hitpoints))
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                            if playerCurrentHealth + healed > player.maxHitpoints:
                                healed = player.maxHitpoints - playerCurrentHealth
                                playerCurrentHealth = player.maxHitpoints
                            else:
                                playerCurrentHealth += healed
                            scrollText(str(healed), (0, 255, 0), "player", 80, 20)
                    #the block move
                    elif move == "block":
                        playerBlocks -= 1
                        roll = random.randint(0, 2)
                        if immunityTurnsLeftPlayer < roll:
                            immunityTurnsLeftPlayer = roll
                        if immunityTurnsLeftPlayer > 0:
                           scrollText("immune for " + str(immunityTurnsLeftPlayer) + " turns", (100, 100, 255),
                                           "player", 30, 50)
                        else:
                            scrollText("Block Failed", (255, 0, 0), "player", 40, 20)
                    state = "turnEnemy"
            #the code for when the item button is pressed
            elif button.check(itemButton, mouseDown, screen) and len(player.items) > 0:
                draw_scene()
                done = False
                pages = len(player.items) // 4
                page = 0
                usedItem = None
                # loop where an item can be selected
                while not done:
                    # checks if the mousebutton is down
                    mouseDown = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseDown = True
                    # checks the buttons to change pages
                    if page < pages:
                        if button.check(buttonNextPage, mouseDown, screen):
                            page += 1
                            draw_scene()
                    if page > 0:
                        if button.check(buttonPrevPage, mouseDown, screen):
                            page -= 1
                            draw_scene()
                    # for loop drawing the buttons and checking if they're pressed
                    for i in range(0, 4):
                        if (page * 4) + i < len(player.items):
                            if player.items[page * 4 + i].ammount <= 0:
                                itemButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4), int((height / 7) * 2), (100, 40, 0), (100, 40, 0), player.items[(page * 4) + i].name, (0, 0, 0), width // 40, (0, 0, 0))
                            else:
                                itemButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4), int((height / 7) * 2), (255, 180, 0), (255, 255, 255), player.items[(page * 4) + i].name, (0, 0, 0), width // 40, (0, 0, 0))
                            if button.check(itemButton, mouseDown, screen) and player.items[page * 4 + i].ammount > 0:
                                usedItem = player.items[page * 4 + i].name
                                done = True
                    # checks whether the button to return to the main options is pressed
                    if button.check(buttonBack, mouseDown, screen):
                        done = True
                draw_scene()
                if usedItem is not None:
                    pass
            #the code for when the heal button is pressed
            elif button.check(healButton, mouseDown, screen) and (playerCurrentHealth < player.maxHitpoints or poisonTurnsLeftPlayer > 0) and playerHeals > 0:
                playerHeals -= 1
                healed = 20
                if playerCurrentHealth + healed > player.maxHitpoints:
                    healed = player.maxHitpoints - playerCurrentHealth
                    playerCurrentHealth = player.maxHitpoints
                else:
                    playerCurrentHealth += healed
                scrollText(str(healed), (0, 255, 0), "player", 80, 20)
                state = "turnEnemy"
            #the code for when the flee button is pressed
            elif button.check(fleeButton, mouseDown, screen):
                #defining the variables
                confirmFont = pygame.font.Font("freesansbold.ttf", int(width * 0.02))
                confirmText = confirmFont.render("Are you sure you want to leave?", True, (0, 0, 0))
                confirmRect = confirmText.get_rect()
                confirmRect.center = (width / 2, (height / 12) * 5)
                pygame.draw.rect(screen, (255, 180, 0), [int(width / 3), int(height / 3), int(width / 3), int(height / 3)])
                screen.blit(confirmText, confirmRect)
                confirmed = False
                confirmButton = button(width / 3, height / 2, width / 6, height / 6, (255, 80, 0), (255, 255, 255), "confirm", (0, 0, 0), width // 30,  (0, 0, 0))
                cancelButton = button(width / 2, height / 2, width / 6, height / 6, (255, 80, 0),(255, 255, 255), "cancel", (0, 0, 0), width // 30, (0, 0, 0))
                #while loop checking if they confirm they want to flee
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
            #various checks when the players turn is over
            if state == "turnEnemy":
                #removes a turn if the player is enraged, resets if they are no longer enraged
                if enrageTurnsLeftPlayer > 0:
                    enrageTurnsLeftPlayer -= 1
                    if enrageTurnsLeftPlayer == 0:
                        damageMultiplierPlayer /= 1.5
                #damages and removes a turn if the enemy is poisoned
                if poisonTurnsLeftEnemy > 0 and enemyCurrentHealth > 0:
                    time.sleep(0.5)
                    damage = int(1 / (enemyCurrentHealth / enemy.hitpoints) + 4)
                    enemyCurrentHealth -= damage
                    scrollText(str(damage), (255, 0, 255), "enemy", 80, 20)
                    poisonTurnsLeftEnemy -= 1
                    if poisonTurnsLeftEnemy == 0:
                        time.sleep(0.5)
                        scrollText("poison cleared", (255, 0, 255), "enemy", 40, 40)
                #removes a turn if the enemy is immune
                if immunityTurnsLeftEnemy > 0:
                    immunityTurnsLeftEnemy -= 1
                    if immunityTurnsLeftEnemy == 0:
                        scrollText("No longer immune", (100, 100, 255), "enemy", 40, 40)
                #checks if the enemy is dead
                if enemyCurrentHealth <= 0:
                    enemyCurrentHealth = 0
                    fighting = False
                    state = "gameOver"
                    result = "win"
        #the enemy turn
        elif state == "turnEnemy":
            draw_scene()
            time.sleep(0.5)
            selected = False
            #loop where a move is selected
            while not selected:
                roll = random.randint(0, len(enemy.moveset))
                if roll == len(enemy.moveset):
                    move = "heal"
                else:
                    move = enemy.moveset[roll]
                if (move != "heal" or enemyCurrentHealth < enemy.hitpoints and enemyHeals > 0) and (move!= "block" or enemyBlocks > 0):
                    selected = True
            #the punch move
            if move == "punch":
                if immunityTurnsLeftPlayer > 0:
                    blocked("player")
                else:
                    damage = 10 * damageMultiplierEnemy
                    playerCurrentHealth -= damage
                    scrollText(str(damage), (255, 0, 0), "player", 80, 20)
            #the combo punch move
            elif move == "combo punch":
                if immunityTurnsLeftPlayer > 0:
                    blocked("player")
                else:
                    done = False
                    while not done:
                        damage = int(3 * damageMultiplierEnemy)
                        playerCurrentHealth -= damage
                        scrollText(str(damage), (255, 0, 0), "player", 80, 20)
                        if random.randint(0, 2) == 0:
                            done = True
            #the enrage move
            elif move == "enrage":
                if enrageTurnsLeftEnemy == 0:
                    scrollText("1.5x damage", (255, 0, 0), "enemy", 40, 20)
                    damageMultiplierEnemy *= 1.5
                enrageTurnsLeftEnemy = 3
            #the poison move
            elif move == "poison":
                if immunityTurnsLeftPlayer > 0:
                    blocked("player")
                else:
                    roll = random.randint(2, 5)
                    if poisonTurnsLeftPlayer < roll:
                        poisonTurnsLeftPlayer = roll
                    scrollText("poisoned for " + str(poisonTurnsLeftPlayer) + " turns", (255, 0, 255), "player", 30, 50)
            #the life steal move
            elif move == "life steal":
                if immunityTurnsLeftPlayer > 0:
                    blocked("player")
                else:
                    damage = int(5 * damageMultiplierEnemy)
                    healed = damage * (playerCurrentHealth // player.maxHitpoints)
                    playerCurrentHealth -= damage
                    scrollText(str(damage), (255, 0, 0), "player", 80, 20)
                    if enemyCurrentHealth + healed > enemy.hitpoints:
                        healed = enemy.hitpoints - enemyCurrentHealth
                        enemyCurrentHealth = enemy.hitpoints
                    else:
                        enemyCurrentHealth += healed
                    scrollText(str(healed), (0, 255, 0), "enemy", 80, 20)
            #the block move
            elif move == "block":
                enemyBlocks -= 1
                roll = random.randint(0, 2)
                if immunityTurnsLeftEnemy < roll:
                    immunityTurnsLeftEnemy = roll
                if immunityTurnsLeftEnemy > 0:
                    scrollText("immune for " + str(immunityTurnsLeftEnemy) + " turns", (100, 100, 255), "enemy", 30, 50)
                else:
                    scrollText("Block Failed", (255, 0, 0), "enemy", 40, 20)
            #the heal move
            elif move == "heal":
                enemyHeals -= 1
                healed = 20
                if enemyCurrentHealth + healed > enemy.hitpoints:
                    healed = enemy.hitpoints - enemyCurrentHealth
                    enemyCurrentHealth = enemy.hitpoints
                else:
                    enemyCurrentHealth += healed
                scrollText(str(healed), (0, 255, 0), "enemy", 80, 20)
                if poisonTurnsLeftEnemy > 0:
                    poisonTurnsLeftEnemy = 0
                    scrollText("poison cleared", (0, 255, 0), "enemy", 40, 40)
            #removes a turn if the enemy is enraged and resets if they are no longer enraged
            if enrageTurnsLeftEnemy > 0:
                enrageTurnsLeftEnemy -= 1
                if enrageTurnsLeftEnemy == 0:
                    damageMultiplierEnemy /= 1.5
            #damages the player and removes a turn if theyre poisoned
            if poisonTurnsLeftPlayer > 0 and playerCurrentHealth > 0:
                time.sleep(0.5)
                damage = int(1 / enemyCurrentHealth / enemy.hitpoints + 4)
                playerCurrentHealth -= damage
                scrollText(str(damage), (255, 0, 255), "player", 80, 20)
                poisonTurnsLeftPlayer -= 1
                if poisonTurnsLeftPlayer == 0:
                    time.sleep(0.5)
                    scrollText("poison cleared", (255, 0, 255), "player", 40, 40)
            #removes a turn if the player is immune
            if immunityTurnsLeftPlayer > 0:
                immunityTurnsLeftPlayer -= 1
                if immunityTurnsLeftPlayer == 0:
                    scrollText("No longer immune", (100, 100, 255), "player", 40, 40)
            #checks if the player has died
            if playerCurrentHealth <= 0:
                playerCurrentHealth = 0
                fighting = False
                result = "loss"
            #returns to the player turn
            time.sleep(0.5)
            state = "turnPlayer"
        time.sleep(0.01)
        pygame.display.update()
    #returning the values if the fight is over
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
        player.hitpoints = result[1]
        screen.fill((0, 255, 0))
    elif result[0] == "flee":
        player.hitpoints = result[1]
    elif result[0] == "loss":
        player.hitpoints = 100
        player.lives -= 1

    time.sleep(0.01)
pygame.quit()