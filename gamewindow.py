import pygame
import math
from objects import Prey, Predator

pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 650

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill((255, 255, 255))

def display_info(object, keys_pressed, window, position, control_keys):
    # Determine the direction based on keys pressed
    direction_str = []
    if keys_pressed[control_keys['left']]:
        direction_str.append("Left")
    if keys_pressed[control_keys['right']]:
        direction_str.append("Right")
    if keys_pressed[control_keys['up']]:
        direction_str.append("Up")
    if keys_pressed[control_keys['down']]:
        direction_str.append("Down")

    direction_text = ", ".join(direction_str) if direction_str else "None"

    # Render text
    position_text = f'Object: x: {object.x:.2f}, y: {object.y:.2f}'
    direction_text = f'Direction: {direction_text}'
    text_surface1 = myfont.render(position_text, False, (0, 0, 0))
    text_surface2 = myfont.render(direction_text, False, (0, 0, 0))
    
    # Determine the x-coordinate based on the position parameter
    if position == "right":
        x_coord = WINDOW_WIDTH - text_surface1.get_width() - 10
    elif position == "left":
        x_coord = 10
    else:
        raise ValueError("Invalid position parameter")
    
    # Position text at the bottom-right or bottom-left corner
    text_position1 = (x_coord, WINDOW_HEIGHT - text_surface1.get_height() - 10)
    text_position2 = (x_coord, WINDOW_HEIGHT - text_surface1.get_height() - text_surface2.get_height() - 20)
    
    # Draw the text on the window
    window.blit(text_surface1, text_position1)
    window.blit(text_surface2, text_position2)



# Create instances of Prey and Predator classes
prey_control_keys = {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s}
prey = Prey(100, 100, prey_control_keys)
predator_control_keys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}
predator = Predator(200, 200, predator_control_keys)



# Initialize Pygame font
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 20)


# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    window.fill((255, 255, 255))
    
    # Get the keys pressed by the user
    keys_pressed = pygame.key.get_pressed()

    # Move the prey based on the keys pressed
    prey.move(keys_pressed)
    prey.draw(window)

    # Move the predator based on the keys pressed
    predator.move(keys_pressed)

    
    predator.draw(window)  # Add movement logic for predator as needed
    
    # Display position and direction information
    display_info(prey, keys_pressed, window, "right", prey_control_keys)
    display_info(predator, keys_pressed, window, "left", predator_control_keys)


    pygame.display.update()