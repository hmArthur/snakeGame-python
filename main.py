import pygame, sys, time
from pygame.locals import *
from snake import *
from food import *

pygame.init()

BACKGROUND = (141, 162, 89)

FPS = pygame.time.Clock()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("snake game")
pygame.display.set_icon(pygame.image.load('icon.jpg'))

def message(msg, color, pos, size) :
    mesg = pygame.font.SysFont(None, size).render(msg, True, color)
    WINDOW.blit(mesg, pos)

def main() :  
    gameOver = False


    snake = Snake(10, (WINDOW_WIDTH, WINDOW_HEIGHT))
    snake.respawn()

    food = Food((WINDOW_WIDTH, WINDOW_HEIGHT))
    food.spawn()

  
    while not snake.gameOver :
        WINDOW.fill(BACKGROUND)

        
        snake.draw(pygame, WINDOW)
        snake.move(pygame)
        snake.check_death()
        snake.adm_segments()

        food.draw(pygame, WINDOW)
        food.check_state(snake)
      
        message("your score: " + str(snake.length - 1),(43, 49, 29), [0, 0], 30)
     
        pygame.display.update()
        FPS.tick(snake.snake_speed)
        print(snake.snake_speed)

    message("wasted", (43, 49, 29), [WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT /2 - 30], 50)
    pygame.display.update()

    time.sleep(2)
    
    pygame.quit()
    sys.exit()  
 

main()
