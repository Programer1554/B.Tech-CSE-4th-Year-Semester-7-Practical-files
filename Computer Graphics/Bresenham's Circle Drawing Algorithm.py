import matplotlib.pyplot as plt
import math

# Brute Force Circle Drawing Algorithm
def brute_force_circle(h, k, r):

    points = set()

    # Iterate through x coordinates
    for x in range(0, r + 1):

        # Calculate y using circle equation
        y = round(math.sqrt(r * r - x * x))

        # Generate eight symmetric points
        points.add((h + x, k + y))
        points.add((h - x, k + y))
        points.add((h + x, k - y))
        points.add((h - x, k - y))

        points.add((h + y, k + x))
        points.add((h - y, k + x))
        points.add((h + y, k - x))
        points.add((h - y, k - x))

    return sorted(points)


# Input center and radius
h = int(input("Enter center X coordinate: "))
k = int(input("Enter center Y coordinate: "))
r = int(input("Enter radius: "))

if r <= 0:
    print("Radius must be greater than zero.")

else:

    # Calculate circle points
    points = brute_force_circle(h, k, r)

    # Extract coordinates
    x_points = [p[0] for p in points]
    y_points = [p[1] for p in points]

    # Graphic visualization
    plt.figure(figsize=(8, 8))

    # Plot circle pixels
    plt.scatter(x_points, y_points, color="blue",
                s=80, marker="s", label="Circle Pixels")

    # Draw grid
    plt.grid(True, linestyle="--", alpha=0.6)

    # Mark center
    plt.scatter(h, k, color="red", s=150,
                label="Center")

    # Display pixel coordinates
    for x, y in points:
        plt.text(x + 0.1, y + 0.1,
                 f"({x},{y})", fontsize=7)

    # Graph settings
    plt.title("Brute Force Circle Drawing Algorithm")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    plt.xticks(range(h - r - 1, h + r + 2))
    plt.yticks(range(k - r - 1, k + r + 2))

    plt.xlim(h - r - 1, h + r + 1)
    plt.ylim(k - r - 1, k + r + 1)

    plt.axis("equal")
    plt.legend()

    plt.show()

    # Display calculated points
    print("\nPoints generated using Brute Force Algorithm:")

    for point in points:
        print(point)
