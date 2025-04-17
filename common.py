from button_code import *
from firework_function import *
import pygame
import time
gravity = 0.6
tick = 0
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()

#Textures
image_background = pygame.transform.scale(pygame.image.load('resources/textures/background_ceilingWallV1.png').convert(), (2560, 1125))
image_floor = pygame.transform.scale(pygame.image.load('resources/textures/background_floor.png').convert(), (2525, 810))
image_floor3D = pygame.transform.scale(pygame.image.load('resources/textures/background_floorV3.png').convert(), (2560, 810))
image_floor3D_right = pygame.transform.scale(pygame.image.load('resources/textures/background_floor_right3D.png'), (70, 810))
image_floor3D_right_2 = pygame.transform.scale(pygame.image.load('resources/textures/background_floor_right3D_2.png'), (70, 30))
image_pillar = pygame.transform.scale(pygame.image.load('resources/textures/background_pillar.png').convert(), (2560, 810))
image_pillar_right = pygame.transform.scale(pygame.image.load('resources/textures/background_pillar_right3D.png'), (70, 810))
image_floating = pygame.transform.scale(pygame.image.load('resources/textures/background_floating.png').convert(), (1600, 175))
image_floating_right = pygame.transform.scale(pygame.image.load('resources/textures/background_floating_right3D.png'), (70, 175))
image_floating_ridge = pygame.transform.scale(pygame.image.load('resources/textures/background_floating_ridge.png'), (1600, 10))
image_wall = pygame.image.load('resources/textures/background_wall.png').convert()
image_fallingBlock1 = pygame.image.load('resources/textures/Falling_Debris1.png')
image_fallingBlock2 = pygame.image.load('resources/textures/Falling_Debris2.png')
image_lifeboat = pygame.transform.scale(pygame.image.load('resources/textures/Lifeboat.png'), (605, 415))
texture_y_overlap = 30

