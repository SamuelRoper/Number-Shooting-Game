from Sprite import Sprite
import pygame.transform

class Bullet(Sprite):
    def __init__(self, speed, angle, original_pos_y, original_pos_x, pos_x, pos_y, sprite):
        self._angle = self.calculate_angle() - 170
        self._alive = True
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._speed = speed
        self._sprite = sprite

    def update(self):
        self.move_in_line()

    def draw(self, screen):
        if self._alive == True:
            new_sprite = pygame.transform.rotate(self._sprite, self._angle + 270)
            screen.blit(new_sprite, (self._pos_x, self._pos_y))
