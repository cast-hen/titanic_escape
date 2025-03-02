import pygame
from pygame import RESIZABLE
WIDTH = 1366
HEIGHT = 690
gravity = 0.6
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)



class Objects:
    def __init__(self, xpos, ypos, width, height, color, mass, xspeed, yspeed, ObjectScene):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.mass = mass
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.Rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.on_ground = False
        self.ObjectScene = ObjectScene

    def update_pos(self, platforms, CameraPosx, scene):

        self.xpos += self.xspeed
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)

        for platform in platforms:
            if platform.ObjectScene == scene:
                if self.Rect.colliderect(platform.Rect):
                    if self.xspeed > 0:
                        self.xpos = platform.xpos - self.width
                    elif self.xspeed < 0:
                        self.xpos = platform.xpos + platform.width
                    self.xspeed = 0
                    self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)

        self.yspeed += self.mass * gravity

        self.ypos += self.yspeed
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
        self.on_ground = False

        # platformcollision
        for platform in platforms:
            if platform.ObjectScene == scene:
                if self.Rect.colliderect(platform.Rect):
                    if self.yspeed > 0:  # Falling
                        self.ypos = platform.ypos - self.height
                        self.yspeed = 0
                        self.on_ground = True
                    elif self.yspeed < 0:  # Hitting ceiling
                        self.ypos = platform.ypos + platform.height
                        self.yspeed = 0
                    self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
                    return platform.color == "orange"

        # wall en floor collision
        if self.ypos + self.height >= HEIGHT - 4:
            self.ypos = HEIGHT - self.height - 4
            self.yspeed = 0
            self.on_ground = True
            self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)
        if self.xpos + self.width > WIDTH:
            self.xpos = WIDTH - self.width
        self.Rect.topleft = (self.xpos - CameraPosx, self.ypos)

    def draw(self, surface, CameraPosx):
        self.Rect = pygame.draw.rect(surface, self.color, (self.xpos - CameraPosx, self.ypos, self.width, self.height))


# maakt vloer
def draw_floor():
    pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 25)
