from locale import currency

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

class Fireworks:
    def __init__(self, pointList, center, radius, explosionType, state, currentPhase):
        self.pointList = pointList
        self.center = center
        self.radius = radius
        self.explosionType = explosionType
        self.state = state
        self.currentPhase = currentPhase


    def findCirclePoints(self):
        self.pointList = []
        numberOfPoints = 0
        for alpha in range(0, 360, 2):
            angle = random.randint(0, 4) + alpha
            deltaX = self.radius * math.sin(angle * math.pi / 180)
            deltaY = self.radius * math.cos(angle * math.pi / 180)
            point = (self.center[0] - deltaX, self.center[1] - deltaY)
            self.pointList.append(point)
        # print(self.pointList)
        return self.pointList


    def draw(self):
        screen.fill('black')
        if self.currentPhase + len(colourGradients) >= maxFireworkPhase:
            phase = maxFireworkPhase - len(colourGradients) - 1
        else:
            phase = self.currentPhase

        if self.state == "Rising":
            for p in range(phase, 0, -1):
                xB = self.center[0]
                yB = h - ((h - self.center[1]) // (maxFireworkPhase - len(colourGradients) - 2)) * p

                colourIndex = self.currentPhase - p
                if colourIndex >= len(colourGradients):
                    break
                if yB == self.center[1]:
                    colourIndex = 0
                colour = colourGradients[colourIndex]

                if self.explosionType == 0:
                    pygame.draw.circle(screen, colour, (xB, yB), (6 - colourIndex) / 2)
                else:
                    pygame.draw.circle(screen, colour, (xB, yB), random.randint(1, 3))
        elif self.state == "Exploding":
            for i in range(len(self.pointList)):
                for p in range(self.currentPhase, 0, -1):
                    pointP = self.pointList[i]
                    distanceBCenter = self.radius / (maxFireworkPhase - len(colourGradients) - 1) * p
                    anglePCenter = math.atan2(pointP[1] - self.center[1], pointP[0] - self.center[0])
                    xB = int(distanceBCenter * math.cos(anglePCenter)) + self.center[0]
                    yB = int(distanceBCenter * math.sin(anglePCenter)) + self.center[1]

                    colourIndex = - 1 - (p * len(colourGradients) // maxFireworkPhase)

                    if self.explosionType == 0:
                        pygame.draw.line(screen, colourGradients[colourIndex], self.center,(xB, yB), (6 - colourIndex) // 2)
                    else:
                        pygame.draw.line(screen, colourGradients[colourIndex], self.center,(xB, yB), random.randint(1, 3))




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
                    distancePCenter = radiusList[firework]
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

firework1 = Fireworks([], (w // 2, h // 2), 100, 0, "Pause", 0)

running = True
while running:
    startTime = time.time()
    if firework1.state == "Setup":
        firework1.pointList = firework1.findCirclePoints()
        numberOfPoints = len(firework1.pointList)
        print(numberOfPoints)
        firework1.state = "Rising"
    elif firework1.state == "Rising" or firework1.state == "Exploding":
        screen.fill(backgroundColour)
        firework1.draw()
        firework1.currentPhase += 1
        if firework1.currentPhase == maxFireworkPhase:
            if firework1.state == "Rising":
                firework1.state = "Exploding"
            elif firework1.state == "Exploding":
                firework1.state = "Pause"
            firework1.currentPhase = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            numberOfClicks += 1

    if numberOfClicks > 0 and firework1.state == "Pause":
        firework1.state = "Setup"
        numberOfClicks -= 1

    pygame.display.flip()

    if firework1.state == "Rising":
        time.sleep(0.01)
    elif firework1.state == "Exploding" and firework1.currentPhase + len(colourGradients) >= maxFireworkPhase:
        time.sleep(0.08)
    time.sleep(0.01)

    if totalExecutionTime != 0 and firework1.state == "Pause":
        print(totalExecutionTime)
        totalExecutionTime = 0
    elif firework1.state != "Pause":
        executionTime = time.time() - startTime
        totalExecutionTime += executionTime
        startTime = time.time()
