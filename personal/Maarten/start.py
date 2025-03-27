import pygame
import math
from button_code import *
from firework_function import *

screen = pygame.display.set_mode((1366, 668), pygame.RESIZABLE)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.font.init()


def textOutline(text, textSize, textColour, outlineColour, outlineThickness, center):
    textPrint(text, textSize, outlineColour, (center[0] - outlineThickness, center[1] - outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] - outlineThickness, center[1] + outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] + outlineThickness, center[1] - outlineThickness))
    textPrint(text, textSize, outlineColour, (center[0] + outlineThickness, center[1] + outlineThickness))
    textPrint(text, textSize, textColour, center)

pygame.draw.line(screen, 'white', (12.31, 32.9), (-238, 33.4))

textOutline("yippeee", 120, 'black', 'white', 2, (WIDTH/2, HEIGHT/2))
pygame.display.flip()
alpha = 0
while True:
    pygame.draw.arc(screen, 'red', pygame.Rect(100, 100, 200, 200), 0, alpha , 5)
    alpha += 6 * math.pi / 180
    pygame.display.flip()
    time.sleep(0.1)
    break
screen.fill('black')
fireworkWord("Thanks for playing", 100)

#All objects
playerObject = Objects(-90 , 450, 50, 50, 'green', 2, 0, 0, [1], "Player")
cube1_1 = Objects(-500, 500, 900, 1500, 'black', 1, 0, 0, [1], "Collider")
cube1_2 = Objects(400, 580, 570, 950, 'black', 1, 0, 0, [1], "Collider")
cube1_3 = Objects(833, 428, 600, 2430, 'black', 1, 0, 0, [1], "Collider")
cube1_4 = Objects(-200, 320, 80, 180, 'orange', 1, 0, 0, [1], enemy("BOB", (255, 255, 0), 100, ["punch"], 0))
cube1_5 = Objects(-550, 29, 250, 571, 'black', 1, 0, 0, [1], "Collider")

cube2_1 = Objects(461, 581, 412, 500, 'black', 1, 0, 0, [2], "Collider")
cube2_2 = Objects(-700, 428, 887, 500, 'black', 1, 0, 0, [2], "Collider")
cube2_3 = Objects(1109, 481, 350, 500, 'black', 1, 0, 0, [2], "Collider")
cube2_4 = Objects(700, 300, 131, 58, 'black', 1, 0, 0, [2], "Collider")
cube2_5 = Objects(344, 100, 213, 15, 'black', 1, 0, 0, [2], "Collider")

cube4_1 = Objects(564, 116, 3500, 2000, 'black', 1, 0, 0, [4], "Collider")
cube4_2 = Objects(-500, 530, 576, 500, 'black', 1, 0, 0, [4], "Collider")
cube4_3 = Objects(365, 420, 313, 500, 'black', 1, 0, 0, [4], "Collider")
cube4_4 = Objects(365, 430, 313, 54, 'black', 1, 0, 0, [4], "Collider")
cube4_5 = Objects(22, 200, 150, 54, 'black', 1, 0, 0, [4], "Collider")
cube4_6 = Objects(-417, 93, 150, 20, 'black', 1, 0, 0, [4], "Collider")

