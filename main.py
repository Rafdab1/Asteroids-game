from constants import *
import pygame

def main():
    Game_Clock = pygame.time.Clock()
    delta_t = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        delta_t = Game_Clock.tick(60) / 1000

if __name__ == '__main__':
    main()