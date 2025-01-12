# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =     pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
 
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        for asteroid in asteroids:
            if player.check_for_collision(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.check_for_collision(shot):
                    asteroid.split()
                    shot.kill()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
