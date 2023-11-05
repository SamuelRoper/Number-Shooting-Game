import math
import pygame.mouse

class Sprite():
    def __init__(self, speed, angle, original_pos_y, original_pos_x, pos_x, pos_y, sprite):
        self._alive = True
        self._speed = speed
        self._angle = angle
        self._original_pos_y = original_pos_y
        self._original_pos_x = original_pos_x
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._sprite = sprite

    #draws the sprite to the sceen
    def draw(self, screen):
        if self._alive == True:
            screen.blit(self._sprite, (self._pos_x, self._pos_y))


    #when a sprite leaves the window the sprite dissapears
    def check_inside_window(self):
        if self._pos_x > 1800 or self._pos_x < 0:
            self.set_alive(False)
            self._pos_x = 600
            return(False)
        elif self._pos_y > 1000 or self._pos_y < 0:
            self.set_alive(False)
            self._pos_y = 500
            return(False)
        else:
            return(True)


    def move_in_line(self):
        self._pos_x += self._speed * (math.cos((self._angle / 180) * math.pi))
        self._pos_y -= self._speed * (math.sin((self._angle / 180) * math.pi))

    #calculates angle from gun to crosshair
    def calculate_angle(self):
        adjacent = pygame.mouse.get_pos()[0] - 700
        opposite = pygame.mouse.get_pos()[1] - 900
        # to avoid dividing by zero
        if adjacent != 0:
            angle = math.atan(opposite / adjacent)
            angle = 180 - (angle / math.pi) * 180
            if pygame.mouse.get_pos()[0] < 700:
                angle = angle - 180
        elif pygame.mouse.get_pos()[0] == 700:
            angle = 90
        elif pygame.mouse.get_pos()[0] > 700 and pygame.mouse.get_pos()[1] == 900:
            angle = 0
        else:
            angle = 180

        if pygame.mouse.get_pos()[0] < 700:
            angle += + 360
        return(angle)

    #moves sprite in a circle
    def move_in_circle(self):
        self._pos_x = self._original_pos_x * math.cos(self._angle) + self._original_pos_y * math.sin(self._angle)
        self._pos_y = (-1) * self._original_pos_x * math.sin(self._angle) + self._original_pos_y * math.cos(self._angle)

    #getters
    def get_pos_x(self):
        return(self._pos_x)

    def get_pos_y(self):
        return(self._pos_y)

    def get_angle(self):
        return(self._angle)

    def get_status(self):
        return(self._alive)

    def get_sprite(self):
        return(self._sprite)

    #setters
    def set_alive(self, status):
        self._alive = status