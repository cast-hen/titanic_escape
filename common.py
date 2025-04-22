from button_code import *
from firework_function import *
import pygame
import time
import random

gravity = 0.6
tick = 0
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()

#Textures
image_landscape = pygame.transform.scale(pygame.image.load('resources/textures/nighty_landscape.jpg').convert(), (1366, 1558))
image_landscape_mirror = pygame.transform.flip(image_landscape, True, False)

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

lifeImage = pygame.transform.scale(pygame.image.load("resources/textures/life.png"), (38,38))
nolifeImage = pygame.transform.scale(pygame.image.load("resources/textures/life_empty.png"), (38, 38))


class MoveObject:
    def __init__(self, StartPos, EndPos, Speed, WaitTime, Teleport, Randomness):
        self.StartPos = StartPos
        self.EndPos = EndPos
        self.Speed = 100 / Speed
        self.WaitTime = WaitTime
        self.Teleport = Teleport
        self.Randomness = Randomness

        self.randomNumber = 0

        self.xDirection = self.EndPos[0] - self.StartPos[0]
        self.yDirection = self.EndPos[1] - self.StartPos[1]
        self.Direction = (self.xDirection / self.Speed, self.yDirection / self.Speed)

    def Move(self, pos, Speed):
        if self.randomNumber == 0:
            self.randomNumber = random.randint(-self.Randomness, self.Randomness)
        if pos == self.StartPos:
            xDirection = self.EndPos[0] - self.StartPos[0]
            yDirection = self.EndPos[1] - self.StartPos[1]
            self.Direction = (xDirection / Speed, yDirection / Speed)

        if 8 > (self.EndPos[0] - pos[0] + self.randomNumber) + (self.EndPos[1] - pos[1]) > -8 :
            if self.Teleport:
                endpos = self.EndPos
                self.EndPos = self.StartPos
                self.StartPos = endpos
                xDirection = self.EndPos[0] - self.StartPos[0]
                yDirection = self.EndPos[1] - self.StartPos[1]
                self.Direction = (xDirection / Speed, yDirection / Speed)
                self.randomNumber = 0

            else:
                self.randomNumber = random.randint(-self.Randomness, self.Randomness)
                pos = (self.StartPos[0]  + self.randomNumber, self.StartPos[1])

        TargetPos = pos[0] + self.Direction[0], pos[1] + self.Direction[1]
        return TargetPos



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
            if type(self.Type) == MoveObject:
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


    def displayInfo(self, campos):
        """
        Displays the info of the character on screen. Info consist of name, hitpoints and lives.
        :return Nothing
        """
        # Left section
        pygame.draw.rect(screen, 'black', pygame.Rect(20, 65, 210, 60))
        pygame.draw.rect(screen, 'red', pygame.Rect(25, 70, 200 * (self.hitpoints / self.maxHitpoints), 50))

        textPrint(screen,str(self.hitpoints), 40, 'white', (125, 95))
        textPrint(screen,self.name, 40, 'black', (125, 45), outline=('white', 2))

        # Drawing the lives of the player in hearts
        for i in range(5):
            if self.lives >= i + 1:
                screen.blit(lifeImage, (20 + 43 * i, 140))
            else:
                screen.blit(nolifeImage, (20 + 43 * i, 140))


        # Right section
        textPrint(screen,"Level " + str(game_manager.level), 20, 'black', (WIDTH - 125, 25), outline=('white', 1))
        pygame.draw.rect(screen, 'black', pygame.Rect(WIDTH - 20 - 204, 33, 204, 20))

        progress_current_scene = (game_manager.Player_posx + 500) / 1866
        finished_scenes = game_manager.scene - 1
        if game_manager.level == 2:
            finished_scenes -= 8
        elif game_manager.level == 3:
            finished_scenes -= 17
        number_of_scenes_in_level = [7, 8, 9]
        progress_level = (finished_scenes + progress_current_scene) / number_of_scenes_in_level[game_manager.level - 1]

        pygame.draw.rect(screen, 'green', pygame.Rect(WIDTH - 22 - 200, 35, 200 * progress_level, 16))




class Game_Manager:
    def __init__(self, level, scene, Player_posx, Player_posy, playTime):
        """
        Makes the game manager that stores important variables
        :param scene: the current scene - int
        :param Player_posx: The current x position of the player - int
        :param Player_posy: The current y position of the player - int
        """
        self.level = level
        self.scene = scene
        self.Player_posx = Player_posx
        self.Player_posy = Player_posy
        self.playTime = playTime
    def Set(self, level, scene, Player_posx, Player_posy):
        self.level = level
        self.scene = scene
        self.Player_posx = Player_posx
        self.Player_posy = Player_posy
    def Reset(self):
        self.__init__(1, 1, -130, 450, time.time())


