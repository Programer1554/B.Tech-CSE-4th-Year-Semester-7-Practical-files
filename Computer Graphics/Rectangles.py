
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 1000
HEIGHT = 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Flood Fill and Boundary Fill")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
GRAY = (235, 235, 235)

# Fonts
title_font = pygame.font.SysFont("Arial", 28, bold=True)
font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 16)

# Rectangle dimensions
SURFACE_WIDTH = 360
SURFACE_HEIGHT = 280

# Create separate surfaces
flood_surface = pygame.Surface(
    (SURFACE_WIDTH, SURFACE_HEIGHT)
)

boundary_surface = pygame.Surface(
    (SURFACE_WIDTH, SURFACE_HEIGHT)
)

# Set white background
flood_surface.fill(WHITE)
boundary_surface.fill(WHITE)

# Draw black rectangle boundaries
pygame.draw.rect(
    flood_surface,
    BLACK,
    (20, 20, 320, 240),
    4
)

pygame.draw.rect(
    boundary_surface,
    BLACK,
    (20, 20, 320, 240),
    4
)


# ==========================================
# 1. FLOOD FILL ALGORITHM
# ==========================================

def flood_fill(surface, x, y, newColor, targetColor):

    width, height = surface.get_size()

    # Stack to simulate recursive calls
    stack = [(x, y)]

    while stack:

        x, y = stack.pop()

        # Check whether pixel is out of bounds
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        currentColor = surface.get_at((x, y))[:3]

        # Check original target color
        if currentColor != targetColor:
            continue

        # Avoid filling the same color again
        if currentColor == newColor:
            continue

        # Replace target color with new color
        surface.set_at((x, y), newColor)

        # Recursive calls (reverse push order)
        stack.append((x, y - 1))
        stack.append((x, y + 1))
        stack.append((x - 1, y))
        stack.append((x + 1, y))

        # Yield for animation
        yield


# ==========================================
# 2. BOUNDARY FILL ALGORITHM
# ==========================================

def boundary_fill(surface, x, y, newColor, boundaryColor):

    width, height = surface.get_size()

    # Stack to simulate recursive calls
    stack = [(x, y)]

    while stack:

        x, y = stack.pop()

        # Check whether pixel is out of bounds
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        currentColor = surface.get_at((x, y))[:3]

        # Stop at boundary color
        if currentColor == boundaryColor:
            continue

        # Avoid filling the same color again
        if currentColor == newColor:
            continue

        # Fill pixel with new color
        surface.set_at((x, y), newColor)

        # Recursive calls (reverse push order)
        stack.append((x, y - 1))
        stack.append((x, y + 1))
        stack.append((x - 1, y))
        stack.append((x + 1, y))

        # Yield for animation
        yield


# ==========================================
# CREATE ANIMATIONS
# ==========================================

# Flood Fill:
# Seed point = (180, 140)
# Target color = WHITE
# New color = BLUE

flood_animation = flood_fill(
    flood_surface,
    180, 140,
    BLUE,
    WHITE
)

# Boundary Fill:
# Seed point = (180, 140)
# Boundary color = BLACK
# New color = GREEN

boundary_animation = boundary_fill(
    boundary_surface,
    180, 140,
    GREEN,
    BLACK
)

# Animation status
flood_done = False
boundary_done = False

# Pixels processed per frame
PIXELS_PER_FRAME = 100

clock = pygame.time.Clock()

# ==========================================
# MAIN ANIMATION LOOP
# ==========================================

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Animate Flood Fill
    if not flood_done:

        for i in range(PIXELS_PER_FRAME):

            try:
                next(flood_animation)

            except StopIteration:
                flood_done = True
                break

    # Animate Boundary Fill
    if not boundary_done:

        for i in range(PIXELS_PER_FRAME):

            try:
                next(boundary_animation)

            except StopIteration:
                boundary_done = True
                break

    # Clear screen
    screen.fill(GRAY)

    # Main heading
    heading = title_font.render(
        "Flood Fill vs Boundary Fill",
        True,
        BLACK
    )

    screen.blit(heading, (330, 25))

    # Algorithm headings
    text1 = font.render(
        "1. FLOOD FILL ALGORITHM",
        True,
        BLUE
    )

    text2 = font.render(
        "2. BOUNDARY FILL ALGORITHM",
        True,
        GREEN
    )

    screen.blit(text1, (100, 85))
    screen.blit(text2, (560, 85))

    # Display both surfaces
    screen.blit(flood_surface, (80, 130))
    screen.blit(boundary_surface, (540, 130))

    # Display seed points
    seed1 = small_font.render(
        "Seed Point: (180, 140)",
        True,
        BLACK
    )

    seed2 = small_font.render(
        "Seed Point: (180, 140)",
        True,
        BLACK
    )

    screen.blit(seed1, (80, 425))
    screen.blit(seed2, (540, 425))

    # Display animation status
    status1 = (
        "Completed" if flood_done else "Filling..."
    )

    status2 = (
        "Completed" if boundary_done else "Filling..."
    )

    screen.blit(
        font.render("Status: " + status1, True, BLUE),
        (80, 455)
    )

    screen.blit(
        font.render("Status: " + status2, True, GREEN),
        (540, 455)
    )

    # Display explanation
    info1 = small_font.render(
        "Replaces connected WHITE pixels with BLUE.",
        True,
        BLACK
    )

    info2 = small_font.render(
        "Stops filling when BLACK boundary is reached.",
        True,
        BLACK
    )

    screen.blit(info1, (80, 490))
    screen.blit(info2, (540, 490))

    # Update display
    pygame.display.flip()

    # Control animation speed
    clock.tick(60)


# Quit Pygame
pygame.quit()
sys.exit()
