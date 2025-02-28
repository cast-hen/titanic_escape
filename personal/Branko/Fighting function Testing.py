import pygame
import time

class enemy:
    def __init__(self, name, colour, hitpoints, moveset):
        self.name = name
        self.colour = colour
        self.hitpoints = hitpoints
        self.moveset = moveset

class button:
    def __init__(self, x, y, width, height, colourNormal, colourHover, text, textColour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colourNormal = colourNormal
        self.colourHover = colourHover
        self.text = text
        self.textColour = textColour
allMovesList = ["punch", "heal", "combo punch", "enrage", "poison", "life steal", "block"]
playerMoves = ["punch", "heal", "combo punch"]

running = True
mouseDown = False
health = 100
enemy1 = enemy("Bob", (0, 0, 255), 100, ["punch", "heal"])
enemy2 = enemy("ASHRddgteGEtek, destroyer of lightbulbs", (255, 0, 255), 500, ["punch", "combo punch", "enrage"])
buttonEnemy1 = button(100, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy1", (255, 255, 255))
buttonEnemy2 = button(800, 300, 400, 200, (0, 0, 255), (255, 0, 0), "Enemy2", (255, 255, 255))

def buttonCheck(button):
    font = pygame.font.Font("freesansbold.ttf", int(button.width / 5))
    text = font.render(button.text, True, button.textColour)
    if button.x <= mouse[0] <= button.x + button.width and button.y <= mouse[1] <= button.y + \
            button.height:
        pygame.draw.rect(screen, button.colourHover, [button.x, button.y, button.width, button.height])
    else:
        pygame.draw.rect(screen, button.colourNormal, [button.x, button.y, button.width, button.height])
    textRect = text.get_rect()
    textRect.center = (button.x + (button.width / 2), button.y + (button.height / 2))
    screen.blit(text, textRect)
    pygame.display.update()
    if button.x <= mouse[0] <= button.x + button.width and button.y <= mouse[1] <= button.y + button.height and mouseDown == True:
        return True
    else:
        return False

def fight(enemy):
    def draw_scene():
        screen.fill((40, 255, 255))
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, enemy.colour, pygame.Rect(1000, 250, 100, 200))
        healthTextPlayer = healthFont.render(str(playerHealth) + "/" + str(health), True, (255, 255, 255))
        healthTextPlayerRect = healthTextPlayer.get_rect()
        healthTextPlayerRect.center = (250, 200)
        screen.blit(healthTextPlayer, healthTextPlayerRect)
        healthTextEnemy = healthFont.render(str(enemyHealth) + "/" + str(enemy.hitpoints), True, (255, 255, 255))
        healthTextEnemyRect = healthTextEnemy.get_rect()
        healthTextEnemyRect.center = (1050, 200)
        screen.blit(healthTextEnemy, healthTextEnemyRect)
        pygame.display.update()

    playerHealth = health
    enemyHealth = enemy.hitpoints
    fighting = True
    state = "turnPlayer"
    draw_scene()
    fightText = pygame.image.load("../../game assets/images/fightText.png")
    fightText = pygame.transform.scale(fightText, (400, 200))
    screen.blit(fightText, (int(screen.get_width() / 2) - 200, int(screen.get_height() / 2) - 100))
    pygame.display.update()
    time.sleep(3)
    while fighting:
        mouse = pygame.mouse.get_pos()
        draw_scene()
        if state == "turnPlayer":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fighting = False
                    return "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
        elif state == "turnEnemy":
            pass
        time.sleep(0.01)

    pygame.display.update()


screen = pygame.display.set_mode((1300, 600))
pygame.init()
while running:
    mouse = pygame.mouse.get_pos()
    result = "none"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
    if buttonCheck(buttonEnemy1):
        result = fight(enemy1)
    elif buttonCheck(buttonEnemy2):
        result = fight(enemy2)
    if result == "quit":
        running = False
    elif result == "win":
        pass
    elif result == "loss":
        pass

    time.sleep(0.01)
pygame.quit()