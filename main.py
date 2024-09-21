import pygame
import sys
import datetime

def new_ingame_day(date):
    date += datetime.timedelta(days=1)
    return date

def draw_box(screen, button_color, x, y, width, height, text):
    box_rect = pygame.Rect(
        screen_width - text_width - 2*padding,  # X position
        0,                                            # Y position
        text_width + padding * 2,                      # Box width (text width + padding on both sides)
        text_height + padding * 2                      # Box height (text height + padding on top and bottom)
    )
    pygame.draw.rect(screen, button_color, box_rect)


pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (150, 200, 255)  # Light blue color for the box
LIGHT_YELLOW = (255, 255, 197)

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
    screen.fill(LIGHT_BLUE)

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
    
    draw_box(screen, LIGHT_YELLOW, )

    current_date_str = game_date.strftime("%Y-%m-%d")
    date_text = font.render(f"Date: {current_date_str}", True, BLACK)
    text_width, text_height = date_text.get_size()
    
    padding = 10

    # Define the rectangle for the box with padding
    
    
    # add border to rectangle?

    screen.blit(date_text, ((box_rect.x + padding, box_rect.y + padding)))  # Display the date at the top-left corner

    # update the screen display
    pygame.display.flip()



# quit Pygame
pygame.quit()
sys.exit()
