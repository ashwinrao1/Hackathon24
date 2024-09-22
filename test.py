import pygame
import sys
import datetime
from Job import getSalary
from Job import  clicked


# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 150)
BLACK = (0, 0, 0)
LIGHT_BLUE = (150, 200, 255)
LIGHT_YELLOW = (255, 255, 197)
ORANGE = (255, 165, 0)

# Set up the game window
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu Example')


# Button positions for main menu
num_home_buttons = 5  # Home, Job, Bank, Investments, Goals, Static-Stats

# Button dimensions
button_width = screen_width // num_home_buttons  # Each button occupies an equal width
button_height = screen_height // 10  # Height is a small fraction of the screen height (adjustable)

# Coordinates for each button
home_buttons = {
    "Home": (0, 0, button_width, button_height),
    "Job": (button_width, 0, button_width, button_height),
    "Bank": (2 * button_width, 0, button_width, button_height),
    "Investments": (3 * button_width, 0, button_width, button_height),
    #"Goals": (4 * button_width, 0, button_width, button_height),
}

statistics = {
    "Date": (int(4.20 * button_width), 0, int(0.8 * button_width), button_height // 2)
}

clicker_width = 500
clicker_height = 250
money_width = 300
money_height = 50

job_buttons = {
    "Clicker" : (screen_width // 2 - clicker_width // 2, screen_height // 5 * 3 - clicker_height // 2, clicker_width, clicker_height),
    "Salary" : (screen_width // 2 - money_width // 2, screen_height // 5 * 3 - clicker_height // 2 - money_height * 2, money_width, money_height)
}

bank_buttons = {
    "Checking"
}

# Define Clock for frame rate control
clock = pygame.time.Clock()
total_time = 0
seconds_for_day = 60

game_date = datetime.datetime(2024, 1, 1)

# Set up font for rendering text
font = pygame.font.Font(None, 36)  # None means default font, 36 is the size

def new_ingame_day(date):
    date += datetime.timedelta(days=1)
    return date

# Function to check if the mouse is over the button
def is_mouse_over_button(mouse_pos, button):
    mouse_x, mouse_y = mouse_pos
    x, y, width, height = button
    return x < mouse_x < x + width and y < mouse_y < y + height

def draw_buttons(buttons, back_color, text_color):
    for label, (x, y, w, h) in buttons.items():
        pygame.draw.rect(screen, back_color, (x, y, w, h))  
        button_text = font.render(label, True, text_color)  
        screen.blit(button_text, (x + (w - button_text.get_width()) // 2, y + (h - button_text.get_height()) // 2))

def draw_button(text, button, back_color, text_color):
    x, y, w, h = button
    pygame.draw.rect(screen, back_color, (x, y, w, h))  
    button_text = font.render(text, True, text_color)  
    screen.blit(button_text, (x + (w - button_text.get_width()) // 2, y + (h - button_text.get_height()) // 2))

# Main game loop with state management
def game_loop():
    current_screen = "Home"  # Initial screen is the main menu
    running = True
    global total_time
    global game_date

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse click events (left click only)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                mouse_pos = event.pos  # Get the position of the mouse click

                
                for label, (x, y, w, h) in home_buttons.items():
                    if is_mouse_over_button(mouse_pos, (x, y, w, h)):
                        current_screen = label
                
                if current_screen == "Job":
                    if is_mouse_over_button(mouse_pos, job_buttons["Clicker"]):
                        clicked()


        # Clear the screen with white background
        screen.fill(LIGHT_BLUE)

        delta_seconds = clock.tick(60) / 1000
        total_time += delta_seconds

        if total_time >= seconds_for_day:
            total_time -= seconds_for_day
            game_date = new_ingame_day(game_date)

        draw_button(game_date.strftime("%Y-%m-%d"), statistics["Date"], LIGHT_YELLOW, BLACK)

        draw_buttons(home_buttons, LIGHT_YELLOW, BLACK)

        # Draw the appropriate screen
        if current_screen == "Home":
            # do something
            draw_button("Home", home_buttons["Home"], ORANGE, BLACK)
            

        elif current_screen == "Job":
            draw_button("Job", home_buttons["Job"], ORANGE, BLACK)
            draw_button("Click to make money", job_buttons["Clicker"], WHITE, BLACK)
            draw_button("Salary: " + str(getSalary()) + '$', job_buttons["Salary"], WHITE, BLACK)

            #draw inputbox
            txt_surface = font.render(text, True, BLACK)
            width = max(300, txt_surface.get_width() + 10)  # Resize the box if needed
            input_box.w = width
            pygame.draw.rect(screen, color, input_box, 2)  # Draw the text box (border)
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  # Render the text

        
        elif current_screen == "Bank":
            draw_button("Bank", home_buttons["Bank"], ORANGE, BLACK)

        elif current_screen == "Investments":
            draw_button("Investments", home_buttons["Investments"], ORANGE, BLACK)

        else:
            print("error")

        # Update the display
        pygame.display.flip()

# Run the game loop
game_loop()
