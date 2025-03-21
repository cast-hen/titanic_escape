import pygame

screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()

pygame.draw.line(screen, 'white', (12.31, 32.9), (238, 33.4))
pygame.display.flip()
while True:
    pass