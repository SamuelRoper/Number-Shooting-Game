from Sprite import Sprite
import math
import pygame.transform



class Gun(Sprite):
    def __init__(self, angle, pos_x, pos_y, sprite):
        self._alive = True
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._sprite = sprite
        self._angle = angle

    def draw(self, screen):
        self._angle = self.calculate_angle()
        new_sprite = pygame.transform.rotate(self._sprite, self._angle + 10)
        screen.blit(new_sprite, (self._pos_x, self._pos_y))

