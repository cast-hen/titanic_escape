from parkour_functies import *
import pygame
import time
import random
from button_code import button

# pygame.image.load("Bom.png")

screen = pygame.display.set_mode((1366, 697), pygame.RESIZABLE)
running = True
pygame.init()
Aanvallen = ["Slaan", "Genezen"]

Speler = [10, Aanvallen, [0, 0]]
# Speler = [Levens, Aanvallen, positie]



class Aanval:
    def __init__(self, afbeelding, naam, beschrijving, schade, genezing):
        self.Afbeelding = afbeelding
        self.naam = naam
        self.beschrijving = beschrijving

        self.schade = schade
        self.genezing = genezing

    def display_aanval(self, x, y):
        screen.blit(pygame.transform.scale(pygame.image.load("Kaart.png"), (400, 400)), (x - 100, y - 75))

        font = pygame.font.Font("freesansbold.ttf", 10)

        if not self.Afbeelding == "":
            screen.blit(self.Afbeelding, (x, y))
        text = font.render(self.beschrijving, True, (255, 255, 255))
        screen.blit(text, (x + 80 - int(len(self.beschrijving) * 1.3), y + 200))

        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render(self.naam, True, (255, 255, 255))
        screen.blit(text, (x + 80 - len(self.naam) * 5, y - 40))


A_Bom = Aanval(pygame.transform.scale(pygame.image.load("Bom.png"), (200, 200)), "Bom",
               "Valt elke vijand aan voor 5 schade", 5, 5)
A_Zwaardslag = Aanval("", "Zwaard", "Valt 1 vijand aan voor 10 schade", 10, 0)
A_Genezen = Aanval("", "Genezen", "Genees 10 levens", 0, 10)
A_Blokkeren = Aanval("", "Blokkeren", "Blokkeer 80% van de schade", 0, 0)


class Vijand:
    def __init__(self, afbeelding, naam, levens, aanvallen):
        self.Afbeelding = afbeelding
        self.naam = naam
        self.hitpoints = levens
        self.aanvallen = aanvallen

    def aanval_kiezen(self):
        return self.aanvallen[random.randint(0, len(self.aanvallen) - 1)]



def WillekeurigeAanvalKiezen(AanvallenLijst):
    OptiesAanvallen = []
    randomAanval = AanvallenLijst[random.randint(0, len(AanvallenLijst) - 1)]
    OptiesAanvallen.append(randomAanval)
    for i in range(0, 2):

        while randomAanval in OptiesAanvallen:
            randomAanval = AanvallenLijst[random.randint(0, len(AanvallenLijst) - 1)]

        OptiesAanvallen.append(randomAanval)

    return OptiesAanvallen


# Hieronder staan de hoofd functies

# Menu scherm
def menu():
    font = pygame.font.Font("freesansbold.ttf", 100)
    text = font.render("Titanic ecsape", True, (255, 255, 255))
    mouse = pygame.mouse.get_pos()

    mouseDown = False
    buttonKeuze1 = button(550, 200, 160, 80, (0, 0, 255), (255, 0, 0), "Begin",(0, 0, 0), 30, (0, 0, 0))
    buttonKeuze2 = button(550, 300, 160, 80, (0, 0, 255), (255, 0, 0), "Quit", (0, 0, 0), 30, (0, 0, 0))
    buttonKeuze3 = button(550, 400, 160, 80, (0, 0, 255), (255, 0, 0), "Crash", (0, 0, 0), 30, (0, 0, 0))

    buttonKeuze1.check(mouse, mouseDown, screen)
    buttonKeuze2.check(mouse, mouseDown, screen)
    buttonKeuze3.check(mouse, mouseDown, screen)

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if     buttonKeuze1.check(mouse, mouseDown, screen):
                return "Begin"
            if     buttonKeuze2.check(mouse, mouseDown, screen):
                return "Quit"
            if     buttonKeuze3.check(mouse, mouseDown, screen):
                return "Crash"

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            else:
                mouseDown = False

            if event.type == pygame.QUIT:
                return False
        screen.blit(text, (300, 50))


