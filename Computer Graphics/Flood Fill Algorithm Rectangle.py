
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Flood Fill Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Fill background
screen.fill(WHITE)

# Draw rectangle
pygame.draw.rect(screen, BLACK, (150, 100, 300, 250), 3)

# Display instructions
font = pygame.font.SysFont(None, 28)
title = font.render("Flood Fill Algorithm", True, BLACK)
screen.blit(title, (140, 30))

pygame.display.flip()


# Flood Fill Algorithm with Animation
def flood_fill(surface, x, y, old_color, new_color):

    width, height = surface.get_size()

    stack = [(x, y)]
    count = 0

    while stack:

        # Handle window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        x, y = stack.pop()

        # Check screen boundaries
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        current_color = surface.get_at((x, y))[:3]

        # Check old color
        if current_color == old_color:

            # Fill pixel
            surface.set_at((x, y), new_color)

            # Add neighboring pixels
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

            count += 1

            # Update screen after every 100 pixels
            if count % 100 == 0:
                pygame.display.flip()
                pygame.time.delay(10)

    # Display final result
    pygame.display.flip()


# Start Flood Fill from seed point
flood_fill(screen, 200, 150, WHITE, BLUE)


# Main event loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
