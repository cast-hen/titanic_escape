import pygame
import time
import random


scherm = pygame.display.set_mode((680, 680))
pygame.init()
pygame.font.init()
running = True
Achtergrond = (100, 100, 100)

(xSpeler, ySpeler) = (0, 0)
(xVijand, yVijand) = (115, 115)

Speler = pygame.Rect(xSpeler, ySpeler, 70, 70)
Munt = pygame.Rect(xSpeler, ySpeler, 0, 0)
Vijand= pygame.Rect(xVijand, yVijand, 70, 70)
locatieSpeler = [3, 3]
locatieVijand = [0, 0]

HeeftBewogen = False
StartScherm = True

x = 0
y = 0

Zoom = 2
SpeedVijand = 40

Rijen = 10
Kolommen = 10


BlokkenKleur = (100, 200, 200)


BlokkenRijen = []

score = 0

score_font = pygame.font.SysFont('Comic Sans MS', 30)
UI_font = pygame.font.SysFont('Comic Sans MS', 48)



for i in range (0, Rijen):
    BlokkenRijen.append([])
    HuidigeRij = BlokkenRijen[i]
    for j in range(0, Kolommen):
        HuidigeRij.append([(100 + 120 * j, 100 + 120 * i, 100, 100), random.randint(1,10)])



for rijen in BlokkenRijen:
        for i in range (0, len(rijen)):
            blok = rijen[i]
            rijen[i] = [tuple(bloki/Zoom for bloki in blok[0]), blok[1]]




def TekenBord():

    for rijen in BlokkenRijen:
        for blok in rijen:
            if blok[1] >= 3:
                BlokkenKleur = (200, 200, 200)
            elif blok[1] == 2:
                BlokkenKleur = (200, 100, 100)
            elif blok[1] == 1:
                BlokkenKleur = (200, 0, 0)
            else:
                BlokkenKleur = (100, 100, 100)
            pygame.draw.rect(scherm, BlokkenKleur, blok[0], 0)

def positie( x, y):
    rij = BlokkenRijen[y]

    return rij[x]


def Aangrenzend(x, y):
    rij =  [[x + 1, y], [x - 1 , y], [x, y + 1], [x, y - 1]]
    for positie1 in rij:
        if positie1[0] < 0 or positie1[1] < 0 or positie1[0] > Rijen - 1  or positie1[1] > Kolommen - 1:
            rij.remove(positie1)
        elif positie(positie1[0], positie1[1])[1] == 0 and not [positie1[0], positie1[1]] == [xSpeler, ySpeler]:
            rij.remove(positie1)

    return rij

def Afstand():
    xVerschil = xSpeler - xVijand
    if xVerschil < 0:
        xVerschil = -xVerschil
    yVerschil = ySpeler - yVijand
    if yVerschil < 0:
        yVerschil = -yVerschil
    return yVerschil + xVerschil


def AI():
    lijstOrigin = []
    run = True
    lijst = Aangrenzend(xVijand, yVijand)
    lengte = 0
    minLengte = 10000000
    minPad = 0
    for plek in lijst:
        if plek == [xSpeler, ySpeler]:
            return plek

        HuidigeLijst = [plek]
        while run:
            for plekl in HuidigeLijst:

                if plekl == [xSpeler, ySpeler]:
                    if lengte < minLengte or lengte == minLengte and random.randint(0,1) == 1:
                        minLengte = lengte
                        minPad = plek

                    run = False


                HuidigeLijstl = Aangrenzend(plekl[0], plekl[1])
                for plek1 in HuidigeLijstl:
                    if not plek1 in lijstOrigin:
                        lijstOrigin.append(plek1)

            HuidigeLijst = lijstOrigin
            lijstOrigin = []
            lengte += 1
            if lengte > Afstand() + 20:
                return [xVijand, yVijand]
        run = True
        lengte = 0


    return minPad







def MuntBeweegt():
    xMunt = random.randint(0, Rijen -1)
    yMunt = random.randint(0, Kolommen -1)
    MuntL = pygame.Rect(tuple(map(lambda i, j: i + j, positie(xMunt, yMunt)[0], (17 / Zoom, 17 / Zoom, -35 / Zoom, -35 / Zoom))))
    return MuntL

