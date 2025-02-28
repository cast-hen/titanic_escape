import pygame
import time
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
running = True
screen = pygame.display.set_mode((1300, 600))
mouseDown = False
pause = False
scene = "start"
def buttonCheck(button, mouse, mouseDown):
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
    if button.x <= mouse[0] <= button.x + button.width and button.y <= mouse[1] <= button.y + button.height and mouseDown:
        return True
    else:
        return False

def pauseScreen():
    paused = True
    width = screen.get_width()
    height = screen.get_height()
    continueButton = button(int(width / 3), int(height / 7), int(width / 3), int(height / 5), (100, 100, 100),(255, 255, 255), "continue", (0, 0, 0))
    restartButton = button(int(width / 3), int(height / 7 * 3), int(width / 3), int(height / 5), (100, 100, 100),(255, 255, 255), "restart", (0, 0, 0))
    quitButton = button(int(width / 3), int(height / 7) * 5, int(width / 3), int(height / 5), (100, 100, 100), (255,255,255), "quit", (0, 0, 0))
    mouseDown = False
    while paused:
        mouse = pygame.mouse.get_pos()
        if buttonCheck(continueButton, mouse, mouseDown):
            return "continue"
        if buttonCheck(restartButton, mouse, mouseDown):
            return "restart"
        if buttonCheck(quitButton, mouse, mouseDown):
            return "quit"
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "continue"
        time.sleep(0.01)
pygame.init()
while running:
    mouse = pygame.mouse.get_pos()
    mouseDown = False
    screen.fill((255,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause = True
    if pause:
        pauseOutput = pauseScreen()
        if pauseOutput == "quit":
            running = False
        elif pauseOutput == "restart":
            pass
        pause = False
    pygame.display.update()
    time.sleep(0.01)
pygame.quit()