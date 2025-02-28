import pygame
import time
import random

running = True
achtergrond = (0, 0, 0)
board = []
cycles = 0
enimyPos = [0, 0]
colourPlayer = (0, 255, 0)

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

def tekenBord():
    for i in range(0, boardSize):
        for j in range(0, boardSize):
            pygame.draw.rect(screen, board[i][j], pygame.Rect(((100 + 600 * i) / boardSize) + 325, ((100 + 600 * j) / boardSize) + 20, 500 / boardSize, 500 / boardSize))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(((225 + 600 * coinPos[0]) / boardSize) + 325, ((225 + 600 * coinPos[1]) / boardSize) + 20, 250 / boardSize, 250 / boardSize))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(((225 + 600 * enimyPos[0]) / boardSize) + 325, ((225 + 600 * enimyPos[1]) / boardSize) + 20, 250 / boardSize, 250 / boardSize))
    pygame.draw.rect(screen, colourPlayer, pygame.Rect(((225 + 600 * playerPos[0]) / boardSize) + 325, ((225 + 600 * playerPos[1]) / boardSize) + 20, 250 / boardSize, 250 / boardSize))
    pygame.display.flip()

def enimyCalc():
    if enimyPos == playerPos:
        return [0, 0]
    return [0, 0]

def showText(text):
    screen.fill(achtergrond)
    pygame.display.update()
    font = pygame.font.Font("freesansbold.ttf", 100)
    displayedText = font.render(text, True, (255, 255, 255), (0, 0, 0))
    textRect = displayedText.get_rect()
    textRect.center = (1300 // 2, 650 // 2)
    screen.blit(displayedText, textRect)
    pygame.display.update()
    time.sleep(2)
    screen.fill(achtergrond)


screen = pygame.display.set_mode((1300, 650), pygame.SHOWN)
pygame.display.set_caption("Danger Zone")
pygame.init()
screen.fill(achtergrond)
state = "start"
while running:
    mouse = pygame.mouse.get_pos()
    if state == "start":
        startScreen()
        coins = 0
        lives = 5
        while state == "start":
            mouse = pygame.mouse.get_pos()
            buttonLoad([300, 450], [200, 80], (0, 0, 255), (200, 200, 255), "Easy")
            buttonLoad([550, 450], [200, 80], (0, 0, 255), (200, 200, 255), "Normal")
            buttonLoad([800, 450], [200, 80], (0, 0, 255), (200, 200, 255), "Hard")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 450 <= mouse[1] <= 530:
                        boardSize = 22
                        maxCycles = 8
                        state = "playing"
                    if 550 <= mouse[0] <= 750 and 450 <= mouse[1] <= 530:
                        boardSize = 17
                        maxCycles = 6
                        state = "playing"
                    if 800 <= mouse[0] <= 1000 and 450 <= mouse[1] <= 530:
                        boardSize = 12
                        maxCycles = 4
                        state = "playing"
            if state == "playing":
                screen.fill(achtergrond)
                pygame.display.update()
                for i in range(0, boardSize):
                    board.append([])
                    for j in range(0, boardSize):
                        board[i].append((0, 0, 255))
                for i in range(0, boardSize):
                    board[0][i] = board[i][0] = board[boardSize - 1][i] = board[i][boardSize - 1] = (0, 0, 0)
                playerPos = [int(boardSize / 2), int(boardSize / 2)]
                enimyPos = [1, 1]
                coinPos = [random.randint(1, boardSize - 2), random.randint(1, boardSize - 2)]
                while coinPos == enimyPos or coinPos == playerPos or board[coinPos[0]][coinPos[1]] == (0, 0, 0):
                    coinPos = [random.randint(1, boardSize - 2), random.randint(1, boardSize - 2)]
    elif state == "playing":
        tekenBord()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playerPos[1] -= 1
                if event.key == pygame.K_a:
                    playerPos[0] -= 1
                if event.key == pygame.K_s:
                    playerPos[1] += 1
                if event.key == pygame.K_d:
                    playerPos[0] += 1
        if board[playerPos[0]][playerPos[1]] == (0, 0, 0):
            state = "deathPause"
        elif playerPos == coinPos:
            coins += 1
            coinPos = [random.randint(1, boardSize - 2), random.randint(1, boardSize - 2)]
            while coinPos == enimyPos or coinPos == playerPos or board[coinPos[0]][coinPos[1]] == (0, 0, 0):
                coinPos = [random.randint(1, boardSize - 2), random.randint(1, boardSize - 2)]
        cycles += 1
        if cycles == maxCycles:
            cycles = 0
            enimyMovementList = enimyCalc()
            enimyPos[enimyMovementList[0]] += enimyMovementList[1]
        if enimyPos == playerPos:
            state = "deathPause"
    elif state == "deathPause":
        colourPlayer = (255, 0, 0)
        lives -= 1
        tekenBord()
        time.sleep(2)
        if lives == 0:
            running = False
        else:
            showText("-1 life")
            for i in range(1, boardSize - 1):
                for j in range(1, boardSize - 1):
                    if board[i][j] != (0, 0, 255):
                        board[i][j] = (0, 0, 255)
            state = "playing"
            cycles = 0
            playerPos = [int(boardSize / 2), int(boardSize / 2)]
            enimyPos = [1, 1]
            coinPos = [random.randint(1, boardSize - 2), random.randint(1, boardSize - 2)]
            while coinPos == enimyPos or coinPos == playerPos or board[coinPos[0]][coinPos[1]] == (0, 0, 0):
                coinPos = [random.randint(1, boardSize - 2), random.randint(1, boardSize - 2)]
            colourPlayer = (0, 255, 0)
            screen.fill(achtergrond)
            tekenBord()
            pygame.event.get()
    time.sleep(0.1)

pygame.quit()