game_manager = Game_Manager(1,1, -130, 450, time.time())


def tutorial():
    """
    Shows the tutorial for the player. Movement and enemy levels explained.
    :return: None
    """
    # Background
    screen.blit(image_landscape, (0, 0))
    # Titles
    textPrint(screen,"Tutorial", 60, 'white', (WIDTH / 2, HEIGHT / 6))
    textPrint(screen,"Controls", 40, 'white', (WIDTH / 4, HEIGHT / 4))
    textPrint(screen,"Enemy rankings", 40, 'white', (WIDTH * 3 / 4, HEIGHT / 4))

    # Controls
    display_key_a = button(WIDTH / 4 - 130, HEIGHT / 2, 80, 80, 'black', '', "A", 'white', 45, 'white')
    display_key_w = button(WIDTH / 4 - 40, HEIGHT / 2 - 100, 80, 80, 'black', '', "W", 'white', 45, 'white')
    display_key_d = button(WIDTH / 4 + 50, HEIGHT / 2, 80, 80, 'black', '', "D", 'white', 45, 'white')
    display_key_escape = button(WIDTH / 4 - 250, HEIGHT / 2 + 140, 80, 80, 'black', '', "Esc", 'white', 30, 'white')
    display_key_a.check(False, screen)
    display_key_w.check(False, screen)
    display_key_d.check(False, screen)
    display_key_escape.check(False, screen)
    textPrint(screen,"Jump", 30, 'white', (WIDTH / 4 + 120, HEIGHT / 2 - 60))
    textPrint(screen,"Go left", 30, 'white', (WIDTH / 4 - 210, HEIGHT / 2 + 40))
    textPrint(screen,"Go right", 30, 'white', (WIDTH / 4 + 210, HEIGHT / 2 + 40))
    textPrint(screen,"Pause menu", 30, 'white', (WIDTH / 4 - 50, HEIGHT / 2 + 180))

    # Enemy rankings
    image_lvls = pygame.transform.scale(pygame.image.load("resources/textures/lvls.png"), (135, 453))
    screen.blit(image_lvls, (WIDTH * 3 / 4 + 50, HEIGHT / 4 + 50))
    textPrint(screen,"Captain", 25, 'white', (WIDTH * 3 / 4 - 60, HEIGHT / 4 + 83))
    textPrint(screen,"Chief engineer", 25, 'white', (WIDTH * 3 / 4 - 60, HEIGHT / 4 + 83 + 96))
    textPrint(screen,"Second engineer", 25, 'white', (WIDTH * 3 / 4 - 60, HEIGHT / 4 + 83 + 2 * 96))
    textPrint(screen,"Third engineer", 25, 'white', (WIDTH * 3 / 4 - 60, HEIGHT / 4 + 83 + 3 * 96))
    textPrint(screen,"Fourth engineer", 25, 'white', (WIDTH * 3 / 4 - 60, HEIGHT / 4 + 83 + 4 * 96))
    # Red arrow
    surface_arrow = pygame.Surface((400, 30))
    surface_arrow.fill('red')
    textPrint(surface_arrow, "Increasing difficulty", 20, 'white', (175, 17))
    surface_arrow = pygame.transform.rotate(surface_arrow, 270)
    screen.blit(surface_arrow, (WIDTH * 3 / 4 + 200, HEIGHT / 4 + 100))
    pygame.draw.polygon(screen, 'red', [(WIDTH * 3 / 4 + 180, HEIGHT / 4 + 100), (WIDTH * 3 / 4 + 250, HEIGHT / 4 + 100), (WIDTH * 3 / 4 + 215, HEIGHT / 4 + 50)])

    # Waiting for pressing of the menu button
    buttonMenu = button(WIDTH / 2 - 150, HEIGHT / 2 + 200, 300, 80, 'grey', 'darkgrey', "Menu", 'white', 45, 'white')
    waitForInput([buttonMenu])