def EindScherm():
    while True:
        scherm.fill(Achtergrond)
        text_surface = UI_font.render("GAME OVER: Score:" + str(score), False, (0, 0, 0))
        scherm.blit(text_surface, (10, 150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                StartScherm = False
                return False



xMunt = random.randint(0, Rijen -1)
yMunt = random.randint(0, Kolommen -1)
Munt = pygame.Rect(tuple(map(lambda i, j: i + j, positie(xMunt, yMunt)[0], (17 / Zoom, 17 / Zoom, -35 / Zoom, -35 / Zoom))))

while running:
    while StartScherm:
        scherm.fill(Achtergrond)
        text_surface = UI_font.render('Druk een toets om te starten', False, (0, 0, 0))
        scherm.blit(text_surface, (10, 150))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                StartScherm = False
                break
            if event.type == pygame.KEYDOWN:
                StartScherm = False
                break


    if (xSpeler,ySpeler) == (xVijand,yVijand):
        running = EindScherm()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and locatieSpeler[0] < len(BlokkenRijen[0]) - 1:
                locatieSpeler[0] += 1
            if event.key == pygame.K_a and locatieSpeler[0] > 0:
                locatieSpeler[0] -= 1
            if event.key == pygame.K_w and locatieSpeler[1] > 0:
                locatieSpeler[1] -= 1
            if event.key == pygame.K_s and locatieSpeler[1] < len(BlokkenRijen) - 1:
                locatieSpeler[1] += 1
            HeeftBewogen = True
            score+= 1


    if HeeftBewogen:
        HeeftBewogen = False
        ((BlokkenRijen[locatieSpeler[1]])[locatieSpeler[0]])[1] -= 1


    if ((BlokkenRijen[locatieSpeler[1]])[locatieSpeler[0]])[1] == -1:
        running = EindScherm()
    time.sleep(0.01)
    x += 1
    y += 1
    if x == SpeedVijand:
        locatieVijand = AI()
        x = 0



    ActieveBlokkenrij = BlokkenRijen[locatieSpeler[1]]
    ActieveBlokkenrijVijand = BlokkenRijen[locatieVijand[1]]
    Speler = pygame.Rect(tuple(map(lambda i, j: i + j, (ActieveBlokkenrij[locatieSpeler[0]])[0], (17 / Zoom, 17 / Zoom, -35 / Zoom, -35 / Zoom))))
    (xSpeler, ySpeler) = (locatieSpeler[0], locatieSpeler[1])
    (xVijand, yVijand) = (locatieVijand[0], locatieVijand[1])

    Vijand = pygame.Rect(tuple(map(lambda i, j: i + j, (ActieveBlokkenrijVijand[locatieVijand[0]])[0], (17 / Zoom, 17 / Zoom, -35 / Zoom, -35 / Zoom))))


    if (xSpeler, ySpeler) == (xMunt, yMunt):

        xMunt = random.randint(0, Rijen -1)
        yMunt = random.randint(0, Kolommen -1)
        Munt = pygame.Rect(tuple(map(lambda i, j: i + j, positie(xMunt, yMunt)[0], (17 / Zoom, 17 / Zoom, -35 / Zoom, -35 / Zoom))))
        while positie(xMunt,yMunt)[1] == 0:
            xMunt = random.randint(0, Rijen -1)
            yMunt = random.randint(0, Kolommen -1)
            Munt = pygame.Rect(tuple(map(lambda i, j: i + j, positie(xMunt, yMunt)[0], (17 / Zoom, 17 / Zoom, -35 / Zoom, -35 / Zoom))))

            y = 0

        score += 10
        y = 0
    if y == 500:
        xMunt = random.randint(0, Rijen -1)
        yMunt = random.randint(0, Kolommen -1)
        Munt = pygame.Rect(tuple(map(lambda i, j: i + j, positie(xMunt, yMunt)[0], (17 / Zoom, 17 / Zoom, -35 / Zoom, -35 / Zoom))))

        while positie(xMunt,yMunt)[1] == 0:
            print(positie(xMunt,yMunt)[1])
            xMunt = random.randint(0, Rijen -1)
            yMunt = random.randint(0, Kolommen -1)
            Munt = pygame.Rect(tuple(map(lambda i, j: i + j, positie(xMunt, yMunt)[0], (17 / Zoom, 17 / Zoom, -35 / Zoom, -35 / Zoom))))
        y = 0

    scherm.fill(Achtergrond)
    TekenBord()
    pygame.draw.rect(scherm, (0, 255, 0),Speler, 0)
    pygame.draw.rect(scherm, (0, 0, 255),Vijand, 0)
    pygame.draw.rect(scherm, (255, 255, 0),Munt, 0)

    text_surface = score_font.render(str(score), False, (0, 0, 0))
    scherm.blit(text_surface, (0,0))
    pygame.display.update()





print(score)
pygame.quit()