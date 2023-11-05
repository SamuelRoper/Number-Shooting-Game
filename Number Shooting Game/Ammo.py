from Sprite import Sprite
import pygame.image

class Ammo(Sprite):
    def __init__(self, speed, angle, original_pos_y, original_pos_x, pos_x, pos_y, sprite, number):
        self._alive = True
        self._pos_x = pos_x + (20 * (number-1))
        self._pos_y = pos_y
        self._sprite = sprite
        self._sprite_have = pygame.image.load("Sprites/Ammo_left.png")
        self._sprite_have_not = pygame.image.load("Sprites/No_ammo_left.png")
        self._number = number

    def update(self, number_of_bullets):
        if self._number > number_of_bullets:
            self._sprite = self._sprite_have_not
        else:
            self._sprite = self._sprite_have


