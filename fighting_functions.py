from common import *
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()

class item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

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
        # Print de tekst op de kaart
        textPrint(self.description, 20, 'white', (x, y + 150))
        textPrint(self.name, 35, 'white', (x, y - 200), outline=('black', 2))
        screen.blit(pygame.transform.scale(self.image, (160, 200)), (x - 80, y - 140))


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
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (40, 255, 255), (0, 0, width, (height / 10) * 5))
        #draws the player and the enemy
        screen.blit(player.image, (250 - (player.image.width / 2), height / 5 * 3 - player.image.height - 10))
        enemy_image = pygame.transform.scale(enemy.image, (129, 420))
        screen.blit(enemy_image, (1050 - (enemy_image.width / 2), height / 5 * 4.35 - enemy_image.height - 10))
        #draws the name of the player and enemy with a border
        textPrint(player.name, 40, 'black', (250, 150), outline=('white', 2))
        textPrint(enemy.name, 40, 'black', (1050, 150), outline=('white', 2))
        #draws the healthbars
        pygame.draw.rect(screen, 'black', pygame.Rect(145, 175, 210, 60))
        pygame.draw.rect(screen, 'black', pygame.Rect(945, 175, 210, 60))
        pygame.draw.rect(screen, 'red', pygame.Rect(150, 180, 200 * (playerCurrentHealth / player.maxHitpoints), 50))
        pygame.draw.rect(screen, 'red', pygame.Rect(950, 180, 200 * (enemyCurrentHealth / enemy.hitpoints), 50))
        textPrint(str(playerCurrentHealth), 40, 'white', (250, 205))
        textPrint(str(enemyCurrentHealth), 40, 'white', (1050, 205))
    def scrollText(text, colour, location, size, scrollTime):
        """
        Scrolls a given text across the screen for a given time
        text: a string of text you want to scroll
        colour: the colour of the text as 3 integers
        location: the location of the text as a string with 2 options: "player" or "enemy"
        size: "the size of the text as an integer"
        scrollTime: the amount of time the text will scroll for as an integer
        return: none
        """
        #sets the text to be scrolled
        font = pygame.font.Font(mainFont, size)
        toScrollText = font.render(text, True, colour)
        #defines the x value depending on the given location
        if location == "player":
            x = 400
        elif location == "enemy":
            x = 900 - toScrollText.get_rect().width
        #for loop where the text is slowly moved upwards
        for i in range(0, scrollTime):
            timeBegin = time.time()
            draw_scene()
            screen.blit(toScrollText, (x, 150 - i))
            pygame.display.update()
            waitTime = 0.01 - (time.time() - timeBegin)
            if waitTime > 0:
                time.sleep(waitTime)
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
        font = pygame.font.Font(mainFont, 40)
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
            timeBegin = time.time()
            draw_scene()
            pygame.draw.rect(screen, (100, 100, 255), blockedRect)
            screen.blit(blockedText, (x, 150 - i))
            pygame.display.update()
            waitTime = 0.01 - (time.time() - timeBegin)
            if waitTime > 0:
                time.sleep(waitTime)
        time.sleep(0.5)
        draw_scene()
        pygame.display.update()
    #defining the variables before the fight starts
    width = screen.get_width()
    height = screen.get_height()
    attackButton = button(0, (height / 5) * 3, width / 2 + 1, height/5 + 1, (255, 180, 0), (255, 255, 255), "Attack", (0, 0, 0), width // 12, (0, 0, 0))
    itemButton = button(0, (height / 5) * 4, width / 2 + 1, height / 5 + 1, (255, 180, 0), (255, 255, 255), "Use item",(0, 0, 0), width // 12, (0, 0, 0))
    fleeButton = button(width / 2, (height / 5) * 4, width / 2 + 1, height / 5 + 1, (255, 80, 0), (255, 255, 255), "Flee", (0, 0, 0), width // 12,  (0, 0, 0))
    buttonNextPage = button(width / 2, (height / 7) * 6, width / 2 + 1, height / 7 + 1, (255, 180, 0), (255, 255, 255), "Next page", (0, 0, 0), width // 30, (0, 0, 0))
    buttonPrevPage = button(0, (height / 7) * 6, width / 2 + 1, height / 7 + 1, (255, 180, 0), (255, 255, 255), "Previous page",(0, 0, 0), width // 30, (0, 0, 0))
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
    playerItems = player.items
    enemyItems = enemy.items
    fighting = True
    state = "turnPlayer"
    draw_scene()
    #the main fighting loop
    while fighting:
        #the players turn
        if state == "turnPlayer":
            #sets the texture of the buttons depending on whether its an available option or not
            if (playerCurrentHealth < player.maxHitpoints or poisonTurnsLeftPlayer > 0) and playerHeals > 0:
                healButton = button(width / 2, (height / 5) * 3, width / 2 + 1, height / 5 + 1, (255, 180, 0), (255, 255, 255),"Heal", (0, 0, 0), width // 12, (0, 0, 0))
            else:
                healButton = button(width / 2, (height / 5) * 3, width / 2 + 1, height / 5 + 1, (100, 40, 0), (100, 40, 0),"Heal", (0, 0, 0), width // 12, (0, 0, 0))
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
                pages = (len(player.moveset) - 1) // 4
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
                                moveButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4) + 1, int((height / 7) * 2) + 1, (100, 40, 0), (100, 40, 0), player.moveset[(page * 4) + i].name, (0, 0, 0), width // 40,(0, 0, 0))
                            else:
                                moveButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4) + 1, int((height / 7) * 2) + 1, (255, 180, 0), (255, 255, 255), player.moveset[(page * 4) + i].name, (0, 0, 0), width // 40, (0, 0, 0))
                            if button.check(moveButton, mouseDown, screen) and not(player.moveset[page * 4 + i].name == "block" and playerBlocks == 0):
                                move = player.moveset[page * 4 + i].name
                                done = True
                    #checks whether the button to return to the main options is pressed
                    if button.check(buttonBack, mouseDown, screen):
                        done = True
                    pygame.display.update()
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
                            damage = int(8 * damageMultiplierPlayer)
                            healed = int(damage * (enemyCurrentHealth / enemy.maxHitpoints))
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
                #Instakill move for testing purposes
                    elif move == "devtest instakill":
                        enemyCurrentHealth -= 1000
                    state = "turnEnemy"
            #the code for when the item button is pressed
            elif button.check(itemButton, mouseDown, screen) and len(player.items) > 0:
                draw_scene()
                done = False
                pages = len(playerItems) - 1 // 4
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
                        if (page * 4) + i < len(playerItems):
                            font = pygame.font.Font(mainFont, 40)
                            amountText = font.render(str(playerItems[page * 4 + i].amount), True, (0, 0, 0))
                            if playerItems[page * 4 + i].amount <= 0 or playerItems[page * 4 + i].name == "Full Restore" and not(playerCurrentHealth < player.maxHitpoints or poisonTurnsLeftPlayer > 0):
                                selectItemButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4) + 1, int((height / 7) * 2) + 1, (100, 40, 0), (100, 40, 0), playerItems[(page * 4) + i].name, (0, 0, 0), width // 40, (0, 0, 0))
                            else:
                                selectItemButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4) + 1, int((height / 7) * 2) + 1, (255, 180, 0), (255, 255, 255), playerItems[(page * 4) + i].name, (0, 0, 0), width // 40, (0, 0, 0))
                            if button.check(selectItemButton, mouseDown, screen) and playerItems[page * 4 + i].amount > 0 and (playerItems[page * 4 + i].name != "Full Restore" or playerCurrentHealth < player.maxHitpoints or poisonTurnsLeftPlayer > 0):
                                usedItem = playerItems[page * 4 + i].name
                                playerItems[page * 4 + i].amount -= 1
                                done = True
                            screen.blit(amountText, (int((width / 4) * (i + 1)) - amountText.get_rect().width - 15, int((height / 7) * 4) + 15))
                    # checks whether the button to return to the main options is pressed
                    if button.check(buttonBack, mouseDown, screen):
                        done = True
                    pygame.display.update()
                draw_scene()
                #checks whether an item has been selected or whether to return to main options
                if usedItem is not None:
                    #the Full Restore item
                    if usedItem == "Full Restore":
                        healed = player.maxHitpoints - playerCurrentHealth
                        playerCurrentHealth = player.maxHitpoints
                        scrollText(str(healed), (0, 255, 0), "player", 80, 20)
                        if poisonTurnsLeftPlayer > 0:
                            poisonTurnsLeftPlayer = 0
                            scrollText("poison cleared", (255, 0, 255), "player", 40, 40)
                    #the Bomb item
                    elif usedItem == "Bomb":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            enemyCurrentHealth -= 20
                            scrollText("20", (255, 0, 0), "enemy", 80, 20)
                    #the Poison bottle item
                    elif usedItem == "Poison bottle":
                        poisonTurnsLeftEnemy = 5
                        scrollText("Poisoned for 5 turns", (255, 0, 255), "enemy", 30, 50)
                    #the Immunizing elixir item
                    elif usedItem == "Immunizing elixir":
                        immunityTurnsLeftPlayer = 3
                        scrollText("Immune for 3 turns", (100, 100, 255), "player", 30, 50)
                    #the Giantkiller item
                    elif usedItem == "Giantkiller":
                        damage = int(0.3 * enemy.maxHitpoints)
                        enemyCurrentHealth -= damage
                        scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                    #the Orb of absorption item
                    elif usedItem == "Orb of absorption":
                        damage = int(30 * (enemyCurrentHealth / enemy.maxHitpoints))
                        enemyCurrentHealth -= damage
                        scrollText(str(damage), (255, 0, 0), "enemy", 80, 20)
                        healed = int(0.5 * damage)
                        if playerCurrentHealth + healed > player.maxHitpoints:
                            healed = player.maxHitpoints - playerCurrentHealth
                            playerCurrentHealth = player.maxHitpoints
                        else:
                            playerCurrentHealth += healed
                        scrollText(str(healed), (0, 255, 0), "player", 80, 20)
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
                if poisonTurnsLeftPlayer > 0:
                    poisonTurnsLeftPlayer = 0
                    scrollText("poison cleared", (255, 0, 255), "player", 40, 40)
            #the code for when the flee button is pressed
            elif button.check(fleeButton, mouseDown, screen):
                #defining the variables
                dimSurface = pygame.Surface((WIDTH, HEIGHT))
                pygame.Surface.set_alpha(dimSurface, 150)
                pygame.Surface.blit(screen, dimSurface)
                pygame.draw.rect(screen, (255, 180, 0), [width / 3, height / 3, width / 3, height / 3])
                textPrint("Are you sure you want to leave?", int(width * 0.02), 'black', (width / 2, height / 12 * 5))
                confirmButton = button(width / 3, height / 2, round(width / 6), round(height / 6), (255, 80, 0),
                                       (255, 255, 255), "confirm", (0, 0, 0), width // 30, (0, 0, 0))
                cancelButton = button(width / 2, height / 2, round(width / 6), round(height / 6), (255, 80, 0),
                                      (255, 255, 255), "cancel", (0, 0, 0), width // 30, (0, 0, 0))
                # while loop checking if they confirm they want to flee
                index = waitForInput([confirmButton, cancelButton])
                if index == 0:
                    fighting = False
                    result = "Playing"
                else:
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
            #rolls whether the enemy should use an item and selects it
            if random.randint(0, 2) != 0 and len(enemyItems) > 0:
                roll = random.randint(0, len(enemyItems) - 1)
                if enemyItems[roll].amount > 0:
                    usedItem = enemyItems[roll].name
                else:
                    usedItem = None
                #checks whether the enemy "should" use full restore
                if usedItem != "Full Restore" or enemyCurrentHealth < enemy.maxHitpoints - 20:
                    enemyItems[roll].amount -= 1
                    #the Full Restore item
                    if usedItem == "Full Restore":
                        healed = enemy.maxHitpoints - enemyCurrentHealth
                        enemyCurrentHealth = enemy.maxHitpoints
                        scrollText(str(healed), (0, 255, 0), "enemy", 80, 20)
                        if poisonTurnsLeftEnemy > 0:
                            poisonTurnsLeftEnemy = 0
                            scrollText("poison cleared", (255, 0, 255), "enemy", 40, 40)
                    #the Bomb item
                    elif usedItem == "Bomb":
                        if immunityTurnsLeftPlayer > 0:
                            blocked("player")
                        else:
                            playerCurrentHealth -= 20
                            scrollText("20", (255, 0, 0), "player", 80, 20)
                    #the Poison bottle item
                    elif usedItem == "Poison bottle":
                        poisonTurnsLeftPlayer = 5
                        scrollText("Poisoned for 5 turns", (255, 0, 255), "player", 30, 50)
                    #the Immunizing elixir item
                    elif usedItem == "Immunizing elixir":
                        immunityTurnsLeftEnemy = 3
                        scrollText("Immune for 3 turns", (100, 100, 255), "enemy", 30, 50)
                    #the Giantkiller item
                    elif usedItem == "Giantkiller":
                        damage = int(0.3 * player.maxHitpoints)
                        playerCurrentHealth -= damage
                        scrollText(str(damage), (255, 0, 0), "player", 80, 20)
                    #the Orbs of absorption item
                    elif usedItem == "Orb of absorption":
                        damage = int(30 * (playerCurrentHealth / player.maxHitpoints))
                        playerCurrentHealth -= damage
                        scrollText(str(damage), (255, 0, 0), "player", 80, 20)
                        healed = int(0.5 * damage)
                        if enemyCurrentHealth + healed > enemy.maxHitpoints:
                            healed = enemy.maxHitpoints - enemyCurrentHealth
                            enemyCurrentHealth = enemy.maxHitpoints
                        else:
                            enemyCurrentHealth += healed
                        scrollText(str(healed), (0, 255, 0), "enemy", 80, 20)
                    time.sleep(0.5)
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
                    damage = int(10 * damageMultiplierEnemy)
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
                    damage = int(8 * damageMultiplierEnemy)
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
            #damages the player and removes a turn if they're poisoned
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
    return result, playerCurrentHealth, playerItems

def chooseNewAttack(allMovesList, player):
    """
    Displays 3 moves the player can choose from to add to their deck
    :param options: list of 3 moves the player can choose from
    :return: the chosen move or the new state
    """
    allMoves = allMovesList
    # Tekent de 3 opties als kaarten
    if len(allMoves) != len(player.moveset):
        screen.fill((100, 100, 100))
        options = []
        for i in range(3):
            selected = False
            while not selected:
                selected = True
                move = random.randint(0, len(allMoves) - 1)
                for i in range(len(player.moveset)):
                    if allMoves[move] == player.moveset[i]:
                        selected = False
                if selected:
                    options.append(allMoves[move])
                    allMoves.pop(move)
                if len(allMoves) == len(player.moveset):
                    selected = True
        buttonList = []
        for i in range(len(options)):
            options[i].displayMove(WIDTH/2 + 328 * (i - 1), HEIGHT/2 - 50)
            buttonList.append(button(WIDTH/2 + 328 * (i - 1) - 105, 590, 210, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white'))
        # Loop waarin gekeken wordt welke knop wordt ingedrukt
        while True:
            index = waitForInput(buttonList, True)
            if index == -1:
                if Pause() == "Menu":
                    return "Menu"
            else:
                return options[index]
    else:
        return None
