import pygame  # Importing the essential tools for game development from the Python library
from sys import exit
import time  # Importing time module for elapsed time calculation

pygame.init()  # Initializing the Pygame library, which is crucial for using its functions (sound, animation, etc.)

# Setting up the display
screen = pygame.display.set_mode((1000, 800))  # Creating a window with a width of 1000 pixels and a height of 800 pixels
pygame.display.set_caption("Space Dodge")  # Setting the title of the window

# Loading and scaling the background image
BG = pygame.transform.scale(pygame.image.load("s.jpg"), (1000, 800))

# Player dimensions and velocity
player_width = 60
player_height = 100
player_vel = 7

# Initializing font
Font = pygame.font.SysFont("cosmicsans", 30)

# Function to draw elements on the screen
def draw(player, elapsed_time):
    screen.blit(BG, (0, 0))  # Drawing the background image at the top-left corner (0, 0)
    time_text = Font.render(f"Time: {round(elapsed_time)}s", True, "white")
    screen.blit(time_text, (10, 10))
    pygame.draw.rect(screen, "red", player)  # Drawing the player as a red rectangle
    pygame.display.update()  # Updating the display to reflect the changes

# Main function to run the game loop
def main():
    player = pygame.Rect(200, 800 - player_height, player_width, player_height)  # Creating the player rectangle
    clock = pygame.time.Clock()  # Creating a clock object to control the frame rate
    start_time = time.time()  # Recording the start time for elapsed time calculation

    while True:
        elapsed_time = time.time() - start_time  # Calculating elapsed time
        for event in pygame.event.get():  # Handling events
            if event.type == pygame.QUIT:  # Checking if the quit event is triggered (e.g., closing the window)
                pygame.quit()  # Quitting Pygame
                exit()  # Exiting the program
            
        keys = pygame.key.get_pressed()  # Getting the state of all keyboard buttons
        if keys[pygame.K_LEFT] and player.x - player_vel >= 0:  # Moving left if the left key is pressed and within bounds
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player_width <= 1000:  # Moving right if the right key is pressed and within bounds
            player.x += player_vel

        draw(player, elapsed_time)  # Calling the draw function to render the background and the player

        clock.tick(60)  # Setting the frame rate to 60 frames per second (FPS)

# Running the main function
if __name__ == "__main__":
    main()
