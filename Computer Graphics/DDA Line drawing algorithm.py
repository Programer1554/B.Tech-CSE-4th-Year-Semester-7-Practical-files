import matplotlib.pyplot as plt

# DDA Line Drawing Algorithm
def dda_line(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    points = []

    for i in range(steps + 1):

        points.append((round(x), round(y)))

        x += x_increment
        y += y_increment

    return points

# Input coordinates
x1 = int(input("Enter starting X coordinate: "))
y1 = int(input("Enter starting Y coordinate: "))

x2 = int(input("Enter ending X coordinate: "))
y2 = int(input("Enter ending Y coordinate: "))

# Calculate points using DDA
points = dda_line(x1, y1, x2, y2)

# Extract X and Y coordinates
x_points = [point[0] for point in points]
y_points = [point[1] for point in points]

# Graphic visualization
plt.figure(figsize=(8, 8))

# Draw grid
plt.grid(True, linestyle="--", alpha=0.6)

# Plot the line pixels
plt.scatter(x_points, y_points, color="blue", s=100, label="DDA Pixels")

# Connect pixels to show the line
plt.plot(x_points, y_points, color="red", linewidth=1.5)

# Mark starting and ending points
plt.scatter(x1, y1, color="green", s=150, label="Starting Point")
plt.scatter(x2, y2, color="orange", s=150, label="Ending Point")

# Display coordinate labels
for x, y in points:
    plt.text(x + 0.1, y + 0.1, f"({x},{y})", fontsize=8)

# Graph settings
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.xticks(range(min(x_points) - 1, max(x_points) + 2))
plt.yticks(range(min(y_points) - 1, max(y_points) + 2))

plt.xlim(min(x_points) - 1, max(x_points) + 1)
plt.ylim(min(y_points) - 1, max(y_points) + 1)

plt.axis("equal")
plt.legend()
plt.show()


# Display calculated points
print("\nPoints generated using DDA algorithm:")
for point in points:
    print(point)