cube5_1  = Objects(-500, 130, 218, 1000, 'black', 1, 0, 0, [5], "Collider")
cube5_2 =  Objects(-326, 400, 284, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_3 =  Objects(69, 200, 1000, 30, 'black', 1, 0, 0, [5], "Collider")
cube5_4 =  Objects(430, 467, 70, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_5 =  Objects(70, 630, 70, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_6 = Objects(850, 620, 110, 500, 'black', 1, 0, 0, [5], "Collider")
cube5_7 = Objects(1223, 400, 200, 500, 'black', 1, 0, 0, [5], "Collider")

cube6_1 = Objects(-500, 410, 200, 700, 'black', 1, 0, 0, [6], "Collider")
cube6_2 = Objects(-27, 544, 150, 300, 'black', 1, 0, 0, [6], "Collider")
cube6_3 = Objects(425, 431, 150, 400, 'black', 1, 0, 0, [6], "Collider")
cube6_4 = Objects(828, 250, 150, 800, 'black', 1, 0, 0, [6], "Collider")
cube6_5 = Objects(1200, 380, 200, 500, 'black', 1, 0, 0, [6], "Collider")

cube7_1 = Objects(-500, 415, 300, 500, 'black', 1, 0, 0, [7], "Collider")
cube7_2 = Objects(35, 650, 830, 300, 'black', 1, 0, 0, [7], "Collider")
cube7_3 = Objects(1100, 430, 300, 500, 'black', 1, 0, 0, [7], "Collider")

cube8_1 = Objects(-500, 435, 300, 500, 'black', 1, 0, 0, [8], "Collider")
cube8_2 = Objects(-206, 525, 540, 400, 'black', 1, 0, 0, [8], "Collider")
cube8_3 = Objects(250, 630, 1500, 300, 'black', 1, 0, 0, [8], "Collider")
cube8_4 = Objects(1150, 0, 400, 440, 'black', 1, 0, 0, [8], "Collider")

cube10_1 = Objects(-500, 635, 2500, 445, 'black', 1, 0, 0, [10], "Collider")
cube10_2 = Objects(-200, 530, 470, 180, 'black', 1, 0, 0, [10], "Collider")
cube10_3 = Objects(125, 365, 525, 325, 'black', 1, 0, 0, [10], "Collider")
cube10_4 = Objects(625, 500, 430, 250, 'black', 1, 0, 0, [10], "Collider")
cube10_5 = Objects(1025, 280, 400, 475, 'black', 1, 0, 0, [10], "Collider")

cube10_6 = Objects(460, 0, 60, 60, 'red', 1, 0, 0, [10], MoveObject((460, -100), (460, 2000), 0.5, 10, False, 100))
cube10_7 = Objects(1050, 600, 60, 60, 'red', 1, 0, 0, [10], MoveObject((1050, -100), (1050, 2000), 0.4, 10, False, 100))
cube10_8 = Objects(150, 300, 60, 60, 'red', 1, 0, 0, [10], MoveObject((150, -100), (150, 2000), 0.6, 10, False, 100))

cube11_1 = Objects(-500, 285, 400, 600, 'black', 1, 0, 0, [11], "Collider")
cube11_2 = Objects(216, 400, 475, 370, 'black', 1, 0, 0, [11], "Collider")
cube11_3 = Objects(1050, 500, 350, 300, 'black', 1, 0, 0, [11], "Collider")

cube11_4 = Objects(0, -100, 60, 60, 'red', 1, 0, 0, [11], MoveObject((0, -100), (0, 2000), 1, 10, False, 0))
cube11_5 = Objects(50, -250, 60, 60, 'red', 1, 0, 0, [11], MoveObject((50, -100), (50, 2000), 1, 10, False, 0))
cube11_6 = Objects(790, -100, 150, 150, 'red', 1, 0, 0, [11], MoveObject((790, -100), (790, 2000), 0.8, 10, False, 0))
cube11_7 = Objects(800, 1000, 150, 150, 'red', 1, 0, 0, [11], MoveObject((790, -100), (790, 2000), 0.8, 10, False, 0))

cube12_1 = Objects(-500, 505, 350, 300, 'black', 1, 0, 0, [12], "Collider")
cube12_2 = Objects(-160, 575, 600, 250, 'black', 1, 0, 0, [12], "Collider")
cube12_3 = Objects(285, 480, 540, 290, 'black', 1, 0, 0, [12], "Collider")
cube12_4 = Objects(810, 520, 560, 250, 'black', 1, 0, 0, [12], "Collider")
cube12_13_1 = Objects(335, 0, 150, 350, 'black', 1, 0, 0, [12, 13], "Collider")

cube12_13_2 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.63, 10, False, 200))
cube12_13_3 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.73, 10, False, 200))
cube12_13_4 = Objects(-100, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((-100, -100), (-100, 2000), 0.5, 10, False, 200))
cube12_13_5 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.8, 10, False, 400))
cube12_13_6 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.75, 10, False, 400))
cube12_13_7 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.7, 10, False, 400))
cube12_13_8 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.55, 10, False, 400))
cube12_13_9 = Objects(900, 1000, 50, 50, 'red', 1, 0, 0, [12, 13], MoveObject((900, -100), (900, 2000), 0.65, 10, False, 400))