class Objects:
    def __init__(self, xpos, ypos, width, height, texture_type, mass, xspeed, yspeed, ObjectScene, Type):
        """
        Create an object
        :param xpos: the x position - int
        :param ypos: the y position - int
        :param width: the width of the object - int
        :param height: the height of the object - int
        :param texture_type: the texture type that needs to render - string
        :param mass: change how fast the player falls - float
        :param xspeed: the speed in x direction - int
        :param yspeed: the speed in y direction - int
        :param ObjectScene: the scene the object appeares in - int
        :param Type: The type of block - string or object type
        :return: None
        """

        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.texture_type = texture_type
        self.mass = mass
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.Rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.on_ground = False
        self.ObjectScene = ObjectScene
        self.Type = Type
        self.surface = None

        if self.texture_type == "floor3D" or self.texture_type == "floor":
            self.surface = pygame.Surface((self.width, self.height + texture_y_overlap))
            self.surface.blit(image_floor3D, (0, 0))
        elif self.texture_type == "pillar":
            self.surface = pygame.Surface((self.width, self.height + texture_y_overlap))
            self.surface.blit(image_pillar, (0, 0))
        elif self.texture_type == "floating":
            self.surface = pygame.Surface((self.width, self.height + texture_y_overlap))
            self.surface.blit(image_floating, (0, 0))
            self.surface.blit(image_floating_ridge, (0, self.height + texture_y_overlap - 10))
        elif texture_type == "wall":
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.blit(pygame.transform.scale(image_wall, (self.width, self.height)), (0, 0))
        elif texture_type == "water":
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.blit(pygame.transform.scale(pygame.image.load('resources/textures/water.png').convert(), (self.width, self.height)))
            self.surface.set_alpha(200)
        elif texture_type == "Falling Block":
            if random.randint(0, 1) == 1:
                self.texture_type = pygame.transform.scale(image_fallingBlock1, (self.width, self.height))
            else:
                self.texture_type = pygame.transform.scale(image_fallingBlock2, (self.width, self.height))
        elif not (self.texture_type == 'red' or self.texture_type == 'blue' or self.texture_type == "lifeboat" or type(self.texture_type) == pygame.Surface):
            self.texture_type = (180, 80, 0)

    def update_pos(self, platforms, CameraPosx, scene):
        """
        updates the position of all objects based on the camera position
        :param platforms: a list of all the platforms - list[platforms]
        :param CamerPosx: the position of the camera - int
        :param scene: the current scene. - int
        :return: The object the player collided with - object
        """
        Collider = []
        self.xpos += self.xspeed
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)

        for platform in platforms:
            if scene in platform.ObjectScene:
                if self.Rect.colliderect(platform.Rect) and platform.Type != "NonCollider":
                    if self.xspeed > 0:
                        self.xpos = platform.xpos - self.width
                    elif self.xspeed < 0:
                        self.xpos = platform.xpos + platform.width
                    self.xspeed = 0
                    self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
                    Collider.append(platform.Type)

        self.yspeed += self.mass * gravity

        self.ypos += self.yspeed
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
        self.on_ground = False

        # platformcollision
        for platform in platforms:
            if scene in platform.ObjectScene:
                if self.Rect.colliderect(platform.Rect) and platform.Type != "NonCollider":
                    if self.yspeed > 0:  # Falling
                        self.ypos = platform.ypos - self.height
                        self.yspeed = 0
                        self.on_ground = True
                    elif self.yspeed < 0:  # Hitting ceiling
                        self.ypos = platform.ypos + platform.height
                        self.yspeed = 0
                    self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
                    Collider.append(platform.Type)



        # wall en floor collision
        if self.ypos + self.height >= HEIGHT - 4:
            self.ypos = HEIGHT - self.height - 4
            self.yspeed = 0
            self.on_ground = True
            self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
            Collider.append(platform.Type)
        return Collider

    def draw(self, screen, CameraPosx):
        """
        draws the scene
        :param CamerPosx: the position of the camera - int
        :param screen: the screen everything gets drawn on - int
        :return: None
        """
        if type(self.texture_type) == pygame.Surface: #player, wall
            self.Rect = screen.blit(self.texture_type, (self.xpos - CameraPosx, self.ypos))
        elif type(self.Type) == character: #enemies
            self.Rect = screen.blit(self.Type.image, (self.xpos - CameraPosx, self.ypos))
        elif self.surface is not None: #platforms
            if self.texture_type == "wall" or self.texture_type == "water":
                screen.blit(self.surface, (self.xpos - CameraPosx, self.ypos))
            else:
                screen.blit(self.surface, (self.xpos - CameraPosx,  self.ypos - texture_y_overlap))
                screen.blit(image_floor3D_right_2, (self.xpos - CameraPosx + self.width - 30, self.ypos - texture_y_overlap))
            self.Rect = (self.xpos - CameraPosx, self.ypos, self.width, self.height)
        elif self.texture_type != "lifeboat": #platforms with no texture
            self.Rect = pygame.draw.rect(screen, self.texture_type,(self.xpos - CameraPosx, self.ypos, self.width, self.height))

    def draw_3D_extension(self, screen, CameraPosx):
        """
        Gives all objects a texture
        :param CamerPosx: the position of the camera - int
        :param screen: The scene everything gets drawn. - int
        :return: The object the player collided with - object
        """
        if self.texture_type == "floor" or self.texture_type == "floor3D":
            screen.blit(image_floor3D_right, (self.xpos - CameraPosx + self.width - 30, self.ypos - texture_y_overlap))
        elif self.texture_type == "pillar":
            screen.blit(image_pillar_right, (self.xpos - CameraPosx + self.width - 30, self.ypos - texture_y_overlap))
        elif self.texture_type == "floating":
            surface = pygame.Surface((self.width + 40, self.height + texture_y_overlap - 10)).convert_alpha()
            surface.fill((0, 0, 0, 0))
            surface.blit(image_floating_right, (self.width - 30, 0))
            screen.blit(surface, (self.xpos - CameraPosx, self.ypos - texture_y_overlap))
        elif self.texture_type == "lifeboat":
            screen.blit(image_lifeboat, (self.xpos - CameraPosx, self.ypos))


