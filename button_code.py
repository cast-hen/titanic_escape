import pygame
import time
# from common import textPrint
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()

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
        pygame.draw.rect(screen, self.borderColour, [self.x, self.y, self.width, self.height])
        if self.width < self.height:
            borderSize = self.width / 20
        else:
            borderSize = self.height / 20
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            pygame.draw.rect(screen, self.colourHover, [round(self.x + borderSize), round(self.y + borderSize),
                                                          round(self.width - (2 * borderSize)),
                                                          round(self.height - (2 * borderSize))])
        else:
            pygame.draw.rect(screen, self.colourNormal, [round(self.x + borderSize), round(self.y + borderSize),
                                                           round(self.width - (2 * borderSize)),
                                                           round(self.height - (2 * borderSize))])
        textPrint(self.text, self.textSize, self.textColour, (self.x + (self.width / 2), self.y + (self.height / 2)))
        pygame.display.update()
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[
            1] <= self.y + self.height and mouseDown == True:
            return True
        else:
            return False


def textPrint(text, textSize, textColour, center):
    """
    Prints the text on the screen. center is tuple.
    :param text: What text will print
    :param textSize: How big is the text
    :param textColour: What color is the text
    :param center: location of center text
    :return: None
    """
    font = pygame.font.Font("freesansbold.ttf", textSize)
    text = font.render(text, True, textColour)
    textRect = text.get_rect()
    textRect.center = center
    screen.blit(text, textRect)
