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
pointDensity = 10  # Higher values mean less particles thus faster
backgroundColour = (0, 0, 0)

fireworkPhase = 0
maxFireworkPhase = 50
pointVelocity = 4 # pixels per frame
explosionType = 0 # 0: Front point is the biggest. - 1: Points have random sizes

totalExecutionTime = 0
numberOfClicks = 0

numberOfFireworks = 6
circleThickness = 10

centerList = [(w/2, h/2)]
radiusList = [200]

def findCirclePoints(centers, r):
    pointList = []
    numberOfPoints = 0
    for index in range(len(centers)):
        foundPoints = []
        for alpha in range(0, 360, 2):
            angle = random.randint(0, 4) + alpha
            deltaX = r[index] * math.sin(angle * math.pi / 180)
            deltaY = r[index] * math.cos(angle * math.pi / 180)
            point = (centers[index][0] - deltaX, centers[index][1] - deltaY)
            foundPoints.append(point)
        pointList.append(foundPoints)
        numberOfPoints += len(foundPoints)
    print(pointList)
    return pointList, numberOfPoints


def draw(pointList, centers):
    if fireworkPhase + len(colourGradients) >= maxFireworkPhase:
        phase = maxFireworkPhase - len(colourGradients) - 1
    else:
        phase = fireworkPhase
    for firework in range(len(centers)):
        for p in range(phase, 0, -1):
            if state == "Rising":
                xB = centers[firework][0]
                yB = h - ((h - centers[firework][1]) // (maxFireworkPhase - len(colourGradients) - 2)) * p

                colourIndex = fireworkPhase - p
                if colourIndex >= len(colourGradients):
                    break
                if yB == centers[firework][1]:
                    colourIndex = 0
                colour = colourGradients[colourIndex]

                if explosionType == 0:
                    pygame.draw.circle(screen, colour, (xB, yB), (6-colourIndex)/2)
                else:
                    pygame.draw.circle(screen, colour, (xB, yB), random.randint(1, 3))
            elif state == "Exploding":
                for i in range(len(pointList[firework])):
                    pointP = pointList[firework][i]
                    distancePCenter = randomRadiusList[i]
                    distanceBCenter = distancePCenter / (maxFireworkPhase - len(colourGradients) - 1) * p
                    anglePCenter = math.atan2(pointP[1] - centers[firework][1], pointP[0] - centers[firework][0])
                    xB = int(distanceBCenter * math.cos(anglePCenter)) + centers[firework][0]
                    yB = int(distanceBCenter * math.sin(anglePCenter)) + centers[firework][1]
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
        for i in range(len(centerList)):
            pygame.draw.circle(screen, 'white', centerList[i], radiusList[i], circleThickness)
        pointList, numberOfPoints = findCirclePoints(centerList, radiusList)
        screen.fill(backgroundColour)

        print(numberOfPoints, numberOfPoints * len(colourGradients), sep=", ")
        state = "Rising"
        fireworkPhase = 0

        randomRadiusList = []
        for i in range(len(pointList[0])):
            randomRadiusList.append(radiusList[0] - random.randint(0, 150))
    elif state == "Rising" or state == "Exploding":
        screen.fill(backgroundColour)
        draw(pointList, centerList)
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
        state = "Setup"
        numberOfClicks -= 1

    pygame.display.flip()

    if state == "Rising":
        time.sleep(0.01)
    elif state == "Exploding" and fireworkPhase + len(colourGradients) >= maxFireworkPhase:
        time.sleep(0.08)
    time.sleep(0.01)

    if totalExecutionTime != 0 and state == "Pause":
        print(totalExecutionTime)
        totalExecutionTime = 0
    elif state != "Pause":
        executionTime = time.time() - startTime
        totalExecutionTime += executionTime
        startTime = time.time()
