import pygame
import math
import time
import random
from pygame import K_TAB, K_RETURN, K_BACKSPACE

pygame.init()

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
w, h = pygame.display.get_window_size()

# word = "2025"
# word = "Happy new Baguette"
fontSize = 200
inputFontSize = 30
inputHeight = 20
colourGradients = [(224, 78, 31), (255, 186, 48), (255, 208, 114),
                   (255, 251, 129), (184, 190, 184), (207, 213, 206)]
endColour = (40, 40, 40)
pygame.display.set_caption("Fireworks")

state = "Setup" # Setup, Rising, Exploding, Pause, Typing, Writing, End
pointDensity = 2  # Higher values mean less particles thus faster
backgroundColour = (0, 0, 0)

fireworkPhase = 0
maxFireworkPhase = 25
pointVelocity = 4 # pixels per frame
explosionType = 1 # 0: Front point is the biggest. - 1: Points have random sizes

totalExecutionTime = 0
extraCharWidth = 5
numberOfClicks = 0
backspacePause = None
h = fontSize + 2 * extraCharWidth
setupSentence = "Type your word:    "

centers = [(w//2, h//2)]
r = 20


def findPoints(centers, r):
    pointList = []
    numberOfPoints = 0
    for index in range(len(centers)):
        foundPoints = []
        xCorner = centers[index][0] - r
        yCorner = centers[index][1] - r
        for pointY in range(yCorner, yCorner + 2 * r, pointDensity):
            for pointX in range(xCorner, xCorner + 2 * r , pointDensity):
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
    for letter in range(len(centers)):
        for p in range(phase, 0, -1):
            if state == "Rising":
                xB = centers[letter][0]
                yB = h - (h // (2 * (maxFireworkPhase - len(colourGradients) - 1))) * p

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
        pygame.draw.circle(screen, 'white', centers[0], r)
        pointList, numberOfPoints = findPoints(centers, r)
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
