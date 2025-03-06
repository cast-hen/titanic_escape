from pauze import *
from common import *
from button_code import *
import pygame

screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)

class Aanval:
    def __init__(self, afbeelding, naam, beschrijving, schade, genezing):
        self.Afbeelding = afbeelding
        self.naam = naam
        self.beschrijving = beschrijving

        self.schade = schade
        self.genezing = genezing

    def display_aanval(self, x, y):
        screen.blit(pygame.transform.scale(pygame.image.load("resources/textures/Kaart.png"), (400, 400)), (x - 100, y - 75))

        font = pygame.font.Font("freesansbold.ttf", 10)

        if not self.Afbeelding == "":
            screen.blit(self.Afbeelding, (x, y))
        text = font.render(self.beschrijving, True, (255, 255, 255))
        screen.blit(text, (x + 80 - int(len(self.beschrijving) * 1.3), y + 200))

        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render(self.naam, True, (255, 255, 255))
        screen.blit(text, (x + 80 - len(self.naam) * 5, y - 40))

def keuze(TeKiezenAanvallen):
    screen.fill((100, 100, 100))
    TeKiezenAanvallen[0].display_aanval(30, 110)
    TeKiezenAanvallen[1].display_aanval(330, 110)
    TeKiezenAanvallen[2].display_aanval(630, 110)

    buttonKeuze1 = button(50, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Kiezen", 'white', 50, 'white')
    buttonKeuze2 = button(350, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Kiezen", 'white', 50, 'white')
    buttonKeuze3 = button(650, 500, 200, 80, (0, 0, 255), (255, 0, 0), "Kiezen", 'white', 50, 'white')

    mouseDown = False
    mouse = pygame.mouse.get_pos()
    button.check(buttonKeuze1, mouse, mouseDown, screen)
    button.check(buttonKeuze2, mouse, mouseDown, screen)
    button.check(buttonKeuze3, mouse, mouseDown, screen)

    while True:
        for event in pygame.event.get():
            if button.check(buttonKeuze1, pygame.mouse.get_pos(), mouseDown, screen):
                return TeKiezenAanvallen[0]
            if button.check(buttonKeuze2, pygame.mouse.get_pos(), mouseDown, screen):
                return TeKiezenAanvallen[1]
            if button.check(buttonKeuze3, pygame.mouse.get_pos(), mouseDown, screen):
                return TeKiezenAanvallen[2]

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            else:
                mouseDown = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if Pause() == "Menu":
                        return "Menu"
                    else:
                        screen.fill((100, 100, 100))
                        TeKiezenAanvallen[0].display_aanval(30, 110)
                        TeKiezenAanvallen[1].display_aanval(330, 110)
                        TeKiezenAanvallen[2].display_aanval(630, 110)

            if event.type == pygame.QUIT:
                return False