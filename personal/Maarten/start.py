import pygame

screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.font.init()

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


def textOutline(text, textSize, textColour, outlineColour, outlineThickness, center):
    textPrint(text, textSize, outlineColour, (center[0] - outlineThickness, center[1] - outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] - outlineThickness, center[1] + outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] + outlineThickness, center[1] - outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] + outlineThickness, center[1] + outlineThickness))
    textPrint(text, textSize, textColour, center)

pygame.draw.line(screen, 'white', (12.31, 32.9), (238, 33.4))

textOutline("yippeee", 120, 'black', 'white', 2, (WIDTH/2, HEIGHT/2))
pygame.display.flip()

while True:
    pass