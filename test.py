import pygame
import sys
import datetime
from Job import getSalary
from Job import clicked
from Bank import *

# Initialize Pygame
pygame.init()
init()

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 150)
BLACK = (0, 0, 0)
LIGHT_BLUE = (150, 200, 255)
LIGHT_YELLOW = (255, 255, 197)
ORANGE = (255, 165, 0)
GRAY = (200, 200, 200)

# Set up the game window
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu Example')

# Button positions for main menu
num_home_buttons = 5  # Home, Job, Bank, Investments, Goals

# Button dimensions
button_width = screen_width // num_home_buttons  # Each button occupies an equal width
button_height = screen_height // 10  # Height is a small fraction of the screen height (adjustable)

# Coordinates for each button
home_buttons = {
    "Home": (0, 0, button_width, button_height),
    "Job": (button_width, 0, button_width, button_height),
    "Bank": (2 * button_width, 0, button_width, button_height),
    "Investments": (3 * button_width, 0, button_width, button_height),
}

statistics = {
    "Date": (int(4.20 * button_width), 0, int(0.8 * button_width), button_height // 2)
}

clicker_width = 500
clicker_height = 250
money_width = 300
money_height = 50

job_buttons = {
    "Clicker": (screen_width // 2 - clicker_width // 2, screen_height // 5 * 3 - clicker_height // 2, clicker_width, clicker_height),
    "Salary": (screen_width // 2 - money_width // 2, screen_height // 5 * 3 - clicker_height // 2 - money_height * 2, money_width, money_height)
}

# Define Clock for frame rate control
clock = pygame.time.Clock()
total_time = 0
seconds_for_day = 60

game_date = datetime.datetime(2024, 1, 1)

# Set up font for rendering text
font = pygame.font.Font(None, 36)  # None means default font, 36 is the size

# Bank balances
checking_balance = getCheckingBalance()  # Example initial balance
saving_balance = getSavingsBalance()  # Example initial balance

# Text box variables for the Bank tab
input_box_checking_to_saving = pygame.Rect(100, 400, 300, 50)
input_box_saving_to_checking = pygame.Rect(800, 400, 300, 50)

color_inactive = GRAY
color_active = BLUE
color_checking_to_saving = color_inactive
color_saving_to_checking = color_inactive
active_checking_to_saving = False
active_saving_to_checking = False
text_checking_to_saving = ''  # Input text for transferring money from Checking to Saving
text_saving_to_checking = ''  # Input text for transferring money from Saving to Checking

day_count = 0

def new_ingame_day(date):
    global checking_balance
    global saving_balance
    global day_count
    date += datetime.timedelta(days=1)
    day_count += 1

    # THE VALUE OF THE IF STATEMENT SHOULD BE 14 DAYS BUT ITS 1 DAY FOR THE DEMO
    if day_count == 1:
        addToAccount(getSalary(),"Salary of 2 weeks")
        day_count = 0

    checking_balance = getCheckingBalance()
    saving_balance = getSavingsBalance()
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

# Function to handle transfers between accounts
def transfer_money(from_account, to_account, amount):
    global checking_balance, saving_balance
    try:
        amount = float(amount)
        if from_account == 'Checking' and checking_balance >= amount:
            checking_balance -= amount
            saving_balance += amount
        elif from_account == 'Saving' and saving_balance >= amount:
            saving_balance -= amount
            checking_balance += amount
    except ValueError:
        pass  # Handle invalid input

# Main game loop with state management
def game_loop():
    current_screen = "Home"  # Initial screen is the main menu
    running = True
    global total_time
    global game_date
    global active_checking_to_saving, active_saving_to_checking
    global text_checking_to_saving, text_saving_to_checking
    global checking_balance, saving_balance

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse click events (left click only)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                mouse_pos = event.pos  # Get the position of the mouse click

                # Activate the appropriate text box
                if input_box_checking_to_saving.collidepoint(event.pos):
                    active_checking_to_saving = True
                    active_saving_to_checking = False
                elif input_box_saving_to_checking.collidepoint(event.pos):
                    active_saving_to_checking = True
                    active_checking_to_saving = False
                else:
                    active_checking_to_saving = False
                    active_saving_to_checking = False

                # Update colors
                color_checking_to_saving = color_active if active_checking_to_saving else color_inactive
                color_saving_to_checking = color_active if active_saving_to_checking else color_inactive

                # Check buttons for screen navigation
                for label, (x, y, w, h) in home_buttons.items():
                    if is_mouse_over_button(mouse_pos, (x, y, w, h)):
                        current_screen = label

                if current_screen == "Job":
                    if is_mouse_over_button(mouse_pos, job_buttons["Clicker"]):
                        clicked()
                        checking_balance = getCheckingBalance()
                        saving_balance = getSavingsBalance()

            # If a key is pressed and the text box is active
            if event.type == pygame.KEYDOWN:
                if active_checking_to_saving:
                    if event.key == pygame.K_RETURN:
                        transfer_money('Checking', 'Saving', text_checking_to_saving)
                        text_checking_to_saving = ''  # Clear the text box after submission
                    elif event.key == pygame.K_BACKSPACE:
                        text_checking_to_saving = text_checking_to_saving[:-1]  # Remove last character
                    else:
                        text_checking_to_saving += event.unicode  # Add typed character

                if active_saving_to_checking:
                    if event.key == pygame.K_RETURN:
                        transfer_money('Saving', 'Checking', text_saving_to_checking)
                        text_saving_to_checking = ''  # Clear the text box after submission
                    elif event.key == pygame.K_BACKSPACE:
                        text_saving_to_checking = text_saving_to_checking[:-1]  # Remove last character
                    else:
                        text_saving_to_checking += event.unicode  # Add typed character

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
            draw_button("Home", home_buttons["Home"], ORANGE, BLACK)

        elif current_screen == "Job":
            draw_button("Job", home_buttons["Job"], ORANGE, BLACK)
            draw_button("Click to make money", job_buttons["Clicker"], WHITE, BLACK)
            draw_button("Salary: " + str(getSalary()) + '$', job_buttons["Salary"], WHITE, BLACK)

        elif current_screen == "Bank":
            draw_button("Bank", home_buttons["Bank"], ORANGE, BLACK)

            # Draw Bank tab buttons and text boxes for Checking and Saving
            draw_button(f"Checking Balance: ${checking_balance:.2f}", (50, 100, 500, 50), WHITE, BLACK)
            draw_button(f"Saving Balance: ${saving_balance:.2f}", (650, 100, 500, 50), WHITE, BLACK)

            # Draw text boxes
            pygame.draw.rect(screen, color_checking_to_saving, input_box_checking_to_saving, 2)
            pygame.draw.rect(screen, color_saving_to_checking, input_box_saving_to_checking, 2)

            # Render text input in text boxes
            txt_surface_checking_to_saving = font.render(text_checking_to_saving, True, BLACK)
            txt_surface_saving_to_checking = font.render(text_saving_to_checking, True, BLACK)

            screen.blit(txt_surface_checking_to_saving, (input_box_checking_to_saving.x + 5, input_box_checking_to_saving.y + 5))
            screen.blit(txt_surface_saving_to_checking, (input_box_saving_to_checking.x + 5, input_box_saving_to_checking.y + 5))

        elif current_screen == "Investments":
            draw_button("Investments", home_buttons["Investments"], ORANGE, BLACK)

        else:
            print("error")

        # Update the display
        pygame.display.flip()

# Run the game loop
game_loop()