cube13_1 = Objects(-500, 525, 250, 300, 'black', 1, 0, 0, [13], "Collider")
cube13_2 = Objects(285, 480, 320, 380, 'black', 1, 0, 0, [13], "Collider")
cube13_3 = Objects(-50, 360, 150, 500, 'black', 1, 0, 0, [13], "Collider")
cube13_4 = Objects(910, 380, 500, 400, 'black', 1, 0, 0, [13], "Collider")

cube14_1 = Objects(-500, 385, 500, 400, 'black', 1, 0, 0, [14], "Collider")
cube14_2 = Objects(222, 450, 130, 30, 'black', 1, 0, 0, [14], "Collider")
cube14_3 = Objects(555, 360, 130, 30, 'black', 1, 0, 0, [14], "Collider")
cube14_4 = Objects(1165, 650,250 , 500, 'black', 1, 0, 0, [14], "Collider")
cube14_5 = Objects(888, 540, 130, 30, 'black', 1, 0, 0, [14], "Collider")
cube14_6 = Objects(1165, 0, 250, 350, 'black', 1, 0, 0, [14], "Collider")

cube14_7 = Objects(227, 1000, 120, 120, 'red', 1, 0, 0, [14], MoveObject((227, -100), (227, 2500), 0.7, 10, False, 0))
cube14_8 = Objects(888, 0, 120, 120, 'red', 1, 0, 0, [14], MoveObject((888, -100), (888, 2500), 0.7, 10, False, 0))
cube14_9 = Objects(555, 500, 120, 120, 'red', 1, 0, 0, [14], MoveObject((555, -100), (555, 2500), 0.7, 10, False, 0))

cube15_1 = Objects(-500, 650, 2000, 500, 'black', 1, 0, 0, [15], "Collider")
cube15_2 = Objects(-500, 190, 2000, 250, 'black', 1, 0, 0, [15], "Collider")
cube15_3 = Objects(-500, 0, 300, 350, 'black', 1, 0, 0, [15], "Collider")
cube15_4 = Objects(1100, 0, 300, 350, 'black', 1, 0, 0, [15], "Collider")

cube15_5 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 4, 10, False, 500))
cube15_6 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 4.5, 10, False, 500))
cube15_7 = Objects(400, -500, 50, 50, 'red', 1, 0, 0, [15], MoveObject((400, -100), (400, 190), 5.5, 10, False, 500))

# voeg hier nieuwe platformen to zodat ze collision krijgen.
platforms = [cube1_1, cube1_2, cube1_3, cube1_4, cube1_5,
             cube2_1, cube2_1, cube2_2, cube2_3, cube2_4, cube2_5,
             cube4_1, cube4_2, cube4_3, cube4_4, cube4_5, cube4_6,
             cube5_1, cube5_2, cube5_3, cube5_4, cube5_5, cube5_6, cube5_7,
             cube6_1, cube6_2, cube6_3, cube6_4, cube6_5,
             cube7_1, cube7_2, cube7_3,
             cube8_1, cube8_2, cube8_3, cube8_4,
             cube10_1, cube10_2, cube10_3, cube10_4, cube10_5, cube10_6, cube10_7, cube10_8,
             cube11_1, cube11_2, cube11_3, cube11_4, cube11_5, cube11_6, cube11_7,
             cube12_1, cube12_2, cube12_3, cube12_4,
             cube12_13_1, cube12_13_2, cube12_13_3, cube12_13_4, cube12_13_5, cube12_13_6, cube12_13_7, cube12_13_8, cube12_13_9,
             cube13_1, cube13_2, cube13_3, cube13_4,
             cube14_1, cube14_2, cube14_3, cube14_4, cube14_5, cube14_6, cube14_7, cube14_8, cube14_9,
             cube15_1, cube15_2, cube15_3,cube15_4, cube15_5, cube15_6, cube15_7]