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
        textPrint(screen, self.description, 20, 'white', (x, y + 150))
        textPrint(screen, self.name, 35, 'white', (x, y - 200), outline=('black', 2))
        screen.blit(pygame.transform.scale(self.image, (160, 200)), (x - 80, y - 140))


def fight(enemy, player, screen):
    """
    Starts a fight with a given enemy and returns the result
    enemy: an enemy following the enemy class that will be fought
    player: the player following the player class fighting
    screen: the screen where everything should be drawn
    return: a list containing the result of the fight as a string and the hitpoints the player has remaining as an integer
    """
    def draw_scene(Text):
        """
        Draws the fighting scene
        return: none
        """
        #draws the background
        screen.blit(image_background, (0, 0))
        mouse_pillar.draw(screen, 0)
        mouse_pillar.draw_3D_extension(screen, 0)
        enemy_pillar.draw(screen, 0)
        enemy_pillar.draw_3D_extension(screen, 0)
        #draws the player and the enemy
        screen.blit(player.image, (250 - (player.image.width / 2), height / 5 * 3 - player.image.height - 10))
        enemy_image = pygame.transform.scale(enemy.image, (129, 420))
        screen.blit(enemy_image, (1050 - (enemy_image.width / 2), height / 5 * 4.35 - enemy_image.height - 10))
        #draws the name of the player and enemy with a border
        textPrint(screen, player.name, 40, 'black', (250, 150), outline=('white', 2))
        textPrint(screen, enemy.name, 40, 'black', (1050, 150), outline=('white', 2))
        #draws the healthbars
        pygame.draw.rect(screen, 'black', pygame.Rect(145, 175, 210, 60))
        pygame.draw.rect(screen, 'black', pygame.Rect(945, 175, 210, 60))
        pygame.draw.rect(screen, 'red', pygame.Rect(150, 180, 200 * (playerCurrentHealth / player.maxHitpoints), 50))
        pygame.draw.rect(screen, 'red', pygame.Rect(950, 180, 200 * (enemyCurrentHealth / enemy.hitpoints), 50))
        textPrint(screen, str(playerCurrentHealth), 40, 'white', (250, 205))
        textPrint(screen, str(enemyCurrentHealth), 40, 'white', (1050, 205))
        #draws the text on the top of the screen
        textPrint(screen, Text, 70, 'black', (width / 2, 100), outline=('white', 2))

    def scrollText(text, colour, location, size, scrollTime, Fight_Text):
        """
        Scrolls a given text across the screen for a given time
        text: a string of text you want to scroll
        colour: the colour of the text as 3 integers
        location: the location of the text as a string with 2 options: "player" or "enemy"
        size: "the size of the text as an integer"
        scrollTime: the amount of time the text will scroll for as an integer
        Fight_Text: the text at the top middle of the screen
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
            draw_scene(Fight_Text)
            screen.blit(toScrollText, (x, 150 - i))
            pygame.display.update()
            waitTime = 0.01 - (time.time() - timeBegin)
            if waitTime > 0:
                time.sleep(waitTime)
        #resets the screen
        draw_scene(Fight_Text)
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
        blockedImage = pygame.transform.scale(pygame.image.load('resources/textures/move_block_sideProfile.png'),(120, 260))
        #sets the x value and rectangle position depending on the given location
        if location == "player":
            x = 400
        elif location == "enemy":
            x = 900 - 120
            blockedImage = pygame.transform.flip(blockedImage, True, False)
        #for loop where the text is scrolled upwards
        for i in range(0, 20):
            timeBegin = time.time()
            draw_scene("")
            screen.blit(blockedImage, (x, 240))
            screen.blit(blockedText, (x, 150 - i))
            pygame.display.flip()
            waitTime = 0.01 - (time.time() - timeBegin)
            if waitTime > 0:
                time.sleep(waitTime)
        time.sleep(0.5)
        draw_scene("The attack was blocked")
        pygame.display.update()
    #defining the variables before the fight starts
    width = screen.get_width()
    height = screen.get_height()
    mouse_pillar = Objects(125, 400, 250, 500, "pillar", 1, 0, 0, [], "")
    enemy_pillar = Objects(925, 600, 250, 500, "pillar", 1, 0, 0, [], "")
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
    draw_scene("")
    pygame.mixer.stop()
    #pygame.mixer.music.load("resources/sound/battle_theme.mp3")
    pygame.mixer.music.play(-1)
    #the main fighting loop
    while fighting:
        draw_scene("Its your turn")
        Fight_Text = "Its your turn"
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
                draw_scene("Select your attack")
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
                            draw_scene("Select your attack")
                    if page > 0:
                        if button.check(buttonPrevPage, mouseDown, screen):
                            page -= 1
                            draw_scene("Select your attack")
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
                draw_scene("Its your turn")
                Fight_Text = "Its your turn"
                #checks if a move is selected or whether to return to the main options
                if move is not None:
                    draw_scene("You used " + move)
                    Fight_Text = "You used " + move
                    #the punch move
                    if move == "punch":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            damage = int(10 * damageMultiplierPlayer)
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy", 80, 20, Fight_Text)
                    #the combo punch move
                    elif move == "combo punch":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            done = False
                            while not done:
                                damage = int(3 * damageMultiplierPlayer)
                                enemyCurrentHealth -= damage
                                scrollText(str(damage), (255, 0, 0), "enemy", 80, 20, Fight_Text)
                                if random.randint(0, 2) == 0:
                                    done = True
                    #the enrage move
                    elif move == "enrage":
                        if enrageTurnsLeftPlayer == 0:
                            scrollText("1.5x damage", (255, 0, 0), "player", 40, 20, Fight_Text)
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
                            scrollText("poisoned for " + str(poisonTurnsLeftEnemy) + " turns", (255, 0, 255), "enemy", 30, 50, Fight_Text)
                    #the life steal move
                    elif move == "life steal":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            damage = int(8 * damageMultiplierPlayer)
                            healed = int(damage * (enemyCurrentHealth / enemy.maxHitpoints))
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy", 80, 20, Fight_Text)
                            if playerCurrentHealth + healed > player.maxHitpoints:
                                healed = player.maxHitpoints - playerCurrentHealth
                                playerCurrentHealth = player.maxHitpoints
                            else:
                                playerCurrentHealth += healed
                            scrollText(str(healed), (0, 255, 0), "player", 80, 20, Fight_Text)
                    #the block move
                    elif move == "block":
                        playerBlocks -= 1
                        roll = random.randint(0, 2)
                        if immunityTurnsLeftPlayer < roll:
                            immunityTurnsLeftPlayer = roll
                        if immunityTurnsLeftPlayer > 0:
                           scrollText("immune for " + str(immunityTurnsLeftPlayer) + " turns", (100, 100, 255),
                                           "player", 30, 50, Fight_Text)
                        else:
                            scrollText("Block Failed", (255, 0, 0), "player", 40, 20, Fight_Text)
                #Instakill move for testing purposes
                    elif move == "devtest instakill":
                        enemyCurrentHealth -= 1000
                    state = "turnEnemy"
            #the code for when the item button is pressed
            elif button.check(itemButton, mouseDown, screen) and len(player.items) > 0:
                draw_scene("Select an item")
                Fight_Text = "Select an item"
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
                            draw_scene("Select an item")
                            Fight_Text = "Select an item"
                    if page > 0:
                        if button.check(buttonPrevPage, mouseDown, screen):
                            page -= 1
                            draw_scene("Select an item")
                            Fight_Text = "Select an item"
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

                #checks whether an item has been selected or whether to return to main options
                if usedItem is not None:
                    draw_scene("You used an item: " + usedItem)
                    Fight_Text = "You used an item: " + usedItem
                    #the Full Restore item
                    if usedItem == "Full Restore":
                        healed = player.maxHitpoints - playerCurrentHealth
                        playerCurrentHealth = player.maxHitpoints
                        scrollText(str(healed), (0, 255, 0), "player", 80, 20, Fight_Text)
                        if poisonTurnsLeftPlayer > 0:
                            poisonTurnsLeftPlayer = 0
                            scrollText("poison cleared", (255, 0, 255), "player", 40, 40, Fight_Text)
                    #the Bomb item
                    elif usedItem == "Bomb":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            enemyCurrentHealth -= 20
                            scrollText("20", (255, 0, 0), "enemy", 80, 20, Fight_Text)
                    #the Poison bottle item
                    elif usedItem == "Poison bottle":
                        poisonTurnsLeftEnemy = 5
                        scrollText("Poisoned for 5 turns", (255, 0, 255), "enemy", 30, 50, Fight_Text)
                    #the Immunizing elixir item
                    elif usedItem == "Immunizing elixir":
                        immunityTurnsLeftPlayer = 3
                        scrollText("Immune for 3 turns", (100, 100, 255), "player", 30, 50, Fight_Text)
                    #the Giantkiller item
                    elif usedItem == "Giantkiller":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            damage = int(0.3 * enemy.maxHitpoints)
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy", 80, 20, Fight_Text)
                    #the Orb of absorption item
                    elif usedItem == "Orb of absorption":
                        if immunityTurnsLeftEnemy > 0:
                            blocked("enemy")
                        else:
                            damage = int(30 * (enemyCurrentHealth / enemy.maxHitpoints))
                            enemyCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "enemy", 80, 20, Fight_Text)
                            healed = int(0.5 * damage)
                            if playerCurrentHealth + healed > player.maxHitpoints:
                                healed = player.maxHitpoints - playerCurrentHealth
                                playerCurrentHealth = player.maxHitpoints
                            else:
                                playerCurrentHealth += healed
                            scrollText(str(healed), (0, 255, 0), "player", 80, 20, Fight_Text)
                        time.sleep(1.5)
            #the code for when the heal button is pressed
            elif button.check(healButton, mouseDown, screen) and (playerCurrentHealth < player.maxHitpoints or poisonTurnsLeftPlayer > 0) and playerHeals > 0:
                playerHeals -= 1
                healed = 20
                if playerCurrentHealth + healed > player.maxHitpoints:
                    healed = player.maxHitpoints - playerCurrentHealth
                    playerCurrentHealth = player.maxHitpoints
                else:
                    playerCurrentHealth += healed
                draw_scene("You healed")
                Fight_Text = "You healed"
                scrollText(str(healed), (0, 255, 0), "player", 80, 20, Fight_Text)
                state = "turnEnemy"
                if poisonTurnsLeftPlayer > 0:
                    poisonTurnsLeftPlayer = 0
                    scrollText("poison cleared", (255, 0, 255), "player", 40, 40, Fight_Text)
            #the code for when the flee button is pressed
            elif button.check(fleeButton, mouseDown, screen):
                #defining the variables
                dimSurface = pygame.Surface((WIDTH, HEIGHT))
                pygame.Surface.set_alpha(dimSurface, 150)
                pygame.Surface.blit(screen, dimSurface)
                pygame.draw.rect(screen, (255, 180, 0), [width / 3, height / 3, width / 3, height / 3])
                textPrint(screen,"Are you sure you want to leave?", int(width * 0.02), 'black', (width / 2, height / 12 * 5))
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
                    draw_scene("")
                    Fight_Text = ""
            #draws the number of heals you have left
            font = pygame.font.Font(mainFont, 40)
            healAmmountText = font.render(str(playerHeals), True, (0, 0, 0))
            screen.blit(healAmmountText, (int(width) - healAmmountText.get_rect().width - 15, int((height / 5) * 3) + 15))
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
                    scrollText(str(damage), (255, 0, 255), "enemy", 80, 20, Fight_Text)
                    poisonTurnsLeftEnemy -= 1
                    if poisonTurnsLeftEnemy == 0:
                        time.sleep(0.5)
                        scrollText("poison cleared", (255, 0, 255), "enemy", 40, 40, Fight_Text)
                #removes a turn if the enemy is immune
                if immunityTurnsLeftEnemy > 0:
                    immunityTurnsLeftEnemy -= 1
                    if immunityTurnsLeftEnemy == 0:
                        scrollText("No longer immune", (100, 100, 255), "enemy", 40, 40, Fight_Text)
            #checks if the enemy is dead
            if enemyCurrentHealth <= 0:
                enemyCurrentHealth = 0
                fighting = False
                state = "gameOver"
                result = "win"
        #the enemy turn
        elif state == "turnEnemy":
            draw_scene("The enemy's turn")
            Fight_Text = "The enemy's turn"
            pygame.display.update()
            time.sleep(1)
            selected = False
            #rolls whether the enemy should use an item and selects it
            if random.randint(0, 2) != 0 and len(enemyItems) > 0:
                roll = random.randint(0, len(enemyItems) - 1)
                if enemyItems[roll].amount > 0:
                    usedItem = enemyItems[roll].name
                    draw_scene("They used an item: " + usedItem)
                    Fight_Text = "They used an item: " + usedItem
                    pygame.display.update()
                else:
                    usedItem = None
                #checks whether the enemy "should" use full restore
                if usedItem != "Full Restore" or enemyCurrentHealth < enemy.maxHitpoints - 20:
                    enemyItems[roll].amount -= 1
                    #the Full Restore item
                    if usedItem == "Full Restore":
                        healed = enemy.maxHitpoints - enemyCurrentHealth
                        enemyCurrentHealth = enemy.maxHitpoints
                        scrollText(str(healed), (0, 255, 0), "enemy", 80, 20, Fight_Text)
                        if poisonTurnsLeftEnemy > 0:
                            poisonTurnsLeftEnemy = 0
                            scrollText("poison cleared", (255, 0, 255), "enemy", 40, 40, Fight_Text)
                    #the Bomb item
                    elif usedItem == "Bomb":
                        if immunityTurnsLeftPlayer > 0:
                            blocked("player")
                        else:
                            playerCurrentHealth -= 20
                            scrollText("20", (255, 0, 0), "player", 80, 20, Fight_Text)
                    #the Poison bottle item
                    elif usedItem == "Poison bottle":
                        poisonTurnsLeftPlayer = 5
                        scrollText("Poisoned for 5 turns", (255, 0, 255), "player", 30, 50, Fight_Text)
                    #the Immunizing elixir item
                    elif usedItem == "Immunizing elixir":
                        immunityTurnsLeftEnemy = 3
                        scrollText("Immune for 3 turns", (100, 100, 255), "enemy", 30, 50, Fight_Text)
                    #the Giantkiller item
                    elif usedItem == "Giantkiller":
                        if immunityTurnsLeftPlayer > 0:
                            blocked("player")
                        else:
                            damage = int(0.3 * player.maxHitpoints)
                            playerCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "player", 80, 20, Fight_Text)
                    #the Orbs of absorption item
                    elif usedItem == "Orb of absorption":
                        if immunityTurnsLeftPlayer > 0:
                            blocked("player")
                        else:
                            damage = int(30 * (playerCurrentHealth / player.maxHitpoints))
                            playerCurrentHealth -= damage
                            scrollText(str(damage), (255, 0, 0), "player", 80, 20, Fight_Text)
                            healed = int(0.5 * damage)
                            if enemyCurrentHealth + healed > enemy.maxHitpoints:
                                healed = enemy.maxHitpoints - enemyCurrentHealth
                                enemyCurrentHealth = enemy.maxHitpoints
                            else:
                                enemyCurrentHealth += healed
                            scrollText(str(healed), (0, 255, 0), "enemy", 80, 20, Fight_Text)

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
            draw_scene("They used " + move)
            Fight_Text = "They used " + move
            pygame.display.update()
            time.sleep(0.5)
            if move == "punch":
                if immunityTurnsLeftPlayer > 0:
                    blocked("player")
                else:
                    damage = int(10 * damageMultiplierEnemy)
                    playerCurrentHealth -= damage
                    scrollText(str(damage), (255, 0, 0), "player", 80, 20, Fight_Text)
            #the combo punch move
            elif move == "combo punch":
                if immunityTurnsLeftPlayer > 0:
                    blocked("player")
                else:
                    done = False
                    while not done:
                        damage = int(3 * damageMultiplierEnemy)
                        playerCurrentHealth -= damage
                        scrollText(str(damage), (255, 0, 0), "player", 80, 20, Fight_Text)
                        if random.randint(0, 2) == 0:
                            done = True
            #the enrage move
            elif move == "enrage":
                if enrageTurnsLeftEnemy == 0:
                    scrollText("1.5x damage", (255, 0, 0), "enemy", 40, 20, Fight_Text)
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
                    scrollText("poisoned for " + str(poisonTurnsLeftPlayer) + " turns", (255, 0, 255), "player", 30, 50, Fight_Text)
            #the life steal move
            elif move == "life steal":
                if immunityTurnsLeftPlayer > 0:
                    blocked("player")
                else:
                    damage = int(8 * damageMultiplierEnemy)
                    healed = int(damage * (playerCurrentHealth / player.maxHitpoints))
                    playerCurrentHealth -= damage
                    scrollText(str(damage), (255, 0, 0), "player", 80, 20, Fight_Text)
                    if enemyCurrentHealth + healed > enemy.hitpoints:
                        healed = enemy.hitpoints - enemyCurrentHealth
                        enemyCurrentHealth = enemy.hitpoints
                    else:
                        enemyCurrentHealth += healed
                    scrollText(str(healed), (0, 255, 0), "enemy", 80, 20, Fight_Text)
            #the block move
            elif move == "block":
                enemyBlocks -= 1
                roll = random.randint(0, 2)
                if immunityTurnsLeftEnemy < roll:
                    immunityTurnsLeftEnemy = roll
                if immunityTurnsLeftEnemy > 0:
                    scrollText("immune for " + str(immunityTurnsLeftEnemy) + " turns", (100, 100, 255), "enemy", 30, 50, Fight_Text)
                else:
                    scrollText("Block Failed", (255, 0, 0), "enemy", 40, 20, Fight_Text)
            #the heal move
            elif move == "heal":
                enemyHeals -= 1
                healed = 20
                if enemyCurrentHealth + healed > enemy.hitpoints:
                    healed = enemy.hitpoints - enemyCurrentHealth
                    enemyCurrentHealth = enemy.hitpoints
                else:
                    enemyCurrentHealth += healed
                scrollText(str(healed), (0, 255, 0), "enemy", 80, 20, Fight_Text)
                if poisonTurnsLeftEnemy > 0:
                    poisonTurnsLeftEnemy = 0
                    scrollText("poison cleared", (0, 255, 0), "enemy", 40, 40, Fight_Text)
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
                scrollText(str(damage), (255, 0, 255), "player", 80, 20, Fight_Text)
                poisonTurnsLeftPlayer -= 1
                if poisonTurnsLeftPlayer == 0:
                    time.sleep(0.5)
                    scrollText("poison cleared", (255, 0, 255), "player", 40, 40, Fight_Text)
            #removes a turn if the player is immune
            if immunityTurnsLeftPlayer > 0:
                immunityTurnsLeftPlayer -= 1
                if immunityTurnsLeftPlayer == 0:
                    scrollText("No longer immune", (100, 100, 255), "player", 40, 40, Fight_Text)
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
    if result == "loss":
        draw_scene("You lost")
        pygame.display.update()
        time.sleep(2)
    elif result == "win":
        draw_scene("You won!")
        pygame.display.update()
        time.sleep(2)
    return result, playerCurrentHealth, playerItems

def chooseNewAttack(allMovesList, player, background_surface):
    """
    Displays 3 moves the player can choose from to add to their deck
    :param options: list of 3 moves the player can choose from
    :return: the chosen move or the new state
    """
    allMoves = allMovesList
    # Tekent de 3 opties als kaarten
    if len(allMoves) != len(player.moveset):
        options = []
        for i in range(3):
            while True:
                move = random.randint(0, len(allMoves) - 1)
                if not allMoves[move] in player.moveset or len(allMoves) == len(player.moveset):
                    break
            options.append(allMoves[move])
            allMoves.pop(move)

        buttonList = []
        for i in range(len(options)):
            buttonList.append(button(WIDTH/2 + 328 * (i - 1) - 105, 620, 210, 80, (0, 0, 255), (255, 0, 0), "Choose", 'white', 50, 'white'))

        dimSurface = pygame.Surface((WIDTH, HEIGHT))
        pygame.Surface.set_alpha(dimSurface, 100)
        # Loop waarin gekeken wordt welke knop wordt ingedrukt
        while True:
            screen.blit(background_surface)
            pygame.Surface.blit(screen, dimSurface)
            textPrint(screen,"CHOOSE A NEW ATTACK", 50, 'black', (700, 80), outline=('white', 2))
            for i in range(len(options)):
                options[i].displayMove(WIDTH / 2 + 328 * (i - 1), HEIGHT / 2 - 20)
            index = waitForInput(buttonList, True)
            if index == -1:
                if Pause() == "Menu":
                    return "Menu"
            else:
                return options[index]
    else:
        return None
