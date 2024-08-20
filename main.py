from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    Game_Clock = pygame.time.Clock()
    delta_t = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.contaiers = (updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_WIDTH/2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(delta_t)
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        delta_t = Game_Clock.tick(60) / 1000

if __name__ == '__main__':
    main()