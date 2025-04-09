import pygame
import time
# from common import textPrint
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
        textPrint(self.text, self.textSize, self.textColour, (self.x + (self.width / 2), self.y + (self.height / 2)))
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[
            1] <= self.y + self.height and mouseDown == True:
            return True
        else:
            return False


def textPrint(word, textSize, textColour, center, delete=None, outline=None):
    """
    Prints the text on the screen. Can also delete the text by drawing the Rect of the text given.
    :param word: What word will print
    :param textSize: How big is the text
    :param textColour: What color is the text. If delete is not None, the colour of the drawn Rect.
    :param center: location of center text in tuple
    :param delete: True if job is to delete the text, fill to black
    :param outline: tuple (outlineColour, outlineThickness). If not None there will be an outline around the text.
    :return: None
    """
    font = pygame.font.Font(mainFont, textSize)
    if outline is not None:
        text = font.render(word, True, outline[0])
        textRect = text.get_rect()
        textRect.center = (center[0] - outline[1], center[1] - outline[1])
        screen.blit(text, textRect)
        textRect.center = (center[0] - outline[1], center[1] + outline[1])
        screen.blit(text, textRect)
        textRect.center = (center[0] + outline[1], center[1] - outline[1])
        screen.blit(text, textRect)
        textRect.center = (center[0] + outline[1], center[1] + outline[1])
        screen.blit(text, textRect)
    text = font.render(word, True, textColour)
    textRect = text.get_rect()
    textRect.center = center
    if delete is not None:
        pygame.draw.rect(screen, textColour, textRect)
    else:
        screen.blit(text, textRect)


def waitForInput(buttonList, keyEscape=None, typeInfo=None):
    """
    Waits for input of the player in the form of pressing a button.
    :param buttonList: The buttons that are checked
    :param keyEscape: True if using the escape button is possible
    :param typeInfo: If possible to type, tuple with (buttonToType, startText, textCenter, textSize)
    :return the index of the pressed button
    """
    typing = False
    if typeInfo is not None:
        buttonToType, text, textCenter, textSize, outline = typeInfo
    while True:
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and keyEscape is not None:
                    if typeInfo is None:
                        return -1
                    else:
                        return -1, text

                if event.key == pygame.K_BACKSPACE and typing:
                    textPrint(text, textSize, 'black', (textCenter[0], textCenter[1] - 3), True)
                    text = text[:-1]
                    textPrint(text, textSize, 'white', textCenter, outline=outline)
                elif event.key == pygame.K_RETURN and typing:
                    typing = False
            elif event.type == pygame.TEXTINPUT and typing:
                textPrint(text + "    ", textSize, 'black', (textCenter[0], textCenter[1] - 3), True)
                if len(text) <= 10:
                    text += event.text
                else:
                    textPrint("Too long!", textSize, 'red', textCenter)
                    pygame.display.flip()
                    time.sleep(1)
                    textPrint("Too long!", textSize, 'black', (textCenter[0], textCenter[1] - 3), True)
                textPrint(text, textSize, 'white', textCenter, outline=outline)
        for i in range(len(buttonList)):
            if button.check(buttonList[i], mouseDown, screen):
                if typeInfo is None:
                    return i
                else:
                    return i, text
            pygame.display.update()

        if typeInfo is not None:
            if button.check(buttonToType, mouseDown, screen):
                typing = not typing
        pygame.display.flip()
