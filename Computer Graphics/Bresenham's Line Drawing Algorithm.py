import matplotlib.pyplot as plt

# Bresenham's Line Drawing Algorithm
def bresenham_line(x1, y1, x2, y2):

    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    error = dx - dy

    x, y = x1, y1

    while True:

        points.append((x, y))

        # Stop when the endpoint is reached
        if x == x2 and y == y2:
            break

        e2 = 2 * error

        if e2 > -dy:
            error -= dy
            x += sx

        if e2 < dx:
            error += dx
            y += sy

    return points


# Input coordinates
x1 = int(input("Enter starting X coordinate: "))
y1 = int(input("Enter starting Y coordinate: "))

x2 = int(input("Enter ending X coordinate: "))
y2 = int(input("Enter ending Y coordinate: "))


# Calculate points
points = bresenham_line(x1, y1, x2, y2)

# Extract coordinates
x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

# Graphic visualization
plt.figure(figsize=(8, 8))

# Draw grid
plt.grid(True, linestyle="--", alpha=0.6)

# Plot pixels
plt.scatter(x_points, y_points, color="blue", s=120, marker="s", label="Bresenham Pixels")

# Connect pixels
plt.plot(x_points, y_points, color="red", linewidth=1.5, label="Line")

# Mark endpoints
plt.scatter(x1, y1, color="green", s=150, label="Starting Point")

plt.scatter(x2, y2, color="orange", s=150, label="Ending Point")

# Display coordinates
for x, y in points:
    plt.text(x + 0.15, y + 0.15, f"({x},{y})", fontsize=8)

# Graph settings
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.xticks(range(min(x_points) - 1, max(x_points) + 2))
plt.yticks(range(min(y_points) - 1, max(y_points) + 2))
plt.xlim(min(x_points) - 1, max(x_points) + 1)
plt.ylim(min(y_points) - 1, max(y_points) + 1)
plt.axis("equal")
plt.legend()
plt.show()

# Display generated points
print("\nPoints generated using Bresenham's Algorithm:")
for point in points:
    print(point)
