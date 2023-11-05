import pygame.mouse
from Sprite import Sprite

class Crosshair(Sprite):
    def __init__(self, speed, angle, original_pos_y, original_pos_x, pos_x, pos_y, sprite):
        self._alive = True
        self._sprite = sprite

    def update(self):
        self._pos_x = pygame.mouse.get_pos()[0] - 55
        self._pos_y = pygame.mouse.get_pos()[1] - 60