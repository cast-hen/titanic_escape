import pygame
import time

screen = pygame.display.set_mode((1366, 690), pygame.RESIZABLE)

class button:
    def __init__(self, x, y, width, height, colourNormal, colourHover, text, textColour, textSize, borderColour):
        """
        Maak een nieuwe knop aan
        x: de x-positie van de linkerzijde van de knop
        y: de y-positie van de top van de knop
        width: hoe wijd de knop is
        height: hoe hoog de knop is
        colourNormal: de kleur van de knop
        colourHover: de kleur van de knop als de muis eroverheen gaat
        text: een string tekst die op de knop moet staan
        textColour: de kleur van de tekst
        textSize: de grootte van de tekst
        borderColour: de kleur van de rand om de knop heen
        return: De knop in het juiste format voor de functies
        """
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

    def check(self, mouseDown, screen):
        """
        Print een knop, geeft aan als de knop wordt ingedrukt
        :param mouseDown: Is de muisknop ingedrukt True of False
        :param screen: Het scherm waar de button op moet komen
        :return: True of False
        """
        mouse = pygame.mouse.get_pos()

        font = pygame.font.Font("freesansbold.ttf", self.textSize)
        text = font.render(self.text, True, self.textColour)
        pygame.draw.rect(screen, self.borderColour, [self.x, self.y, self.width, self.height])
        if self.width < self.height:
            borderSize = self.width / 20
        else:
            borderSize = self.height / 20
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            pygame.draw.rect(screen, self.colourHover, [round(self.x + borderSize), round(self.y + borderSize),
                                                          round(self.width - (2 * borderSize)),
                                                          round(self.height - (2 * borderSize))])
        else:
            pygame.draw.rect(screen, self.colourNormal, [round(self.x + borderSize), round(self.y + borderSize),
                                                           round(self.width - (2 * borderSize)),
                                                           round(self.height - (2 * borderSize))])
        textRect = text.get_rect()
        textRect.center = (self.x + (self.width / 2), self.y + (self.height / 2))
        screen.blit(text, textRect)
        pygame.display.update()
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[
            1] <= self.y + self.height and mouseDown == True:
            return True
        else:
            return False
