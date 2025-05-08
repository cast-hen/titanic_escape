import pygame
import time
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
mainFont = 'resources/MinecraftTen-VGORe.ttf'

class button:
    def __init__(self, x, y, width, height, colourNormal, colourHover, text, textColour, textSize, borderColour):
        """
        Maakt een nieuwe knop aan
        :param x: de x-positie van de linkerzijde van de knop
        :param y: de y-positie van de top van de knop
        :param width: hoe wijd de knop is
        :param height: hoe hoog de knop is
        :param colourNormal: de kleur van de knop
        :param colourHover: de kleur van de knop als de muis eroverheen gaat
        :param text: een string tekst die op de knop moet staan
        :param textColour: de kleur van de tekst
        :param textSize: de grootte van de tekst
        :param borderColour: de kleur van de rand om de knop heen
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
        textPrint(screen, self.text, self.textSize, self.textColour, (self.x + (self.width / 2), self.y + (self.height / 2)))
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[
            1] <= self.y + self.height and mouseDown == True:
            return True
        else:
            return False


def textPrint(surface, word, textSize, textColour, center, return_rect=None, outline=None):
    """
    Prints the text on the screen. Can also delete the text by drawing the Rect of the text given.
    :param surface: The surface on which the text will print
    :param word: What word will print
    :param textSize: How big is the text
    :param textColour: What color is the text. If delete is not None, the colour of the drawn Rect.
    :param center: location of center text in tuple
    :param return_rect: If True the rectangle of the text will be returned.
    :param outline: tuple (outlineColour, outlineThickness). If not None there will be an outline around the text.
    :return: None
    """
    font = pygame.font.Font(mainFont, textSize)
    if outline is not None:
        text = font.render(word, True, outline[0])
        textRect = text.get_rect()
        textRect.center = (center[0] - outline[1], center[1] - outline[1])
        surface.blit(text, textRect)
        textRect.center = (center[0] - outline[1], center[1] + outline[1])
        surface.blit(text, textRect)
        textRect.center = (center[0] + outline[1], center[1] - outline[1])
        surface.blit(text, textRect)
        textRect.center = (center[0] + outline[1], center[1] + outline[1])
        surface.blit(text, textRect)
    text = font.render(word, True, textColour)
    textRect = text.get_rect()
    textRect.center = center
    if return_rect:
        return textRect
    else:
        surface.blit(text, textRect)
        return None


def waitForInput(buttonList, keyEscape=None):
    """
    Waits for input of the player in the form of pressing a button.
    :param buttonList: The buttons that are checked
    :param keyEscape: True if using the escape button is possible
    :return the index of the pressed button
    """
    while True:
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and keyEscape is not None:
                    return -1

        for i in range(len(buttonList)):
            if button.check(buttonList[i], mouseDown, screen):
                return i
        pygame.display.flip()
