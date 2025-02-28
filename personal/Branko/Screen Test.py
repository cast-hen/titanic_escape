import pygame
import time
running = True
achtergrond = (0, 0, 0)
screen = pygame.display.set_mode((1300, 650), pygame.SHOWN)
pygame.display.set_caption("Danger Zone")
pygame.init()
screen.fill(achtergrond)
state = "start"
def startScreen():
    screen.fill(achtergrond)
    pygame.display.update()
    textFont = pygame.font.Font("freesansbold.ttf", 170)
    text = textFont.render("DANGER ZONE", True, (255, 0, 0), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1300 // 2, 200)
    screen.blit(text, textRect)
    subTextFont = pygame.font.Font("freesansbold.ttf", 50)
    subText = subTextFont.render("Select the difficulty", True, (255, 255, 255), (0, 0, 0))
    subTextRect = subText.get_rect()
    subTextRect.center = (1300 // 2, 300)
    pygame.display.update()
    time.sleep(1)
    screen.blit(subText, subTextRect)
    pygame.display.update()

def buttonLoad(buttonPos, buttonSize, buttonColourBasic, buttonColourPressed, text):
    font = pygame.font.Font("freesansbold.ttf", 40)
    text = font.render(text, True, (255, 255, 255))
    if buttonPos[0] <= mouse[0] <= buttonPos[0] + buttonSize[0] and buttonPos[1] <= mouse[1] <= buttonPos[1] + buttonSize[1]:
        pygame.draw.rect(screen, buttonColourPressed, [buttonPos[0], buttonPos[1], buttonSize[0], buttonSize[1]])
    else:
        pygame.draw.rect(screen, buttonColourBasic, [buttonPos[0], buttonPos[1], buttonSize[0], buttonSize[1]])
    textRect = text.get_rect()
    textRect.center = (buttonPos[0] + (buttonSize[0] / 2), buttonPos[1] + (buttonSize[1] / 2))
    screen.blit(text, textRect)
    pygame.display.update()

startScreen()
while running:
    mouse = pygame.mouse.get_pos()
    if state == "start":
        buttonLoad([300, 450], [200, 80], (0, 0, 255), (200, 200, 255), "Easy")
        buttonLoad([550, 450], [200, 80], (0, 0, 255), (200, 200, 255), "Normal")
        buttonLoad([800, 450], [200, 80], (0, 0, 255), (200, 200, 255), "Hard")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= mouse[0] <= 500 and 450 <= mouse[1] <= 530:
                    boardSize = 22
                    maxCycles = 10
                    state = "playing"
                if 550 <= mouse[0] <= 750 and 450 <= mouse[1] <= 530:
                    boardSize = 17
                    maxCycles = 7
                    state = "playing"
                if 800 <= mouse[0] <= 1000 and 450 <= mouse[1] <= 530:
                    boardSize = 12
                    maxCycles = 5
                    state = "playing"
    if state == "playing":
        print("yay")
        time.sleep(1)
    time.sleep(0.1)
pygame.quit()
