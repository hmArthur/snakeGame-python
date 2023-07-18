import pygame, random
from pygame.locals import *


class Food :
    bounds = None

    foodx = None
    foody = None

    def __init__(self, bounds) :
        self.bounds = bounds

    def spawn(self) : 
        self.foodx = round(random.randrange(0, self.bounds[0] - 10) / 10.0) * 10.0
        self.foody = round(random.randrange(0, self.bounds[1] - 10) / 10.0) * 10.0

    def check_state(self, snake) : 
        if snake.player_x == self.foodx and snake.player_y == self.foody :
            self.spawn()
            snake.speed_change()
            snake.add_segment()
    
    def draw(self, game, window) :
        game.draw.rect(window, (43, 100, 29), [self.foodx, self.foody, 10, 10]) 

