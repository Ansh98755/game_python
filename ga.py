import pygame
from sys import exit
import time
import random

pygame.init()

# Setting up the display
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Space Dodge")

# Loading and scaling the background image
BG = pygame.transform.scale(pygame.image.load("s.jpg"), (1000, 800))

# Player dimensions and velocity
player_width = 60
player_height = 100
player_vel = 7
star_width = 10
star_height = 20
star_vel = 5

# Initializing font
Font = pygame.font.SysFont("cosmicsans", 30)

# Function to draw elements on the screen
def draw(player, stars, elapsed_time):
    screen.blit(BG, (0, 0))
    time_text = Font.render(f"Time: {round(elapsed_time)}s", True, "white")
    screen.blit(time_text, (10, 10))
    pygame.draw.rect(screen, "red", player)
    
    for star in stars:
        pygame.draw.rect(screen, "yellow", star)
    
    pygame.display.update()

# Function to display the game over screen
def game_over_screen(elapsed_time):
    screen.blit(BG, (0, 0))
    game_over_text = Font.render("Game Over", True, "white")
    time_survived_text = Font.render(f"You survived for {round(elapsed_time)} seconds", True, "white")
    screen.blit(game_over_text, (400, 300))
    screen.blit(time_survived_text, (320, 350))
    pygame.display.update()
    pygame.time.wait(3000)

# Main function to run the game loop
def main():
    player = pygame.Rect(200, 800 - player_height, player_width, player_height)
    clock = pygame.time.Clock()
    start_time = time.time()
    star_add_increment = 2000
    star_count = 0
    stars = []

    while True:
        elapsed_time = time.time() - start_time
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, 1000 - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel >= 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player_width <= 1000:
            player.x += player_vel

        for star in stars[:]:
            star.y += star_vel
            if star.colliderect(player):
                game_over_screen(elapsed_time)
                pygame.quit()
                exit()
            if star.y > 800:
                stars.remove(star)

        draw(player, stars, elapsed_time)
        star_count += clock.tick(60)

if __name__ == "__main__":
    main()
