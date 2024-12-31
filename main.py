import pygame
import sys
from constants import * # importing all from file
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import CircleShape
from shot import Shot
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)
asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
shots = pygame.sprite.Group()
Shot.containers = (shots, updatable, drawable)

def main(): 
	pygame.init() 
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # setting screen size
	clock = pygame.time.Clock() #silly me... create a clock object
	dt = 0
	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # player position

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # exit game on window close
				return
		screen.fill((0, 0 ,0)) # black screen
		for sprite in updatable:
			sprite.update(dt)
		for asteroid in asteroids:  # iterate through your asteroids group
			if player.check_collision(asteroid):  # check collision with each asteroid
				print("Game over!")
				sys.exit()
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip() # screen refresh
		dt = clock.tick(60) / 1000 # setting clock speed to 60 fps
	

if __name__ == "__main__":
	main()