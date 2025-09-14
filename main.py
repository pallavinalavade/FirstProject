import random
import pygame
import sys
from pygame.locals import *


pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (screen_info.current_w, screen_info.current_h)
score_font = pygame.font.SysFont(None, 70)
display_font = pygame.font.SysFont(None, 25)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255, 224, 179)

sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()

def main(): 
    game_over = False 
    while True: 
        clock.tick(60) 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                sys.exit() 
            if event.type == KEYDOWN: 
                if event.key == K_f: 
                    pygame.display.set_mode(size, FULLSCREEN) 
                if event.key == K_ESCAPE: 
                    pygame.display.set_mode(size) 
        screen.fill(color) 
        platforms.draw(screen) 
        sprite_list.draw(screen) 
        pygame.display.flip() 

if __name__ == "__main__": 
    main()