# Return "Begin", of "Quit" (of "Tutorial")


# Parkour deel
def parkour():
    # global variables
    WIDTH = 1366
    HEIGHT = 690
    font = pygame.font.Font("freesansbold.ttf", 100)
    text = font.render("you ded", True, 'black')
    textRect = text.get_rect()
    textRect.center = (WIDTH / 2, HEIGHT / 2)
    clock = pygame.time.Clock()
    fps = 60
    gravity = 0.6
    jump_height = -25
    speed = 10
    running = True
    scene = "main_menu"
    mouseDown = False
    CameraPosx = 0

    # texturestest
    # texture = pygame.image.load(r"C:\Users\12880\OneDrive - Atheneum College Hageveld\2024-2025\infomatica\game files\game assets\images\texturetest.png")
    # player_texture = pygame.image.load(r"C:\Users\12880\OneDrive - Atheneum College Hageveld\2024-2025\infomatica\game files\game assets\images\BozeJantje.png")



    # objects
    player = Objects(300, 200, 50, 50, 'green', 2, 0, 0)
    cube1 = Objects(580, 400, 60, 60, 'black', 1, 0, 0)
    cube2 = Objects(690, 546, 600, 40, 'black', 1, 0, 0)
    cube3 = Objects(0, 300, 400, 60, 'black', 1, 0, 0)
    cube4 = Objects(600, 100, 80, 80, 'orange', 1, 0, 0)

    # voeg hier nieuwe platformen to zodat ze collision krijgen.
    platforms = [cube1, cube2, cube3, cube4]

    # texturecropping
    # texture1 = texture.subsurface(pygame.Rect(0, 0, cube4.width, cube4.height))
    # texture2 = texture.subsurface(pygame.Rect(0, 0, cube3.width, cube3.height))
    # texture3 = texture.subsurface(pygame.Rect(0, 0, cube1.width, cube1.height))
    # texture4 = texture.subsurface(pygame.Rect(0, 0, cube2.width, cube2.height))

    # random ahhh movement fix, couldn't bother om een betere oplossing te vinden.
    keys = {"left": False, "right": False}
    EnemyCollider = False

    L_border = 0
    R_border = 500

    # game loop
    while running:
        print(screen.get_size())
        mouse = pygame.mouse.get_pos()

        if scene == "main_menu":
            scene = "scene1"


        elif scene == "scene1":
            clock.tick(fps)
            screen.fill((135, 206, 250))
            draw_floor()
            EnemyCollider = player.update_pos(platforms, CameraPosx)

            player.draw(screen, CameraPosx)
            cube1.draw(screen, CameraPosx)
            cube2.draw(screen, CameraPosx)
            cube3.draw(screen, CameraPosx)
            cube4.draw(screen, CameraPosx)
            # screen.blit(texture1, cube4.Rect.topleft)
            # screen.blit(texture2, cube3.Rect.topleft)
            # screen.blit(texture3, cube1.Rect.topleft)
            # screen.blit(texture4, cube2.Rect.topleft)
            player.xspeed = speed * (keys["right"] - keys["left"])

        if player.ypos >= 630:
            screen.fill((255, 0, 0))
            screen.blit(text, textRect)
            player.ypos = 200
            player.xpos = 200
            pygame.display.flip()
            time.sleep(2)

        if EnemyCollider:
            return "Vijand"
        if L_border < player.xpos < R_border:
            CameraPosx = player.xpos - 400

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            # movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keys["right"] = True
                elif event.key == pygame.K_a:
                    keys["left"] = True
                elif event.key == pygame.K_w and player.on_ground:
                    player.yspeed = jump_height

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keys["right"] = False
                elif event.key == pygame.K_a:
                    keys["left"] = False

        pygame.display.flip()

    pygame.quit()