class character:

    def __init__(self, name, lives, image, hitpoints, maxHitpoints, moveset, items, heals, alive, NewMove):
        """
        updates the position of all objects based on the camera position
        :param name:The name of the character - string
        :param lives: The amount of lives of the character - int
        :param image: The image that gets drawn at the place of the character - image
        :param hitpoints: The amount of hitpoints of the character - int
        :param maxHitpoints: The maximum hitpoints a character can have - int
        :param moveset: The moveset of the character - list[strings]
        :param items: The items the character has - list[strings]
        :param heals: The amount of times this character can heal - int
        :param alive: Wether the character is alive - bool
        :param newMove: Wehter you get a new move after defeating this enemy - bool
        :return: None
        """
        self.name = name
        self.lives = lives
        self.image = image
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.moveset = moveset
        self.items = items
        self.heals = heals
        self.alive = alive
        self.NewMove = NewMove


    def displayInfo(self):
        """
        Displays the info of the character on screen. Info consist of name, hitpoints and lives.
        :return Nothing
        """
        pygame.draw.rect(screen, 'black', pygame.Rect(20, 65, 210, 60))
        pygame.draw.rect(screen, 'red', pygame.Rect(25, 70, 200 * (self.hitpoints / self.maxHitpoints), 50))

        lifeImage = pygame.transform.scale(pygame.image.load("resources/textures/life.png"), (38,38))
        nolifeImage = pygame.transform.scale(pygame.image.load("resources/textures/life_empty.png"), (38, 38))
        for i in range(5):
            if self.lives >= i + 1:
                screen.blit(lifeImage, (20 + 43 * i, 140))
            else:
                screen.blit(nolifeImage, (20 + 43 * i, 140))

        textPrint(str(self.hitpoints), 40, 'white', (125, 95))
        textPrint(self.name, 40, 'black', (125, 45), outline=('white', 2))


class Game_Manager:
    def __init__(self, scene, Player_posx, Player_posy):
        """
        Makes the game manager that stores important variables
        :param scene: the current scene - int
        :param Player_posx: The current x position of the player - int
        :param Player_posy: The current y position of the player - int

        :return the pressed button (Start, Quit)
        """
        self.scene = scene
        self.Player_posx = Player_posx
        self.Player_posy = Player_posy
    def Set(self, scene, Player_posx, Player_posy):
        """
        changes the Game manager
        :param scene: the scene it get changed to- int
        :param Player_posx: the x position it get changed to - int
        :param Player_posy: the y position it get changed to - int
        :return None
        """
        self.scene = scene
        self.Player_posx = Player_posx
        self.Player_posy = Player_posy
    def Reset(self):
        """
        Resets the game manager to its start phase
        :return None
        """
        self.Set(1, -130, 450)


game_manager = Game_Manager(1, -90, 450)

