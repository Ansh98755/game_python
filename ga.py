import pygame  # Importing the essential tools for game development from the Python library
from sys import exit

pygame.init()  # Initializing the Pygame library, which is crucial for using its functions (sound, animation, etc.)

# Setting up the display
screen = pygame.display.set_mode((1000, 800))  # Creating a window with a width of 1000 pixels and a height of 800 pixels
pygame.display.set_caption("Space Dodge")  # Setting the title of the window

# Loading the background image
BG = pygame.image.load("s.jpg")
BG=pygame.transform.scale(pygame.image.load("s.jpg"),(1000,800))
player_width=60
player_height=50
# Function to draw elements on the screen
def draw(player):
    screen.blit(BG, (0, 0))  # Drawing the background image at the top-left corner (0, 0)
    pygame.draw.rect(screen,"red",player)
    pygame.display.update()  # Updating the display to reflect the changes

# Main function to run the game loop
def main():
    player=pygame.Rect(200,800-player_height,player_width,player_height)
    clock = pygame.time.Clock()  # Creating a clock object to control the frame rate

    while True:
        for event in pygame.event.get():  # Handling events
            if event.type == pygame.QUIT:  # Checking if the quit event is triggered (e.g., closing the window)
                pygame.quit()  # Quitting Pygame
                exit()  # Exiting the program

        draw(player)  # Calling the draw function to render the background

        clock.tick(60)  # Setting the frame rate to 60 frames per second (FPS)

# Running the main function
if __name__ == "__main__":
    main()