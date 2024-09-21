import pygame
import sys
import datetime

def new_ingame_day():
    return None


pygame.init()

# initialize a screen w/ correct dimensions for display
screen = pygame.display.set_mode((1200, 700))

pygame.display.set_caption('Hackathon Game - Date Function')

# create an object to help track time
clock = pygame.time.Clock()
total_time = 0
game_date = datetime.datetime(2024, 1, 1)

font = pygame.font.Font(None, 36) 
running = True

while running:
  # iterate through each event in the game's event queue
    for event in pygame.event.get():
      # if an event is of type "QUIT", set game as no longer running
        if event.type == pygame.QUIT:
            running = False

    # ADD YOUR OWN CODE FOR GAME LOGIC HERE
    # EXAMPLE: MOVING OBJECTS, COLLISION DETECTION, ETC. 

    # clear the screen (make it black)
    screen.fill((0,0,0))

    # ADD YOUR OWN CODE TO DRAW EVERYTHING ON THE SCREEN HERE
    # EXAMPLE: screen.blit(your_surface, (x, y)) FOR DISPLAYING IMAGES

    # update the screen display
    pygame.display.flip()

    # set limit on num frames per second game will render (cap the frame rate)
    
    # set limit on num frames per second game will render (cap the frame rate)
    delta_seconds = clock.tick(60) / 1000

    total_time += delta_seconds

    if total_time >= 60:
        total_time -= 60
        new_ingame_day()

# quit Pygame
pygame.quit()
sys.exit()