# returns de tegengekomen vijand


# Gevecht deel
def gevecht(health, enemy):
    def draw_scene():
        screen.fill((100, 200, 0))
        healthFont = pygame.font.Font("freesansbold.ttf", 40)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(200, 250, 100, 200))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(700, 250, 100, 200))
        healthTextPlayer = healthFont.render(str(playerHealth) + "/" + str(health), True, (255, 255, 255))
        healthTextPlayerRect = healthTextPlayer.get_rect()
        healthTextPlayerRect.center = (250, 200)
        screen.blit(healthTextPlayer, healthTextPlayerRect)
        healthTextEnemy = healthFont.render(str(enemyHealth) + "/" + str(enemy.hitpoints), True, (255, 255, 255))
        healthTextEnemyRect = healthTextEnemy.get_rect()
        healthTextEnemyRect.center = (750, 200)
        screen.blit(healthTextEnemy, healthTextEnemyRect)
        pygame.display.update()

    buttonKeuze1 = button(70, 500, 160, 80, (0, 0, 255), (255, 0, 0), "Aanval", (0, 0, 0), 30, (0, 0, 0))

    playerHealth = health
    enemyHealth = enemy.hitpoints
    fighting = True
    state = "turnPlayer"
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
                    if     buttonKeuze1.check(mouse, mouseDown, screen):
                        enemy.hitpoints -= 10
                    if enemy.hitpoints <= 0:
                        return True
        elif state == "turnEnemy":
            pass
        time.sleep(0.01)

    pygame.display.update()


# returns uitslag gevecht: (Gewonnen = True)


# Game Over scherm
def game_over():
    return None


# Nieuwe aanval kiezen
def keuze(TeKiezenAanvallen):
    screen.fill((100, 100, 100))
    mouse = pygame.mouse.get_pos()

    TeKiezenAanvallen[0].display_aanval(280, 110)
    TeKiezenAanvallen[1].display_aanval(580, 110)
    TeKiezenAanvallen[2].display_aanval(880, 110)

    mouseDown = False
    buttonKeuze1 = button(320, 500, 160, 80, (0, 0, 255), (255, 0, 0), "Kiezen", (0, 0, 0), 30, (0, 0, 0))
    buttonKeuze2 = button(620, 500, 160, 80, (0, 0, 255), (255, 0, 0), "Kiezen", (0, 0, 0), 30, (0, 0, 0))
    buttonKeuze3 = button(920, 500, 160, 80, (0, 0, 255), (255, 0, 0), "Kiezen", (0, 0, 0), 30, (0, 0, 0))

    buttonKeuze1.check(mouse, mouseDown, screen)
    buttonKeuze2.check(mouse, mouseDown, screen)
    buttonKeuze3.check(mouse, mouseDown, screen)

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if buttonKeuze1.check(mouse, mouseDown, screen):
                return TeKiezenAanvallen[0]
            if buttonKeuze2.check(mouse, mouseDown, screen):
                return TeKiezenAanvallen[1]
            if buttonKeuze3.check(mouse, mouseDown, screen):
                return TeKiezenAanvallen[2]

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            else:
                mouseDown = False

            if event.type == pygame.QUIT:
                return False


# Returns gekozen aanval

# Het eindscherm
def eind():
    return None


state = "Menu"

while running:
    if state == "Menu":
        state = menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hoofd code:
    if state == "Begin":
        Encounter = parkour()
        gewonnen = gevecht(100, Vijand("", "", 100, 10))

        if gewonnen:
            gekozenAanval = keuze(WillekeurigeAanvalKiezen([A_Bom, A_Zwaardslag, A_Genezen, A_Blokkeren]))
            if not gekozenAanval == False:
                Aanvallen.append(gekozenAanval)
            else:
                running = False
        else:
            game_over()
    if state == "Quit":
        running = False

    pygame.display.update()

pygame.quit()
