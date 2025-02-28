import pygame
from pygame import RESIZABLE
WIDTH = 1366
HEIGHT = 690
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

def draw_floor():
    pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 25)
