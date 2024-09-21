import pygame
import sys
import datetime

def new_ingame_day(date):
    date += datetime.timedelta(days=1)
    return date

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# initialize a screen w/ correct dimensions for display
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

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
    screen.fill(WHITE)

    # ADD YOUR OWN CODE TO DRAW EVERYTHING ON THE SCREEN HERE
    # EXAMPLE: screen.blit(your_surface, (x, y)) FOR DISPLAYING IMAGES



    # set limit on num frames per second game will render (cap the frame rate)
    
    # set limit on num frames per second game will render (cap the frame rate)
    delta_seconds = clock.tick(60) / 1000

    total_time += delta_seconds

    seconds_for_day = 60

    if total_time >= seconds_for_day:
        total_time -= seconds_for_day
        game_date = new_ingame_day(game_date)

    current_date_str = game_date.strftime("%Y-%m-%d")
    date_text = font.render(f"Game Date: {current_date_str}", True, BLACK)
    text_width, text_height = date_text.get_size()


    #pygame.draw.rect(screen, BLUE, (screen_width//2 - 25, screen_height//2 - 30, 50, 60))

    screen.blit(date_text, (screen_width - text_width, 10))  # Display the date at the top-left corner

    # update the screen display
    pygame.display.flip()



# quit Pygame
pygame.quit()
sys.exit()
