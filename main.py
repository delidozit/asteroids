import pygame
from constants import * # importing all from file
from player import Player

def main(): 
	pygame.init() 
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # setting screen size
	clock = pygame.time.Clock() #silly me... create a clock object
	dt = 0
	
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # exit game on window close
				return
		screen.fill((0, 0 ,0)) # black screen
		player.update(dt) # update players dt state
		player.draw(screen) # draw the triangle for player
		pygame.display.flip() # screen refresh
		dt = clock.tick(60) / 1000 # setting clock speed to 60 fps
	

if __name__ == "__main__":
	main()