import pygame
import time

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

    def check(self, mouse, mouseDown):
        font = pygame.font.Font("freesansbold.ttf", self.textSize)
        text = font.render(self.text, True, self.textColour)
        pygame.draw.rect(screen, self.borderColour, [self.x, self.y, self.width, self.height])
        if self.width < self.height:
            borderSize = self.width / 20
        else:
            borderSize = self.height / 20
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            pygame.draw.rect(screen, self.colourHover, [int(self.x + borderSize), int(self.y + borderSize),
                                                          int(self.width - (2 * borderSize)),
                                                          int(self.height - (2 * borderSize))])
        else:
            pygame.draw.rect(screen, self.colourNormal, [int(self.x + borderSize), int(self.y + borderSize),
                                                           int(self.width - (2 * borderSize)),
                                                           int(self.height - (2 * borderSize))])
        textRect = text.get_rect()
        textRect.center = (self.x + (self.width / 2), self.y + (self.height / 2))
        screen.blit(text, textRect)
        pygame.display.update()
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[
            1] <= self.y + self.height and mouseDown == True:
            return True
        else:
            return False

buttonTest = button(0, 0, 50, 50, (255, 0, 0), (0, 0, 255), "ello", (0, 0, 0), 10, (0, 0, 0))
running = True
screen = pygame.display.set_mode((1300, 600))

pygame.init()
while running:
    mouse = pygame.mouse.get_pos()
    mouseDown = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
    if button.check(buttonTest, mouse, mouseDown):
        running = False
pygame.quit()