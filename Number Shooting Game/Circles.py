from Sprite import Sprite
import random
import pygame
import math

class Circle(Sprite):
    def __init__(self):
        self._alive = False
        self._speed = random.randint(1, 5)
        self._angular_speed = random.randint(3,7) / 1000
        self._angle = (random.randint(0, 180) / 180) * math.pi
        self._original_pos_x = random.randint(500, 900)
        self._original_pos_y = random.randint(600, 800)
        self._pos_x = self._original_pos_x
        self._pos_y = self._original_pos_y
        self._type = random.randint(1, 4)

        if self._type == 1:
            self._sprite = pygame.image.load("Sprites/Circle1.png")
        elif self._type == 2:
            self._sprite = pygame.image.load("Sprites/Circle2.png")
            self._angle = 0
        elif self._type == 3:
            self._sprite = pygame.image.load("Sprites/Circle3.png")
            self._angle = 0
        else:
            self._sprite = pygame.image.load("Sprites/Circle4.png")

    def update(self):
        if self._alive == True:
            self._angle += self._angular_speed
            if self._alive == True:
                if self._type == 1:
                    self.move_in_line()
                if self._type == 2:
                    self.move_in_circle()
                if self._type == 3:
                    self.move_in_line()
                    self.move_in_circle()
                if self._type == 4:
                    self.move_in_line()
