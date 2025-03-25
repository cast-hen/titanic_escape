import pygame
import math
import time
import random
from pygame import K_TAB, K_RETURN, K_BACKSPACE

pygame.init()

screen = pygame.display.set_mode((1366, 668))
WIDTH, HEIGHT = pygame.display.get_window_size()

word = "Thanks for Playing!"
fontSize = 120
colourGradients = [(224, 78, 31), (255, 186, 48), (255, 208, 114), (255, 251, 129), (184, 190, 184), (207, 213, 206)]
endColour = (2, 2, 2)

state = "Setup" # Setup, Rising, Exploding, Pause, End
pointDensity = 6  # Higher values mean less particles thus faster
backgroundColour = (0, 0, 0)

fireworkPhase = 0
maxFireworkPhase = 25
pointVelocity = 4 # pixels per frame
explosionType = 1 # 0: Front point is the biggest. - 1: Points have random sizes

totalExecutionTime = 0
extraCharWidth = 5
numberOfClicks = 0



def centerOfLetters(textFontSize, text):
    textCenters = [0]  # center of letters
    charWidthList = character(textFontSize, (1, 1, 1), text)
    for i in range(len(text)):
        charWidth = charWidthList[i] // 2
        lastCharWidth = textCenters[i]
        if i == 0:
            point = ((WIDTH - sum(charWidthList[1:]) - extraCharWidth * (len(text) - 1)) // 2, HEIGHT // 2)
        else:
            point = (textCenters[i - 1][0] + lastCharWidth + extraCharWidth + charWidth, HEIGHT // 2)
        textCenters[i] = point
        textCenters.append(charWidth)
    textCenters.pop(-1)
    return textCenters


def character(textFontSize, colour, text, textHeight=None):
    charWidthList = []
    font = pygame.font.Font('freesansbold.ttf', textFontSize)
    if not colour == (1, 1, 1):
        textCenters = centerOfLetters(textFontSize, text)
    for i in range(len(text)):
        char = font.render(text[i], True, colour)
        charRect = char.get_rect()
        if not colour == (1, 1, 1): # not centers
            if textHeight is None:
                charRect.center = textCenters[i]
            else:
                charRect.center = (textCenters[i][0], textHeight)
            screen.blit(char, charRect)
            pygame.display.flip()
        charWidthList.append(charRect[2])
    return charWidthList


def findPoints(centers, charWidthList):
    pointList = []
    numberOfPoints = 0
    for index in range(len(word)):
        foundPoints = []
        xLeft = centers[index][0] - charWidthList[index] // 2
        for pointY in range(extraCharWidth, HEIGHT-extraCharWidth, pointDensity):
            for pointX in range(xLeft, xLeft + charWidthList[index] , pointDensity):
                pointP = (pointX, pointY)
                pixelColour = screen.get_at(pointP)[:3]
                if pixelColour != backgroundColour:
                    foundPoints.append(pointP)
        pointList.append(foundPoints)
        numberOfPoints += len(foundPoints)
    # print(pointList)
    return pointList, numberOfPoints


def draw(pointList, centers):
    if fireworkPhase + len(colourGradients) >= maxFireworkPhase:
        phase = maxFireworkPhase - len(colourGradients) - 1
    else:
        phase = fireworkPhase
    for letter in range(len(word)):
        for p in range(phase, 0, -1):
            if state == "Rising":
                xB = centers[letter][0]
                yB = HEIGHT - (HEIGHT // (2 * (maxFireworkPhase - len(colourGradients) - 1))) * p

                colourIndex = fireworkPhase - p
                if colourIndex >= len(colourGradients):
                    break
                if yB == centers[letter][1]:
                    colourIndex = 0
                colour = colourGradients[colourIndex]

                if explosionType == 0:
                    pygame.draw.circle(screen, colour, (xB, yB), (6-colourIndex)/2)
                else:
                    pygame.draw.circle(screen, colour, (xB, yB), random.randint(1, 3))
            elif state == "Exploding":
                for i in range(len(pointList[letter])):
                    pointP = pointList[letter][i]
                    distancePCenter = math.sqrt(
                        (centers[letter][0] - pointP[0]) ** 2 + (centers[letter][1] - pointP[1]) ** 2)
                    distanceBCenter = distancePCenter / (maxFireworkPhase - len(colourGradients) - 1) * p
                    anglePCenter = math.atan2(pointP[1] - centers[letter][1], pointP[0] - centers[letter][0])
                    xB = int(distanceBCenter * math.cos(anglePCenter)) + centers[letter][0]
                    yB = int(distanceBCenter * math.sin(anglePCenter)) + centers[letter][1]
                    colourIndex = fireworkPhase - p
                    if colourIndex >= len(colourGradients):
                        break
                    colour = colourGradients[colourIndex]

                    pixelIndex = len(colourGradients)
                    pixelColour = screen.get_at((xB, yB))
                    for ii in range(len(colourGradients)):
                        if pixelColour == colourGradients[ii]:
                            pixelIndex = ii
                            break

                    if pixelIndex > colourIndex:
                        if explosionType == 0:
                            pygame.draw.circle(screen, colour, (xB, yB), (6 - colourIndex) / 2)
                        else:
                            pygame.draw.circle(screen, colour, (xB, yB), random.randint(1, 3))


while not state == "End":
    startTime = time.time()
    if state == "Setup":
        charWidthList = character(fontSize, (1, 1, 1), word)
        centers = centerOfLetters(fontSize, word)

        charWidthList = character(fontSize, endColour, word)
        pointList, numberOfPoints = findPoints(centers, charWidthList)
        screen.fill(backgroundColour)

        print(numberOfPoints, numberOfPoints * len(colourGradients), sep=", ")
        state = "Rising"
        fireworkPhase = 0
    elif state == "Rising" or state == "Exploding":
        screen.fill(backgroundColour)
        draw(pointList, centers)
        fireworkPhase += 1
        if fireworkPhase == maxFireworkPhase:
            if state == "Rising":
                state = "Exploding"
            elif state == "Exploding":
                state = "Pause"
                character(fontSize, colourGradients[-1], word)
            fireworkPhase = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = "End"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            numberOfClicks += 1

    if numberOfClicks > 0 and state == "Pause":
        state = "Rising"
        numberOfClicks -= 1

    pygame.display.flip()

    executionTime = time.time() - startTime
    if state == "Rising" or state == "Exploding":
        totalExecutionTime += executionTime
        if fireworkPhase + len(colourGradients) >= maxFireworkPhase:
            time.sleep(0.02)
        time.sleep(0.01)
    elif totalExecutionTime != 0:
        print(totalExecutionTime)
        totalExecutionTime = 0

    # pygame.time.Clock.tick(40)
