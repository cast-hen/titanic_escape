from fighting_functions import *
from common import *
import pygame

screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()

punch = move("punch", "Hits the opponent \n for 10 damage", pygame.image.load('resources/textures/move_punch.png'))
comboPunch = move("combo punch", "Hits the opponent a \n random number of times", pygame.image.load('resources/textures/move_comboPunch.png'))
devTestInstakill = move("devtest instakill", "for developer purposes only", '')

#Enemies
enemy_image_size = (86, 280)
enemyJAN_1 = character("Robert John Adams", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl0.png'), enemy_image_size), 25, 50,["punch"], [], 0, True, True)
enemyBOBJAN_1 = character("Alfred Samuel Allsop", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl0.png'), enemy_image_size), 30, 30,["combo punch"], [], 0, True, False)
enemyBOBBOBBOB_1 = character("Ernest Owen Abbott", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl2.png'), enemy_image_size), 30, 30,["punch", "poison"], [], 0, True, False)
enemyBobbie_1 = character("Percy Snowden Ahier", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl2.png'), enemy_image_size), 50, 50,["punch", "combo punch", "poison"], [], 1, True, True)

enemyWillem_1 = character("Henry Allen", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl1.png'), enemy_image_size), 50, 50,["punch", "punch", "enrage"], [], 0, True, False)
enemyAlexander_1 = character("Charles Edward Andrews", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl1.png'), enemy_image_size), 50, 50,["punch", "combo punch", "block"], [], 1, True, False)
enemyWillem_Henk_1 = character("Anthony Abbing", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl2.png'), enemy_image_size), 60, 60,["enrage", "combo punch", "poison"], [], 0, True, False)
enemyBoze_Jantje_1 = character("William Thomas Abrams", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl2.png'), enemy_image_size), 60, 60,["block", "poison", "punch"], [
    item("Poison bottle", 2)
], 2, True, False)
enemyKwaardaardige_BOB_1 = character("Ernest Edward Archer", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl3.png'), enemy_image_size), 75, 75,["punch", "enrage", "block"], [
    item("Bomb", 1)
], 5, True, True)
enemyBoudewijn_1 = character("John Anderson", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl2.png'), enemy_image_size), 60, 60,["life steal"], [
    item("Bomb", 1)
], 2, True, False)
enemyRoderick_1 = character("Frank Richard Allsop", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl3.png'), enemy_image_size), 70, 70,["punch", "life steal", "block"], [], 2, True, False)
enemyKleine_Karel_1 = character("Joseph Groves Boxhall", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl3.png'), enemy_image_size), 80, 80,["combo punch", "life steal", "poison"], [], 1, True, False)
enemyIni_Mini_1 = character("Robert Spencer Allen", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl4.png'), enemy_image_size), 100, 100,["life steal", "enrage", "block", "punch"], [
    item("Bomb", 2)
], 0, True, True)
enemyBOSS_1 = character("Captain Edward Smith", 1, pygame.transform.scale(pygame.image.load('resources/textures/enemy_lvl5.png'), enemy_image_size), 200, 150,["punch", "combo punch", "enrage", "block", "life steal"], [
    item("Full Restore", 1),
    item("Bomb", 2)
], 2, True, False)

# Object of the player
playerObject = Objects(game_manager.Player_posx, game_manager.Player_posy, 88, 32, pygame.transform.scale(pygame.image.load("resources/textures/rat_idle.png"), (88, 32)), 2, 0, 0, [1], "Player")
# Player textures
player_Right = pygame.transform.scale(pygame.image.load("resources/textures/rat_walk.png"), (playerObject.width, playerObject.height))
player_Left = pygame.transform.flip(player_Right, True, False)
player_Jump_Right = pygame.transform.scale(pygame.image.load("resources/textures/rat_jump.png"), (playerObject.width, playerObject.height))
player_Jump_Left =  pygame.transform.flip(player_Jump_Right, True, False)
player_idle = pygame.transform.scale(pygame.image.load("resources/textures/rat_idle.png"), (playerObject.width, playerObject.height))
player_idle_Left = pygame.transform.flip(player_idle, True, False)

# No left border transition anymore? Then here rectangle to stop player going there.
cube_LeftBorder = Objects(-501, 0, 1, HEIGHT, 'black', 1, 0, 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], "Collider")

enemy_paste_height = enemy_image_size[1] # height of enemy image. Used for placement
# For every enemy: ypos = ypos of cube it's standing on - enemy_paste_height
# Every object
cube1_1 = Objects(-300, 490, 700, 1500, 'floor', 1, 0, 0, [1], "Collider")
cube1_2 = Objects(400, 580, 433, 950, 'floor', 1, 0, 0, [1], "Collider")
cube1_3 = Objects(833, 428, 600, 2430, 'floor3D', 1, 0, 0, [1], "Collider")
cube1_4 = Objects(-500, 170, 240, 600, 'wall', 1, 0, 0, [1], "Collider")
cube1_Enemy1 = Objects(1050, cube1_3.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [1], enemyJAN_1)

cube2_1 = Objects(461, 581, 412, 500, 'floor3D', 1, 0, 0, [2], "Collider")
cube2_2 = Objects(-500, 428, 687, 500, 'floor', 1, 0, 0, [2], "Collider")
cube2_3 = Objects(1109, 481, 350, 500, 'floor3D', 1, 0, 0, [2], "Collider")
cube2_4 = Objects(700, 300, 131, 58, 'floating', 1, 0, 0, [2], "Collider")
cube2_5 = Objects(344, 100, 213, 15, 'floating', 1, 0, 0, [2], "Collider")

cube3_1 = Objects(564, 116, 3500, 2000, 'floor', 1, 0, 0, [3], "Collider")
cube3_2 = Objects(-500, 530, 576, 500, 'floor', 1, 0, 0, [3], "Collider")
cube3_3 = Objects(364, 420, 200, 500, 'floor', 1, 0, 0, [3], "Collider")
cube3_4 = Objects(22, 200, 150, 54, 'floating', 1, 0, 0, [3], "Collider")
cube3_5 = Objects(-417, 93, 150, 20, 'floating', 1, 0, 0, [3], "Collider")
cube3_Enemy1 = Objects(1040, cube3_1.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [3], enemyBOBJAN_1)

cube4_1  = Objects(-500, 130, 218, 1000, 'floor', 1, 0, 0, [4], "Collider")
cube4_2 =  Objects(-282, 400, 240, 500, 'floor', 1, 0, 0, [4], "Collider")
cube4_3 =  Objects(69, 200, 1000, 30, 'floating', 1, 0, 0, [4], "Collider")
cube4_4 =  Objects(430, 467, 70, 500, 'pillar', 1, 0, 0, [4], "Collider")
cube4_5 =  Objects(70, 630, 70, 500, 'pillar', 1, 0, 0, [4], "Collider")
cube4_6 = Objects(850, 620, 110, 500, 'pillar', 1, 0, 0, [4], "Collider")
cube4_7 = Objects(1223, 400, 200, 500, 'floor', 1, 0, 0, [4], "Collider")
cube4_Enemy1 = Objects(640, cube4_3.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [4], enemyBOBBOBBOB_1)

cube5_1 = Objects(-500, 410, 200, 700, 'floor', 1, 0, 0, [5], "Collider")
cube5_2 = Objects(-27, 544, 150, 300, 'pillar', 1, 0, 0, [5], "Collider")
cube5_3 = Objects(425, 431, 150, 400, 'pillar', 1, 0, 0, [5], "Collider")
cube5_4 = Objects(828, 250, 150, 800, 'pillar', 1, 0, 0, [5], "Collider")
cube5_5 = Objects(1200, 380, 200, 500, 'floor', 1, 0, 0, [5], "Collider")

cube6_1 = Objects(-500, 415, 300, 500, 'floor', 1, 0, 0, [6], "Collider")
cube6_2 = Objects(35, 650, 830, 300, 'floor', 1, 0, 0, [6], "Collider")
cube6_3 = Objects(1100, 430, 300, 500, 'floor', 1, 0, 0, [6], "Collider")
cube6_Enemy1 = Objects(590, cube6_2.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [6], enemyBobbie_1)

cube7_1 = Objects(-500, 435, 300, 500, 'floor', 1, 0, 0, [7], "Collider")
cube7_2 = Objects(-200, 525, 540, 400, 'floor', 1, 0, 0, [7], "Collider")
cube7_3 = Objects(340, 630, 1500, 300, 'floor', 1, 0, 0, [7], "Collider")
cube7_4 = Objects(1150, 0, 400, 440, 'wall', 1, 0, 0, [7], "Collider")

cube9_1 = Objects(-500, 635, 300, 150, 'floor', 1, 0, 0, [9], "Collider")
cube9_2 = Objects(-200, 530, 325, 250, 'floor', 1, 0, 0, [9], "Collider")
cube9_3 = Objects(125, 365, 525, 420, 'floor', 1, 0, 0, [9], "Collider")
cube9_4 = Objects(650, 500, 375, 280, 'floor', 1, 0, 0, [9], "Collider")
cube9_5 = Objects(1025, 280, 400, 500, 'floor', 1, 0, 0, [9], "Collider")
cube9_Enemy1 = Objects(825, cube9_4.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [9], enemyWillem_1)

cube9_6 = Objects(460, 0, 60, 60, 'Falling Block', 1, 0, 0, [9], MoveObject((460, -100), (460, 2000), 0.5, 10, False, 100))
cube9_7 = Objects(1050, 600, 60, 60, 'Falling Block', 1, 0, 0, [9], MoveObject((1050, -100), (1050, 2000), 0.4, 10, False, 100))
cube9_8 = Objects(150, 300, 60, 60, 'Falling Block', 1, 0, 0, [9], MoveObject((150, -100), (150, 2000), 0.6, 10, False, 100))

cube10_1 = Objects(-500, 285, 400, 600, 'floor', 1, 0, 0, [10], "Collider")
cube10_2 = Objects(216, 400, 475, 370, 'floor', 1, 0, 0, [10], "Collider")
cube10_3 = Objects(1050, 500, 350, 300, 'floor', 1, 0, 0, [10], "Collider")
cube10_Enemy1 = Objects(485, cube10_2.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [10], enemyAlexander_1)

cube10_4 = Objects(0, -100, 60, 60, 'Falling Block', 1, 0, 0, [10], MoveObject((0, -100), (0, 2000), 1, 10, False, 0))
cube10_5 = Objects(50, -250, 60, 60, 'Falling Block', 1, 0, 0, [10], MoveObject((50, -100), (50, 2000), 1, 10, False, 0))
cube10_6 = Objects(790, -100, 150, 150, 'Falling Block', 1, 0, 0, [10], MoveObject((790, -100), (790, 2000), 0.8, 10, False, 0))
cube10_7 = Objects(800, 1000, 150, 150, 'Falling Block', 1, 0, 0, [10], MoveObject((790, -100), (790, 2000), 0.8, 10, False, 0))

cube11_1 = Objects(-500, 505, 350, 300, 'floor', 1, 0, 0, [11], "Collider")
cube11_2 = Objects(-150, 575, 435, 250, 'floor', 1, 0, 0, [11], "Collider")
cube11_3 = Objects(285, 480, 540, 290, 'floor', 1, 0, 0, [11], "Collider")
cube11_4 = Objects(825, 520, 560, 250, 'floor', 1, 0, 0, [11], "Collider")

cube11_12_1 = Objects(335, 0, 150, 350, 'wall', 1, 0, 0, [11, 12], "Collider")
cube11_12_2 = Objects(-100, 1000, 50, 50, 'Falling Block', 1, 0, 0, [11, 12], MoveObject((-100, -100), (-100, 2000), 0.63, 10, False, 150))
cube11_12_3 = Objects(-100, 1000, 50, 50, 'Falling Block', 1, 0, 0, [11, 12], MoveObject((-100, -100), (-100, 2000), 0.73, 10, False, 150))
cube11_12_4 = Objects(-100, 1000, 50, 50, 'Falling Block', 1, 0, 0, [11, 12], MoveObject((-100, -100), (-100, 2000), 0.5, 10, False, 150))
cube11_12_5 = Objects(900, 1000, 50, 50, 'Falling Block', 1, 0, 0, [11, 12], MoveObject((900, -100), (900, 2000), 0.8, 10, False, 400))
cube11_12_6 = Objects(900, 1000, 50, 50, 'Falling Block', 1, 0, 0, [11, 12], MoveObject((900, -100), (900, 2000), 0.75, 10, False, 400))
cube11_12_7 = Objects(900, 1000, 50, 50, 'Falling Block', 1, 0, 0, [11, 12], MoveObject((900, -100), (900, 2000), 0.7, 10, False, 400))
cube11_12_8 = Objects(900, 1000, 50, 50, 'Falling Block', 1, 0, 0, [11, 12], MoveObject((900, -100), (900, 2000), 0.55, 10, False, 400))
cube11_12_9 = Objects(900, 1000, 50, 50, 'Falling Block', 1, 0, 0, [11, 12], MoveObject((900, -100), (900, 2000), 0.65, 10, False, 400))

cube12_1 = Objects(-500, 530, 250, 300, 'floor', 1, 0, 0, [12], "Collider")
cube12_2 = Objects(285, 480, 320, 380, 'floor', 1, 0, 0, [12], "Collider")
cube12_3 = Objects(-50, 360, 150, 500, 'pillar', 1, 0, 0, [12], "Collider")
cube12_4 = Objects(910, 380, 500, 400, 'floor', 1, 0, 0, [12], "Collider")

cube13_1 = Objects(-500, 385, 500, 400, 'floor', 1, 0, 0, [13], "Collider")
cube13_2 = Objects(222, 450, 130, 30, 'floating', 1, 0, 0, [13], "Collider")
cube13_3 = Objects(555, 360, 130, 30, 'floating', 1, 0, 0, [13], "Collider")
cube13_4 = Objects(888, 540, 130, 30, 'floating', 1, 0, 0, [13], "Collider")
cube13_5 = Objects(1165, 0, 250, 350, 'wall', 1, 0, 0, [13], "Collider")
cube13_6 = Objects(1165, 650,250 , 500, 'floor', 1, 0, 0, [13], "Collider")

cube13_7 = Objects(227, 1000, 120, 120, 'Falling Block', 1, 0, 0, [13], MoveObject((227, -100), (227, 2500), 0.7, 10, False, 0))
cube13_8 = Objects(888, 0, 120, 120, 'Falling Block', 1, 0, 0, [13], MoveObject((888, -100), (888, 2500), 0.7, 10, False, 0))
cube13_9 = Objects(555, 500, 120, 120, 'Falling Block', 1, 0, 0, [13], MoveObject((555, -100), (555, 2500), 0.7, 10, False, 0))

cube14_15_1 = Objects(-500, 650, 2000, 500, 'floor', 1, 0, 0, [14,15], "Collider")
cube14_2 = Objects(-235, 225, 2000, 150, 'floor', 1, 0, 0, [14], "Collider")
cube14_3 = Objects(-500, 0, 300, 375, 'wall', 1, 0, 0, [14], "Collider")
cube14_4 = Objects(1100, 0, 300, 375, 'wall', 1, 0, 0, [14], "Collider")
cube14_Enemy1 = Objects(69, cube14_15_1.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [14], enemyWillem_Henk_1)
cube14_Enemy2 = Objects(880, cube14_15_1.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [14], enemyBoze_Jantje_1)

cube14_5 = Objects(400, -500, 50, 50, 'Falling Block', 1, 0, 0, [14], MoveObject((400, -100), (400, 190), 4, 10, False, 500))
cube14_6 = Objects(400, -500, 50, 50, 'Falling Block', 1, 0, 0, [14], MoveObject((400, -100), (400, 190), 4.5, 10, False, 500))
cube14_7 = Objects(400, -500, 50, 50, 'Falling Block', 1, 0, 0, [14], MoveObject((400, -100), (400, 190), 5.5, 10, False, 500))

cube15_1 = Objects(-500, 0, 300, 400, 'wall', 1, 0, 0, [15], "Collider")
cube15_7 = Objects(-200, 0, 115, 160, 'wall', 1, 0, 0, [15], "Collider")
cube15_6 = Objects(-200, 280, 170, 120, 'floating', 1, 0, 0, [15], "Collider")
cube15_5 = Objects(210, 330, 175, 40, 'floating', 1, 0, 0, [15], "Collider")
cube15_8 = Objects(615, 90, 175, 40, 'floating', 1, 0, 0, [15], "Collider")
cube15_4 = Objects(640, 410, 175, 40, 'floating', 1, 0, 0, [15], "Collider")
cube15_3 = Objects(1100, 100, 270, 385, 'floor', 1, 0, 0, [15], "Collider")
cube15_2 = Objects(1200, 485, 270, 300, 'wall', 1, 0, 0, [15], "Collider")

cube15_9 = Objects(0, -400, 300, 300, 'Falling Block', 1, 0, 0, [15], MoveObject((0, -400), (0, 2500), 0.5, 10, False, 0))
cube15_10 = Objects(350, -400, 300, 300, 'Falling Block', 1, 0, 0, [15], MoveObject((350, -400), (350, 2500), 0.5, 10, False, 0))
cube15_11 = Objects(700, -400, 300, 300, 'Falling Block', 1, 0, 0, [15], MoveObject((700, -400), (700, 2500), 0.5, 10, False, 0))

cube16_1 = Objects(-500, 100, 270, 770, 'floor', 1, 0, 0, [16], "Collider")
cube16_2 = Objects(-230, 330, 730, 500, 'floor', 1, 0, 0, [16], "Collider")
cube16_3 = Objects(500, 530, 1000, 500, 'floor', 1, 0, 0, [16], "Collider")
cube16_4 = Objects(300, 0, 1200, 75, 'wall', 1, 0, 0, [16], "Collider")
cube16_Enemy1 = Objects(950, cube16_3.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [16], enemyKwaardaardige_BOB_1)

cube18_1 = Objects(-500, 600, 2000, 300, 'floor', 1, 0, 0, [18], "Collider")
cube18_2 = Objects(-40, 430, 230,350, 'pillar', 1, 0, 0, [18], "Collider")
cube18_3 = Objects(400, 280, 200, 600, 'pillar', 1, 0, 0, [18], "Collider")
cube18_4 = Objects(780, 380, 217, 500, 'pillar', 1, 0, 0, [18], "Collider")
cube18_5 = Objects(1200, 140, 170, 650, 'floor', 1, 0, 0, [18], "Collider")

cube19_20_1 = Objects(-500, 600, 630, 200, 'floor', 1, 0, 0, [19, 20], "Collider")
cube19_2 = Objects(-500, 0, 414, 380, 'wall', 1, 0, 0, [19], "Collider")
cube19_4 = Objects(-106, 0, 651, 184, 'wall', 1, 0, 0, [19], "Collider")
cube19_3 = Objects(130, 400, 264, 400, 'pillar', 1, 0, 0, [19], "Collider")
cube19_5 = Objects(394, 520, 440, 268, 'floor', 1, 0, 0, [19], "Collider")
cube19_6 = Objects(533, 0, 192, 407, 'wall', 1, 0, 0, [19], "Collider")
cube19_7 = Objects(725, 0, 700, 150, 'wall', 1, 0, 0, [19], "Collider")
cube19_8 = Objects(834, 300, 600, 364, 'floor', 1, 0, 0, [19], "Collider")

cube20_1 = Objects(-500, 0, 575, 450, 'wall', 1, 0, 0, [20], "Collider")
cube20_2 = Objects(75, 0, 1500, 100, 'wall', 1, 0, 0, [20], "Collider")
cube20_3 = Objects(272, 400, 1200, 400, 'floor', 1, 0, 0, [20], "Collider")
cube20_Enemy1 = Objects(519, cube20_3.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [20], enemyBoudewijn_1)
cube20_Enemy2 = Objects(750, cube20_3.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [20], enemyRoderick_1)

cube21_22_23_1 = Objects(-500, 600, 486, 268, 'floor', 1, 0, 0, [21, 22, 23, 25, 26], "Collider")
cube21_2 = Objects(-500, 0, 297, 329, 'wall', 1, 0, 0, [21], "Collider")
cube21_3 = Objects(-232, 0, 1600, 90, 'wall', 1, 0, 0, [21], "Collider")
cube21_4 = Objects(270, 470, 100, 445, 'pillar', 1, 0, 0, [21], "Collider")
cube21_5 = Objects(650, 390, 100, 445, 'pillar', 1, 0, 0, [21], "Collider")
cube21_6 = Objects(1020, 450, 100, 445, 'pillar', 1, 0, 0, [21], "Collider")
cube21_7 = Objects(1241, 244, 200, 523,'floor', 1, 0, 0, [21], "Collider")

cube22_1 = Objects(-500, 0, 392, 415,'wall', 1, 0, 0, [22], "Collider")
cube22_2 = Objects(263, 406, 469, 361,'floor', 1, 0, 0, [22], "Collider")
cube22_3 = Objects(920, 406, 100, 500,'pillar', 1, 0, 0, [22], "Collider")
cube22_4 = Objects(1200, 406, 300, 500,'floor', 1, 0, 0, [22], "Collider")
cube22_5 = Objects(263, 0, 1500, 300,'wall', 1, 0, 0, [22], "Collider")
cube22_6 = Objects(-170, 0, 488, 117,'wall', 1, 0, 0, [22], "Collider")

cube23_1 = Objects(-500, 0, 3000, 400,'wall', 1, 0, 0, [23], "Collider")
cube23_2 = Objects(224, 659, 400, 300,'floor', 1, 0, 0, [23], "Collider")
cube23_3 = Objects(870, 700, 500, 300,'pillar', 1, 0, 0, [23], "Collider")
cube23_4 = Objects(400, 400, 1000, 65,'wall', 1, 0, 0, [23], "Collider")
cube23_Enemy1 = Objects(493, cube23_2.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [23], enemyKleine_Karel_1)
cube23_Enemy2 = Objects(1128, cube23_3.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [23], enemyIni_Mini_1)

cube24_1 = Objects(-500, 700, 500, 80,'pillar', 1, 0, 0, [24], "Collider")
cube24_2 = Objects(-500, 0, 218, 491,'wall', 1, 0, 0, [24], "Collider")
cube24_3 = Objects(-303, 0, 1700, 70,'wall', 1, 0, 0, [24], "Collider")
cube24_4 = Objects(114, 617, 150, 20,'floating', 1, 0, 0, [24], "Collider")
cube24_5 = Objects(750, 500, 150, 20,'floating', 1, 0, 0, [24], "Collider")
cube24_6 = Objects(410, 450, 150, 20,'floating', 1, 0, 0, [24], "Collider")
cube24_7 = Objects(1000, 330, 150, 20,'floating', 1, 0, 0, [24], "Collider")

cube24_8 = Objects(114, -400, 150, 150,'Falling Block', 1, 0, 0, [24],  MoveObject((114, -400), (114, 2500), 0.7, 10, False, 0))
cube24_9 = Objects(750, -400, 150, 150,'Falling Block', 1, 0, 0, [24],  MoveObject((750, -400), (750, 2500), 0.7, 10, False, 0))
cube24_10 = Objects(410, 1000, 150, 150,'Falling Block', 1, 0, 0, [24],  MoveObject((410, -400), (410, 2500), 0.7, 10, False, 0))
cube24_11 = Objects(1000, 1000, 150, 150,'Falling Block', 1, 0, 0, [24],  MoveObject((1000, -400), (1000, 2500), 0.7, 10, False, 0))

cube24_12 = Objects(1238, 244, 127, 523,'floor', 1, 0, 0, [24], "Collider")

cube25_1 = Objects(238, 442, 569, 49,'floating', 1, 0, 0, [25], "Collider")
cube25_2 = Objects(-500, 0, 1900, 136,'wall', 1, 0, 0, [25], "Collider")
cube25_3 = Objects(1141, 296, 300, 500,'floor', 1, 0, 0, [25], "Collider")

cube25_4 = Objects(500, 0, 150, 150,'Falling Block', 1, 0, 0, [25],  MoveObject((500, -400), (500, 1200), 0.6, 10, False, 200))
cube25_5 = Objects(400, -400, 150, 150,'Falling Block', 1, 0, 0, [25],  MoveObject((500, -400), (500, 1200), 0.6, 10, False, 200))
cube25_6 = Objects(600, -800, 150, 150,'Falling Block', 1, 0, 0, [25],  MoveObject((500, -400), (500, 1200), 0.6, 10, False, 200))

cube26_1 = Objects(-14, 500, 614, 367,'floor', 1, 0, 0, [26], "Collider")
cube26_2 = Objects(600, 420, 260, 447,'floor', 1, 0, 0, [26], "Collider")
cube26_3 = Objects(860, 452, 605, 415,'water', 1, 0, 0, [26], "Collider")
cube26_4 = Objects(840, 390, 605, 415, 'lifeboat', 1, 0, 0, [26], "NonCollider")
cube26_5 = Objects(940, 430, 10, 20, None, 1, 0, 0, [26], "Collider")
cube26_Enemy1 = Objects(701, cube26_2.ypos - enemy_paste_height, 100, enemy_paste_height, 'orange', 1, 0, 0, [26], enemyBOSS_1)

cube_RisingWater = Objects(-500, 800, 2000, 750, 'water', 1, 0, 0, [18, 19, 21, 22, 24, 25], MoveObject((800, 1000), (800, 0), 0.1, 10, False, 0))
enemyList = [cube1_Enemy1, cube3_Enemy1, cube4_Enemy1, cube6_Enemy1, cube9_Enemy1, cube10_Enemy1, cube14_Enemy1, cube14_Enemy2, cube16_Enemy1, cube20_Enemy1, cube20_Enemy2, cube23_Enemy1, cube23_Enemy2, cube26_Enemy1]

# Add here the new platforms that require collision.
platforms = [cube_LeftBorder,
             cube1_2, cube1_1, cube1_3, cube1_4, cube1_Enemy1,
             cube2_1, cube2_1, cube2_2, cube2_3, cube2_4, cube2_5,
             cube3_1, cube3_2, cube3_3, cube3_4, cube3_5, cube3_Enemy1,
             cube4_1, cube4_2, cube4_3, cube4_4, cube4_5, cube4_6, cube4_7, cube4_Enemy1,
             cube5_1, cube5_2, cube5_3, cube5_4, cube5_5,
             cube6_1, cube6_2, cube6_3, cube6_Enemy1,
             cube7_1, cube7_2, cube7_3, cube7_4,
             cube9_1, cube9_2, cube9_3, cube9_4, cube9_5, cube9_6, cube9_7, cube9_8, cube9_Enemy1,
             cube10_1, cube10_2, cube10_3, cube10_4, cube10_5, cube10_6, cube10_7, cube10_Enemy1,
             cube11_1, cube11_2, cube11_3, cube11_4,
             cube11_12_1, cube11_12_2, cube11_12_3, cube11_12_4, cube11_12_5, cube11_12_6, cube11_12_7, cube11_12_8, cube11_12_9,
             cube12_1, cube12_2, cube12_3, cube12_4,
             cube13_1, cube13_2, cube13_3, cube13_4, cube13_5, cube13_6, cube13_7, cube13_8, cube13_9,
             cube14_15_1, cube14_2, cube14_3,cube14_4, cube14_5, cube14_6, cube14_7, cube14_Enemy1, cube14_Enemy2,
             cube15_1, cube15_2, cube15_3, cube15_4, cube15_5, cube15_6, cube15_7, cube15_8, cube15_9, cube15_10, cube15_11,
             cube16_1, cube16_2, cube16_3, cube16_4, cube16_Enemy1,
             cube18_1, cube18_2, cube18_3, cube18_4, cube18_5,
             cube19_20_1, cube19_2, cube19_3, cube19_4, cube19_5, cube19_6, cube19_7, cube19_8,
             cube20_1, cube20_2, cube20_3, cube20_Enemy1, cube20_Enemy2,
             cube21_22_23_1, cube21_2, cube21_3, cube21_4, cube21_5, cube21_6, cube21_7,
             cube22_1, cube22_2,cube22_3, cube22_4, cube22_5, #cube22_6,
             cube23_1, cube23_2, cube23_3, cube23_4, cube23_Enemy1, cube23_Enemy2,
             cube24_1, cube24_2, cube24_3, cube24_4, cube24_5, cube24_6, cube24_7, cube24_8, cube24_9, cube24_10, cube24_11, cube24_12,
             cube25_1, cube25_2, cube25_3, cube25_4, cube25_5, cube25_6,
             cube26_1, cube26_3, cube26_4, cube26_2, cube26_5, cube26_Enemy1,
             cube_RisingWater]

# All the RespawnPos in a list.
RespawnPos_list = [(270, 450), (-350, 350), (-300, 450), (-330, 50), (-380, 385), (-340, 350), (-340, 350), (0, 0),
                   (-340, 350), (-340, 150), (-320, 400), (-340, 400), (-340, 400), (-300, 530), (-440, 600), (-440, 600), (0, 0),
                   (-440, 500), (-300, 480), (-300, 480), (-300, 480), (-300, 480), (-300, 480), (-300, 600), (-300, 600), (-300, 600), (0, 0)]

# Other contstants
clock = pygame.time.Clock()
fps = 60
jump_height = -25
speed = 11

def parkour(player, game_manager):
    """
    The entire code of the platforming part of the game.
    :param game_manager:
    :param player: The active player
    :return: the new state or the enemy that is encountered
    """
    looking = "Right"
    tick = 0
    running = True
    scene = game_manager.scene
    level = game_manager.level
    RespawnPos = RespawnPos_list[scene - 1]

    CameraPosx = -500
    playerObject.xpos = game_manager.Player_posx + 20
    playerObject.ypos = game_manager.Player_posy
    pos1 = (0, 0)
    CollisionGlitch = True
    TransitionGlitch = 0
    InvincibilityFrames = 5
    # Music
    pygame.mixer.stop()
    pygame.mixer.music.load("resources/sound/parjour song.wav")
    pygame.mixer.music.play(-1)
    PlayerPos2 = (playerObject.xpos, playerObject.ypos)
    PlayerPos1 = PlayerPos2

    # Allows for constant movement
    keys = {"left": False, "right": False, "up": False}

    L_border = 0
    R_border = 500

    # game loop
    while running:
        if TransitionGlitch > 0:
            playerObject.xpos, playerObject.ypos = RespawnPos
            CollisionGlitch = False

        mouse = pygame.mouse.get_pos()
        clock.tick(fps)

        # Draws the background, scene 26 has a different background.
        if not scene == 26:
            screen.blit(image_background, (-CameraPosx - 500, 0))
        else:
            screen.blit(image_landscape, (-CameraPosx - 500, 0))
            screen.blit(image_landscape_mirror, (-CameraPosx + 866, 0))

        Colliders = playerObject.update_pos(platforms, CameraPosx, scene)

        #Collision glitch fix
        if CollisionGlitch:
            if Afstand(PlayerPos1, PlayerPos2) < 50 or Afstand(PlayerPos1, PlayerPos2) > 500 :
                PlayerPos1 = PlayerPos2
            else:
                (playerObject.xpos, playerObject.ypos) = PlayerPos1
            PlayerPos2 = (playerObject.xpos, playerObject.ypos)
        else:
            PlayerPos2 = (playerObject.xpos, playerObject.ypos)
            PlayerPos1 = PlayerPos2
            CollisionGlitch = True

        # Makes the animation for the texture of the player
        if playerObject.yspeed != 0 and playerObject.xspeed < 0:
            playerObject.texture_type = player_Jump_Left
        elif playerObject.yspeed != 0 and playerObject.xspeed > 0:
            playerObject.texture_type = player_Jump_Right
        elif playerObject.on_ground == True and playerObject.xspeed == 0 and looking == 'Left':
            playerObject.texture_type = player_idle_Left
        elif playerObject.on_ground == True and playerObject.xspeed == 0 and looking == 'Right':
            playerObject.texture_type = player_idle
        elif playerObject.xspeed < 0:
            looking = 'Left'
            if tick < 8:
                playerObject.texture_type = player_Left
            else:
                playerObject.texture_type = player_idle_Left
        elif playerObject.xspeed > 0:
            looking = "Right"
            if tick < 10:
                playerObject.texture_type = player_Right
            else:
                playerObject.texture_type = player_idle


        # Draws all the objects that are stationary.
        for platform in platforms:
            if scene in platform.ObjectScene and not type(platform.Type) == MoveObject:
                platform.draw(screen, CameraPosx)
                if type(platform.Type) == character:
                    if not platform.Type.alive:
                        platforms.remove(platform)

        # Draws the player (the rat).
        playerObject.draw(screen, CameraPosx)

        # Draws the extended 3D part on the right side of the platforms above the player.
        for platform in platforms:
            if scene in platform.ObjectScene:
                platform.draw_3D_extension(screen, CameraPosx)
        # Draws the moving objects like falling debris and water.
        for platform in platforms:
            if scene in platform.ObjectScene and type(platform.Type) == MoveObject:
                platform.draw(screen, CameraPosx)
                platform.xpos, platform.ypos = platform.Type.Move((int(platform.xpos), int(platform.ypos)), platform.Type.Speed)

        # Draws the info of the player (upper corners).
        player.displayInfo(level, scene)

        # Special scenes
        if scene == 8:
            LevelComplete()
            scene += 1
            level += 1
            player.maxHitpoints = 120
            player.hitpoints = player.maxHitpoints
            player.heals = 5

        elif scene == 17:
            LevelComplete()
            scene += 1
            level += 1
            player.maxHitpoints = 150
            player.hitpoints = player.maxHitpoints
            player.heals = 8
            cube_RisingWater.ypos = 850

        elif scene == 27:
            end(player.name)
            return "Menu"



        playerObject.xspeed = speed * (keys["right"] - keys["left"])

        # Makes the player die
        for Collider in Colliders:
            if (playerObject.ypos >= HEIGHT - playerObject.height - 10 or Collider == "Death" or type(Collider) == MoveObject) and InvincibilityFrames == 0:

                playerObject.xpos = RespawnPos[0]
                playerObject.ypos = RespawnPos[1]
                if player.hitpoints <= 30:
                    player.lives, state, dead = game_over(player.lives)
                    player.hitpoints = player.maxHitpoints
                else:
                    player.hitpoints, state, dead = got_hurt(player.hitpoints)
                CollisionGlitch = False
                InvincibilityFrames += 50
                TransitionGlitch = 5
                if dead:
                    return "dead"

                cube_RisingWater.ypos = 800
                if state is not None:
                    return state

            #returns enemy waarmee je collide
            if type(Collider) == character:
                if Collider.alive == True and InvincibilityFrames == 0:
                    return Collider
        #print(InvincibilityFrames)


        # Changes camera position
        if L_border <= playerObject.xpos <= R_border:
            CameraPosx = playerObject.xpos - 500
        elif L_border >= playerObject.xpos:
            CameraPosx = L_border - 500
        elif playerObject.xpos >= R_border:
            CameraPosx = R_border - 500
        # Right scene transition
        if playerObject.xpos > R_border + 800:
            TransitionGlitch = 5
            playerObject.xpos = -450
            playerObject.ypos -= 30
            CameraPosx = L_border - 500
            scene += 1
            RespawnPos = RespawnPos_list[scene - 1]
            cube_RisingWater.ypos = 800
            keys = {"left": False, "right": False, "up": False}
            CollisionGlitch = False
            InvincibilityFrames = 25
            if scene in [19, 20, 22, 23, 25, 26]:
                playerObject.ypos = 500

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                if pos1 == (0, 0):
                    pos1 = (mouse[0] + CameraPosx, mouse[1])
                else:
                    print(pos1[0], pos1[1], mouse[0] + CameraPosx - pos1[0], mouse[1] - pos1[1])
                    pos1 = (0, 0)

            # Key press detection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keys["right"] = True
                elif event.key == pygame.K_a:
                    keys["left"] = True
                elif event.key == pygame.K_w:
                    keys["up"] = True

                elif event.key == pygame.K_ESCAPE:
                    if Pause() == "Menu":
                        return "Menu"
                    else:
                        keys = {"left": False, "right": False, "up": False}
            # Deactivating the pressed keys
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keys["right"] = False
                elif event.key == pygame.K_a:
                    keys["left"] = False
                elif event.key == pygame.K_w:
                    keys["up"] = False

        # Jump
        if keys["up"] == True and playerObject.on_ground:
            playerObject.yspeed = jump_height

        pygame.display.flip()

        if InvincibilityFrames > 0:
            InvincibilityFrames -= 1
        if TransitionGlitch > 0:
            TransitionGlitch -= 1
        if tick < 16:
            tick += 1
        else:
            tick = 0

        game_manager.Set(level, scene, playerObject.xpos, playerObject.ypos)
    return None
