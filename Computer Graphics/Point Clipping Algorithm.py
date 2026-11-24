import matplotlib.pyplot as plt

# Point Clipping Algorithm
def point_clipping(points, xmin, ymin, xmax, ymax):

    accepted = []
    rejected = []

    for point in points:

        x, y = point

        # Check whether point is inside clipping window
        if (xmin <= x <= xmax and
                ymin <= y <= ymax):

            accepted.append(point)
            print(f"Point {point} : ACCEPTED")

        else:

            rejected.append(point)
            print(f"Point {point} : REJECTED")

    return accepted, rejected


# Input number of points
n = int(input("Enter number of points: "))

points = []

# Input coordinates
print("\nENTER POINT COORDINATES")

for i in range(n):

    print(f"\nPoint {i + 1}:")

    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    points.append((x, y))


# Input clipping window
print("\nENTER CLIPPING WINDOW")

xmin = float(input("Enter minimum X: "))
ymin = float(input("Enter minimum Y: "))

xmax = float(input("Enter maximum X: "))
ymax = float(input("Enter maximum Y: "))


# Validate clipping window
if xmin >= xmax or ymin >= ymax:
    raise ValueError("Invalid clipping window!")


# Apply Point Clipping Algorithm
print("\nPOINT CLIPPING RESULTS")

accepted, rejected = point_clipping(
    points, xmin, ymin, xmax, ymax
)


# Graphic Visualization
plt.figure(figsize=(9, 8))

# Draw clipping window
window_x = [xmin, xmax, xmax, xmin, xmin]
window_y = [ymin, ymin, ymax, ymax, ymin]

plt.plot(
    window_x, window_y,
    color="green",
    linewidth=2,
    label="Clipping Window"
)

# Plot accepted points
if accepted:

    ax, ay = zip(*accepted)

    plt.scatter(
        ax, ay,
        color="green",
        s=100,
        marker="o",
        label="Accepted Points"
    )

# Plot rejected points
if rejected:

    rx, ry = zip(*rejected)

    plt.scatter(
        rx, ry,
        color="red",
        s=100,
        marker="x",
        label="Rejected Points"
    )

# Label all points
for x, y in points:

    plt.text(
        x + 0.15,
        y + 0.15,
        f"({x},{y})",
        fontsize=9
    )


# Graph settings
plt.title("Point Clipping Algorithm")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)

plt.grid(True, linestyle="--", alpha=0.6)

plt.axis("equal")
plt.legend()

plt.show()


# Display final results
print("\nACCEPTED POINTS:")
for point in accepted:
    print(point)

print("\nREJECTED POINTS:")
for point in rejected:
    print(point)
