import pygame
import time

class player:
    def __init__(self, name, colour, hitpoints, moveset, items):
        self.name = name
        self.colour = colour
        self.hitpoints = hitpoints
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

class button:
    def __init__(self, x, y, width, height, colourNormal, colourHover, text, textColour, textSize, borderColour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colourNormal = colourNormal
        self.colourHover = colourHover
        self.text = text
        self.textColour = textColour
        self.textSize = textSize
        self.borderColour = borderColour
punch = move("punch", "Hits the opponent for 10 damage")
comboPunch = move("combo punch", "Hits the opponent a random number of times")
enrage = move("enrage", "Increases your damage on the next 3 turns")
poison = move("poison", "poisons your opponent to take damage over time")
lifeSteal = move("life steal", "Damages your opponent and gives you 30% back as health")
block = move("block", "Blocks your opponents next attack")

player = player("greg", (0, 0, 255), 100, [punch, comboPunch, enrage, poison, lifeSteal, block], [])

running = True
mouseDown = False
health = 100
enemy1 = enemy("Bob", (0, 0, 255), 100, ["punch", "heal"])
enemy2 = enemy("ASHRddgteGEtek, destroyer of lightbulbs", (255, 0, 255), 500, ["punch", "combo punch", "enrage"])
buttonEnemy1 = button(100, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy1", (255, 255, 255), 80,  (255, 0, 0))
buttonEnemy2 = button(800, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy2", (255, 255, 255), 80, (255, 0, 0))

def buttonCheck(button, mouse, mouseDown):
    font = pygame.font.Font("freesansbold.ttf", button.textSize)
    text = font.render(button.text, True, button.textColour)
    pygame.draw.rect(screen, button.borderColour, [button.x, button.y, button.width, button.height])
    if button.width < button.height:
        borderSize = button.width / 20
    else:
        borderSize = button.height / 20
    if button.x <= mouse[0] <= button.x + button.width and button.y <= mouse[1] <= button.y + button.height:
        pygame.draw.rect(screen, button.colourHover, [int(button.x + borderSize), int(button.y + borderSize), int(button.width - (2 * borderSize)), int(button.height - (2 * borderSize))])
    else:
        pygame.draw.rect(screen, button.colourNormal, [int(button.x + borderSize), int(button.y + borderSize), int(button.width - (2 * borderSize)), int(button.height - (2 * borderSize))])
    textRect = text.get_rect()
    textRect.center = (button.x + (button.width / 2), button.y + (button.height / 2))
    screen.blit(text, textRect)
    pygame.display.update()
    if button.x <= mouse[0] <= button.x + button.width and button.y <= mouse[1] <= button.y + button.height and mouseDown == True:
        return True
    else:
        return False

def fight(enemy, player):
    def draw_scene():
        screen.fill((40, 255, 255))
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enemy.colour, pygame.Rect(1000, 250, 100, 200))
        healthTextPlayer = healthFont.render(str(playerCurrentHealth) + "/" + str(player.hitpoints), True, (255, 255, 255))
        healthTextPlayerRect = healthTextPlayer.get_rect()
        healthTextPlayerRect.center = (250, 200)
        screen.blit(healthTextPlayer, healthTextPlayerRect)
        healthTextEnemy = healthFont.render(str(enemyHealth) + "/" + str(enemy.hitpoints), True, (255, 255, 255))
        healthTextEnemyRect = healthTextEnemy.get_rect()
        healthTextEnemyRect.center = (1050, 200)
        screen.blit(healthTextEnemy, healthTextEnemyRect)
        pygame.display.update()
    width = screen.get_width()
    height = screen.get_height()
    attackButton = button(0, int((height / 5) * 3), int(width / 2), int(height/5), (255, 180, 0), (255, 255, 255), "Attack", (0, 0, 0), int(width / 12), (0, 0, 0))
    itemButton = button(0, int((height / 5) * 4), int(width / 2), int(height / 5), (255, 180, 0), (255, 255, 255), "Use item", (0, 0, 0), int(width / 12),  (0, 0, 0))
    healButton = button(width / 2, int((height / 5) * 3), int(width / 2), int(height / 5), (255, 180, 0), (255, 255, 255),"Heal", (0, 0, 0), int(width / 12), (0, 0, 0))
    fleeButton = button(width / 2, int((height / 5) * 4), int(width / 2), int(height / 5), (255, 80, 0), (255, 255, 255), "Flee", (0, 0, 0), int(width / 12),  (0, 0, 0))
    playerCurrentHealth = player.hitpoints
    enemyHealth = enemy.hitpoints
    fighting = True
    state = "turnPlayer"
    draw_scene()
    while fighting:
        mouse = pygame.mouse.get_pos()
        if state == "turnPlayer":
            mouseDown = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
            if buttonCheck(attackButton, mouse, mouseDown):
                draw_scene()
                buttonNextPage = button(int(width / 2), int((height / 7) * 6), int(width / 2), int(height / 7), (255, 180, 0), (255, 255, 255), "Next page", (0, 0, 0), int(width / 30), (0, 0, 0))
                buttonPrevPage = button(0, int((height / 7) * 6), int(width / 2), int(height / 7), (255, 180, 0), (255, 255, 255), "Previous page", (0, 0, 0), int(width / 30), (0, 0, 0))
                buttonBack = button(0, 0, int(width / 5), int(height / 7), (255, 180, 0), (255, 255, 255), "Back", (0, 0, 0), int(width / 25), (0, 0, 0))
                done = False
                pages = int(len(player.moveset) / 4)
                page = 0
                while not done:
                    mouse = pygame.mouse.get_pos()
                    mouseDown = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseDown = True
                    if page < pages:
                        if buttonCheck(buttonNextPage, mouse, mouseDown):
                            page += 1
                            draw_scene()
                    if page > 0:
                        if buttonCheck(buttonPrevPage, mouse, mouseDown):
                            page -= 1
                            draw_scene()
                    for i in range(0, 4):
                        if (page * 4) + i < len(player.moveset):
                            moveButton = button(int((width / 4) * i), int((height / 7) * 4), int(width / 4), int((height / 7) * 2), (255, 180, 0), (255, 255, 255), player.moveset[(page * 4) + i].name, (0, 0, 0), int(width / 40), (0, 0, 0))
                            if buttonCheck(moveButton, mouse, mouseDown):
                                move = player.moveset[i].name
                                done = True
                    if buttonCheck(buttonBack, mouse, mouseDown):
                        done = True
                draw_scene()
            elif buttonCheck(itemButton, mouse, mouseDown):
                pass
            elif buttonCheck(healButton, mouse, mouseDown):
                playerCurrentHealth += 20
                if playerCurrentHealth > player.hitpoints:
                    playerCurrentHealth = player.hitpoints
                state = "turnEnemy"
            elif buttonCheck(fleeButton, mouse, mouseDown):
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
                    if buttonCheck(confirmButton, mouse, mouseDown):
                        fighting = False
                        result = "flee"
                        confirmed = True
                    elif buttonCheck(cancelButton, mouse, mouseDown):
                        confirmed = True
                        draw_scene()
        elif state == "turnEnemy":
            draw_scene()
            time.sleep(1)
            state = "turnPlayer"
        time.sleep(0.01)
        pygame.display.update()
    if result == "win":
        return True
    else:
        return False


screen = pygame.display.set_mode((1300, 600))
pygame.init()
while running:
    mouse = pygame.mouse.get_pos()
    result = False
    mouseDown = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
    if buttonCheck(buttonEnemy1, mouse, mouseDown):
        result = fight(enemy1, player)
        screen.fill((0, 0, 0))
    elif buttonCheck(buttonEnemy2, mouse, mouseDown):
        result = fight(enemy2, player)
        screen.fill((0, 0, 0))
    if result:
        screen.fill((0, 255, 0))

    time.sleep(0.01)
pygame.quit()