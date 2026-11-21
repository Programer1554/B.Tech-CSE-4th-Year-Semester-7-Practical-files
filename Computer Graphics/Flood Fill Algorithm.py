import matplotlib.pyplot as plt
import numpy as np

# Flood Fill Algorithm (4-connected)
def flood_fill(canvas, x, y, target_color, fill_color):

    height, width, _ = canvas.shape

    stack = [(x, y)]

    while stack:

        x, y = stack.pop()

        # Check canvas boundaries
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        # Check if pixel matches target color
        if not np.array_equal(canvas[y, x], target_color):
            continue

        # Fill the current pixel
        canvas[y, x] = fill_color

        # Add 4-connected neighboring pixels
        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))


# Canvas dimensions
width = 30
height = 20

# Create white canvas
canvas = np.ones((height, width, 3), dtype=np.uint8) * 255

# Define colors
boundary_color = np.array([0, 0, 0], dtype=np.uint8)
fill_color = np.array([0, 150, 255], dtype=np.uint8)

# Input rectangle coordinates
x1 = int(input("Enter left boundary X: "))
y1 = int(input("Enter bottom boundary Y: "))
x2 = int(input("Enter right boundary X: "))
y2 = int(input("Enter top boundary Y: "))

# Input seed point
seed_x = int(input("Enter seed point X: "))
seed_y = int(input("Enter seed point Y: "))

# Draw rectangular boundary
canvas[y1, x1:x2 + 1] = boundary_color
canvas[y2, x1:x2 + 1] = boundary_color

canvas[y1:y2 + 1, x1] = boundary_color
canvas[y1:y2 + 1, x2] = boundary_color

# Get original color of seed point
target_color = canvas[seed_y, seed_x].copy()

# Apply Flood Fill Algorithm
if np.array_equal(target_color, boundary_color):
    print("Seed point is on the boundary. Choose another point.")

else:
    flood_fill(
        canvas,
        seed_x,
        seed_y,
        target_color,
        fill_color
    )

    print("Flood Fill completed successfully!")

    # Graphic visualization
    plt.figure(figsize=(10, 7))

    plt.imshow(canvas, origin="lower")

    # Display grid
    plt.xticks(range(width))
    plt.yticks(range(height))

    plt.grid(True, color="gray", linestyle="-", linewidth=0.5)

    # Mark seed point
    plt.scatter(seed_x, seed_y, color="red",
                marker="x", s=100, label="Seed Point")

    plt.title("4-Connected Flood Fill Algorithm")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    plt.legend()
    plt.show()
