import pygame
from pygame.locals import *

class Snake :
    gameOver = False

    snake_speed = 10
    length = 1

    direction = ''

    player_x = 0
    player_y = 0

    body = None

    bounds = None

    acelerationX = 0
    acelerationY = 0

    block_size = 10

    def __init__(self, block_size, bounds) :
        self.block_size = block_size
        self.bounds = bounds

    def respawn(self) : 
        self.lenght = 1
        self.player_x = self.bounds[0] / 2
        self.player_y = self.bounds[1] / 2
        self.body = [(self.bounds[0] / 2, self.bounds[1] / 2)]
    
    def draw(self, game, window) :
        for segment in self.body :
            game.draw.rect(window, (43, 49, 29),[segment[0], segment[1], self.block_size, self.block_size])  

    def move(self, game) :
        self.body[-1] = (self.player_x, self.player_y)        

        for event in game.event.get() :
            if event.type == QUIT :
                self.gameOver = True 

            if event.type == game.KEYDOWN :
                if event.key == game.K_LEFT and self.direction != 'right':
                    self.acelerationX = -10
                    self.acelerationY = 0
                    self.direction = 'left'

                elif event.key == game.K_RIGHT and self.direction != 'left':
                    self.acelerationX = 10
                    self.acelerationY = 0
                    self.direction = 'right'

                elif event.key == game.K_UP and self.direction != 'down':
                    self.acelerationX = 0
                    self.acelerationY = -10
                    self.direction = 'up'

                elif event.key == game.K_DOWN and self.direction != 'up':
                    self.acelerationX = 0
                    self.acelerationY = 10
                    self.direction = 'down'
             

        self.player_x += self.acelerationX
        self.player_y += self.acelerationY

        if self.length < len(self.body) :
            self.body.pop(0)
    
    def check_death (self) :
        print(self.player_x, self.player_y)
        if self.player_x == (self.bounds[0]) or self.player_y == (self.bounds[1]) or  self.player_x < 0 or self.player_y < 0: 
            self.gameOver = True
        
        current_head = self.body[-1]
        check_death = 0

        for i in range(len(self.body) - 1) :
            segment = self.body[i]

            if segment[0] == current_head[0] and segment[1] == current_head[1]  :
                self.gameOver = True
            
            
    
    def speed_change (self) :
        self.snake_speed += 0
    
    def add_segment(self) :
        self.length += 1
    
    def adm_segments(self) : 
        current_head = self.body[-1]

        if(self.direction == 'down') :
            next_head = (current_head[0], current_head[1] + self.block_size)
            self.body.append(next_head)
        elif (self.direction == 'up') :
            next_head = (current_head[0], current_head[1] - self.block_size)
            self.body.append(next_head)
        elif (self.direction == 'left') :
            next_head = (current_head[0] - self.block_size, current_head[1])
            self.body.append(next_head)
        elif (self.direction == 'right') :
            next_head = (current_head[0] + self.block_size, current_head[1])
            self.body.append(next_head)