def menu(name):
    """
    Shows the menu screen
    :return the pressed button (Start, Quit)
    """
    screen.fill('black')
    screen.blit(image_background, (0, 0))
    screen.blit(image_floor, (0, 490))
    buttonPlaying = button(WIDTH / 2 - 100, HEIGHT / 2, 200, 80, 'grey', 'darkgrey', "start", 'white', 50, 'white')
    buttonQuit = button(WIDTH / 2 - 100, HEIGHT / 2 + 125, 200, 80, 'grey', 'darkgrey', "quit", 'white', 50,'white')
    buttonName = button(WIDTH / 5 - 80, HEIGHT / 2 + 40, 160, 60, 'black', (40, 40, 40), "Change name", 'white', 20, 'black')
    textPrint("Titanic: Escape", 100, 'white', (WIDTH / 2, HEIGHT // 4), outline=('black', 7))

    textPrint(name, 40, 'white', (WIDTH / 5, HEIGHT / 2), outline=('black', 2))
    index, name = waitForInput([buttonPlaying, buttonQuit], typeInfo=(buttonName, name, (WIDTH // 5, HEIGHT // 2), 40, ('black', 2)))
    possibleStates = ["Playing", "quit"]
    return possibleStates[index], name



def Pause():
    """
    Pauses the game until the player selects an option
    :return the state the player should now be in
    """
    buttonResume = button(WIDTH / 2 - 100, HEIGHT / 2, 200, 80, 'grey', 'darkgrey', "resume", 'white', 50,'white')
    buttonMenu = button(WIDTH / 2 - 100, HEIGHT / 2 + 125, 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,'white')
    dimSurface = pygame.Surface((WIDTH, HEIGHT))
    pygame.Surface.set_alpha(dimSurface, 100)
    pygame.Surface.blit(screen, dimSurface)
    textPrint("Pause", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))

    index = waitForInput([buttonResume, buttonMenu], True)
    possibleStates = [None, "Menu", None]
    return possibleStates[index]

def got_hurt(hitpoints, state=None):
    """
    Shows the Got hurt screen
    :param hitpoints: the amount of hitpoints left of the player
    :param state : The state of the game
    :return: hitpoints, state
    """
    def draw_screen(y):
        screen.fill('brown')
        screen.blit(headText, headTextPos)
        screen.blit(subText, subTextPos)
        screen.blit(rat_texture, (100, y))
        pygame.draw.rect(screen, (255, 255, 255), (150, y - 80, 10, 70))
        pygame.draw.rect(screen, (255, 255, 255), (205, y - 110, 10, 100))
        pygame.draw.rect(screen, (255, 255, 255), (260, y - 80, 10, 70))
        pygame.display.update()

    hitpoints -= 30
    headFont = pygame.font.Font(mainFont, 100)
    subFont = pygame.font.Font(mainFont, 40)
    headText = headFont.render("You got hurt", True, (255, 255, 255))
    subText = subFont.render("You have " + str(hitpoints) + " hitpoints left", True, (255, 255, 255))
    headTextRect = headText.get_rect()
    headTextRect.center = (WIDTH / 2, HEIGHT / 2 - 100)
    headTextPos = headTextRect.topleft
    subTextRect = subText.get_rect()
    subTextRect.center = (WIDTH / 2, HEIGHT / 2)
    subTextPos = subTextRect.topleft
    rat_texture = pygame.transform.flip(pygame.transform.scale(pygame.image.load("resources/textures/rat_idle.png"), (200, 80)), False, True)
    y = -50
    for i in range(0, screen.get_height() // 2 + 100):
        beginTime = time.time()
        draw_screen(y)
        y += 2
        waitTime = 0.005 - (time.time() - beginTime)
        if waitTime > 0:
            time.sleep(waitTime)
    return hitpoints, state, False


def game_over(lives, state=None):
    """
    Shows the Game Over screen
    :param lives: the amount of lives left of the player
    :param state : The state of the game
    :return: lives, state
    """
    lives -= 1
    screen.fill('red')
    dead = False
    if lives == 0:
        textPrint("Game over", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
        textPrint("Play again?", 50, 'white', (WIDTH / 2, HEIGHT / 2))
        buttonYes = button(WIDTH / 2 - 150, HEIGHT / 2 + 50, 125, 75, 'grey', 'darkgrey', "YES", 'white', 40, 'white')
        buttonNo = button(WIDTH / 2 + 25, HEIGHT / 2 + 50, 125, 75, 'grey', 'darkgrey', "NO", 'white', 40, 'white')

        index = waitForInput([buttonYes, buttonNo])
        possibleStates = ["Playing", "Menu"]
        state = possibleStates[index]
        if index == 0:
            dead = True
        lives = 5
    else:
        textPrint("You died", 100, 'white', (WIDTH / 2, HEIGHT / 2))
        message = "You have " + str(lives) + " lives left"
        if lives == 1:
            message = message[:-8] + "fe left"
        textPrint(message, 40, 'white', (WIDTH / 2, HEIGHT / 2 + 100))
        pygame.display.flip()
        time.sleep(2)
    return lives, state, dead


def LevelComplete():
    """
    Shows the level complete screen and moves on to the next level
    :return none:
    """
    screen.fill((0, 0, 0))
    textPrint("Level Completed", 100, 'white', (WIDTH / 2, HEIGHT // 4))
    textPrint("all hitpoints have been restored", 80, 'white', (WIDTH / 2, HEIGHT // 4 + 300))
    pygame.display.update()
    time.sleep(3)


def eind(name):
    """
    Shows the credit screen and waits until the menu button is pressed.
    :return possibleStates[index]:
    """
    screen.fill('black')
    fireworkWord("Thanks for playing", 120)
    buttonMenu = button(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                        'white')
    textPrint(name, 100, 'white', (WIDTH / 2, HEIGHT / 2 - 220))
    textPrint("escaped the Titanic", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
    textPrint("Berend Sulman, Branko Opdam,", 40, 'white',
              (WIDTH / 2, HEIGHT / 2 - 20))
    textPrint("Maarten van Ammers & Stijn Zwart", 40, 'white',
              (WIDTH / 2, HEIGHT / 2 + 50))

    index = waitForInput([buttonMenu])
    possibleStates = ["Menu"]
    return possibleStates[index]


def Afstand(pos1, pos2):
    """
    caculates the distance between 2 points
    :param pos1: the first position - (int, int)
    :param pos2: the second position - (int, int)
    :return The distance between the points
    """
    x_afstand = pos2[0] - pos1[0]
    y_afstand = pos2[1] - pos1[1]
    if x_afstand < 0:
        x_afstand *= -1
    if y_afstand < 0:
        y_afstand *= -1

    return (x_afstand ** 2 + y_afstand ** 2) **0.5