def menu(name):
    """
    Shows the menu screen with the title of the game. With a button to go to tutorial() and a button to display the story.
    :param name: The name of the player. Can be changed by typing.
    :return the pressed button (Start, Quit) and the (new) name of the player.
    """
    def draw_scene():
        screen.blit(image_background, (0, 0))
        screen.blit(image_floor, (0, 490))
        textPrint(screen,"Titanic: Escape", 100, 'white', (WIDTH / 2, HEIGHT // 4), outline=('black', 7))

        for i in range(len(buttonList)):
            if button.check(buttonList[i], mouseDown, screen):
                return possibleStates[i]

    def story():
        screen.blit(image_landscape, (0, 0))
        textPrint(screen, "The rats of the Titanic", 60, 'white', (WIDTH / 2, 150), outline=('black', 5))
        storyText = ("in the year of 1912, on the 15th of april, the inevitable happened.\n"
                     "The titanic sank to the bottom of the ocean. A lot of people drowned,\n"
                     "only some were rescued. However worst of all, none of the rats abort\n"
                     "the Titanic survived. Whilst the ship was falling apart, roofs coming\n"
                     "down and water filling up the ship, most of the rats scrambled to get\n"
                     "to high ground. Only one singular rat was smart enough to make a sprint\n "
                     "to the lifeboats, sadly the crew stopped this rat. This is where our\n"
                     "game comes in, you will be playing as the one smart rat and fighting\n"
                     "your way to the lifeboat.")
        activatingText = "Do you have what it takes?"
        textPrint(screen,storyText, 35, 'white', (WIDTH / 2, HEIGHT / 2 - 20), outline=('black', 2))
        textPrint(screen, activatingText, 45, 'red', (WIDTH / 2, HEIGHT / 2 + 180), outline=('black', 2))

        disclaimerText = ("This game was made as a tribute to the terrible event\n"
                          "of 15 april 1912. This game is fiction, it is not\n"
                          "intended to mock the disaster in any way.\n"
                          "We respect the victims and the heroes of that horrific night\n"
                          "and trust the players will do the same.\n")
        textPrint(screen, disclaimerText, 15, 'white', (260, HEIGHT - 70), outline=('black', 1))
        # Waiting for pressing of the menu button
        buttonMenu = button(WIDTH / 2 - 150, HEIGHT - 150, 300, 80, 'grey', 'darkgrey', "Menu", 'white', 45,'white')
        waitForInput([buttonMenu])

    buttonPlaying = button(WIDTH / 2 - 150, HEIGHT / 2 - 100, 300, 80, 'grey', 'darkgrey', "Start", 'white', 45, 'white')
    buttonTutorial = button(WIDTH / 2 - 150, HEIGHT / 2, 300, 80, 'grey', 'darkgrey', "How to play", 'white', 45, 'white')
    buttonStory = button(WIDTH / 2 - 150, HEIGHT / 2 + 100, 300, 80, 'grey', 'darkgrey', "Story", 'white', 45, 'white')
    buttonQuit = button(WIDTH / 2 - 150, HEIGHT / 2 + 200, 300, 80, 'grey', 'darkgrey', "Quit", 'white', 45, 'white')
    buttonName = button(WIDTH / 5 - 80, HEIGHT / 2 + 40, 160, 60, 'black', (40, 40, 40), "Change name", 'white', 20, 'black')
    buttonList = [buttonPlaying, buttonTutorial, buttonStory, buttonQuit, buttonName]
    possibleStates = ["Playing", "Tutorial", "Story", "Quit", "Typing"]
    textCenter = (WIDTH // 5, HEIGHT // 2)
    typing = False
    cursor_time = time.time()
    cursor_draw = False
    while True:
        mouseDown = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            elif event.type == pygame.KEYDOWN and typing:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
            elif event.type == pygame.TEXTINPUT and typing:
                if len(name) <= 10:
                    name += event.text
                else:
                    returned_value = draw_scene()
                    if returned_value is not None:
                        return returned_value
                    textPrint(screen,"Too long!", 40, 'red', textCenter, outline=('black', 3))
                    pygame.display.flip()
                    time.sleep(1)

        returned_value = draw_scene()
        if returned_value == "Typing":
            typing = not typing
        elif returned_value == "Tutorial":
            tutorial()
        elif returned_value == "Story":
            story()
        elif returned_value is not None: # Playing, Quit
            return returned_value, name

        textPrint(screen,name, 40, 'white', (WIDTH / 5, HEIGHT / 2), outline=('black', 3))

        # Drawing the flashing cursor.
        if typing and time.time() - cursor_time > 0.8:
            cursor_time = time.time()
            cursor_draw = not cursor_draw
        if typing and cursor_draw:
            rect = textPrint(screen,name, 40, 'white', (WIDTH / 5, HEIGHT / 2), return_rect=True)
            pygame.draw.line(screen, 'black', (textCenter[0] + rect.width / 2 + 8, textCenter[1] - rect.height / 2 - 2),(textCenter[0] + rect.width / 2 + 8, textCenter[1] + rect.height / 2 - 3), 9)
            pygame.draw.line(screen, 'white', (textCenter[0] + rect.width / 2 + 8, textCenter[1] - rect.height / 2),(textCenter[0] + rect.width / 2 + 8, textCenter[1] + rect.height / 2 - 6), 3)
        pygame.display.flip()


def Pause():
    """
    Pauses the game until the player selects an option
    :return the state the player should now be in
    """
    pauseTime = time.time()
    buttonResume = button(WIDTH / 2 - 150, HEIGHT / 2, 300, 80, 'grey', 'darkgrey', "resume", 'white', 45,'white')
    buttonTutorial = button(WIDTH / 2 - 150, HEIGHT / 2 + 100, 300, 80, 'grey', 'darkgrey', "How to play", 'white', 45, 'white')
    buttonMenu = button(WIDTH / 2 - 150, HEIGHT / 2 + 200, 300, 80, 'grey', 'darkgrey', "menu", 'white', 45,'white')
    dimSurface = pygame.Surface((WIDTH, HEIGHT))
    pygame.Surface.set_alpha(dimSurface, 100)

    currentTime = round((time.time() - game_manager.playTime), 2)

    currentScreen = screen.copy()

    buttonList = [buttonResume, buttonTutorial, buttonMenu]
    possibleStates = [None, "Tutorial", "Menu", None]
    while True:
        pygame.Surface.blit(screen, dimSurface)
        textPrint(screen,"Pause", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
        textPrint(screen,str(currentTime) + " seconds playing", 40, 'white', (WIDTH / 2, HEIGHT / 2 + 335))
        index = waitForInput(buttonList, True)
        if possibleStates[index] == "Tutorial":
            tutorial()
            screen.blit(currentScreen, (0, 0))
        else:
            game_manager.playTime += time.time() - pauseTime
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
        textPrint(screen,"Game over", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100))
        textPrint(screen,"Play again?", 50, 'white', (WIDTH / 2, HEIGHT / 2))
        buttonYes = button(WIDTH / 2 - 150, HEIGHT / 2 + 50, 125, 75, 'grey', 'darkgrey', "YES", 'white', 40, 'white')
        buttonNo = button(WIDTH / 2 + 25, HEIGHT / 2 + 50, 125, 75, 'grey', 'darkgrey', "NO", 'white', 40, 'white')

        index = waitForInput([buttonYes, buttonNo])
        possibleStates = ["Playing", "Menu"]
        state = possibleStates[index]
        if index == 0:
            dead = True
        lives = 5
    else:
        textPrint(screen,"You died", 100, 'white', (WIDTH / 2, HEIGHT / 2))
        message = "You have " + str(lives) + " lives left"
        if lives == 1:
            message = message[:-8] + "fe left"
        textPrint(screen,message, 40, 'white', (WIDTH / 2, HEIGHT / 2 + 100))
        pygame.display.flip()
        time.sleep(2)
    return lives, state, dead


def LevelComplete():
    """
    Shows the level complete screen and moves on to the next level
    :return none:
    """
    screen.fill((0, 0, 0))
    textPrint(screen,"Level Completed", 100, 'white', (WIDTH / 2, HEIGHT // 4))
    textPrint(screen,"all hitpoints have been restored", 80, 'white', (WIDTH / 2, HEIGHT // 4 + 300))
    pygame.display.update()
    time.sleep(3)


def end(name):
    """
    Shows the credit screen and waits until the menu button is pressed.
    :return possibleStates[index]:
    """
    screen.fill('black')
    fireworkWord("Thanks for playing", 120)
    screen.blit(image_landscape)
    buttonMenu = button(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 80, 'grey', 'darkgrey', "menu", 'white', 50,
                        'white')
    textPrint(screen,name, 100, 'white', (WIDTH / 2, HEIGHT / 2 - 220) , outline=('black', 7))
    textPrint(screen,"escaped the Titanic", 100, 'white', (WIDTH / 2, HEIGHT / 2 - 100), outline=('black', 7))
    textPrint(screen,"Berend Sulman, Branko Opdam,", 40, 'white',(WIDTH / 2, HEIGHT / 2 - 20), outline=('black', 2))
    textPrint(screen,"Maarten van Ammers & Stijn Zwart", 40, 'white',(WIDTH / 2, HEIGHT / 2 + 50), outline=('black', 2))
    finalTime = round((time.time() - game_manager.playTime), 2)
    textPrint(screen,"You finished in "+ str(finalTime) + " seconds", 40, 'white', (WIDTH / 2, HEIGHT / 2 + 300), outline=('black', 2))

    index = waitForInput([buttonMenu])
    possibleStates = ["Menu"]
    return possibleStates[index]


def Afstand(pos1, pos2):
    x_afstand = pos2[0] - pos1[0]
    y_afstand = pos2[1] - pos1[1]
    if x_afstand < 0:
        x_afstand *= -1
    if y_afstand < 0:
        y_afstand *= -1

    return (x_afstand ** 2 + y_afstand ** 2) **0.5