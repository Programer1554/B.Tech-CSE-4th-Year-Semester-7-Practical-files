import matplotlib.pyplot as plt
import numpy as np

# Function to select shape and input coordinates
def get_shape():

    print("\nSELECT SHAPE")
    print("1. Triangle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Pentagon")
    print("5. Custom Polygon")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = 3
        shape = "Triangle"

    elif choice == 2:
        n = 4
        shape = "Square"

    elif choice == 3:
        n = 4
        shape = "Rectangle"

    elif choice == 4:
        n = 5
        shape = "Pentagon"

    elif choice == 5:
        n = int(input("Enter number of vertices: "))

        if n < 3:
            print("A polygon must have at least 3 vertices.")
            return get_shape()

        shape = "Custom Polygon"

    else:
        print("Invalid choice!")
        return get_shape()

    points = []

    print(f"\nEnter coordinates for {shape}:")

    for i in range(n):
        print(f"\nVertex {i + 1}:")
        x = float(input("Enter X coordinate: "))
        y = float(input("Enter Y coordinate: "))

        points.append([x, y])

    return np.array(points), shape


# Translation
def translation(points, tx, ty):

    matrix = np.array([
        [1, 0],
        [0, 1]
    ])

    return np.dot(points, matrix.T) + [tx, ty]


# Scaling
def scaling(points, sx, sy):

    matrix = np.array([
        [sx, 0],
        [0, sy]
    ])

    return np.dot(points, matrix.T)


# Rotation
def rotation(points, angle):

    theta = np.radians(angle)

    matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

    return np.dot(points, matrix.T)


# Reflection
def reflection(points, choice):

    if choice == 1:
        matrix = [[1, 0], [0, -1]]
        name = "X-axis"

    elif choice == 2:
        matrix = [[-1, 0], [0, 1]]
        name = "Y-axis"

    elif choice == 3:
        matrix = [[-1, 0], [0, -1]]
        name = "Origin"

    elif choice == 4:
        matrix = [[0, 1], [1, 0]]
        name = "Y = X"

    else:
        print("Invalid reflection choice!")
        return points, "None"

    return np.dot(points, np.array(matrix).T), name


# Shearing
def shearing(points, shx, shy):

    matrix = np.array([
        [1, shx],
        [shy, 1]
    ])

    return np.dot(points, matrix.T)


# Display transformation
def visualize(original, transformed, shape, operation):

    # Close polygons
    original_closed = np.vstack([original, original[0]])
    transformed_closed = np.vstack([transformed, transformed[0]])

    plt.figure(figsize=(10, 8))

    # Original shape
    plt.plot(
        original_closed[:, 0],
        original_closed[:, 1],
        'bo-', linewidth=2,
        label="Original Shape"
    )

    # Transformed shape
    plt.plot(
        transformed_closed[:, 0],
        transformed_closed[:, 1],
        'ro-', linewidth=2,
        label="Transformed Shape"
    )

    # Mark vertices
    plt.scatter(original[:, 0], original[:, 1],
                color="blue", s=70)

    plt.scatter(transformed[:, 0], transformed[:, 1],
                color="red", s=70)

    # Label transformed coordinates
    for i, (x, y) in enumerate(transformed):
        plt.text(x, y, f" P{i+1}({x:.1f},{y:.1f})")

    # Coordinate axes
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)

    plt.grid(True, linestyle="--", alpha=0.6)

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    plt.title(f"{shape} - {operation}")

    plt.legend()
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


# Main Program
print("================================")
print("       2D TRANSFORMATIONS")
print("================================")

# Get custom shape
points, shape = get_shape()

print("\nOriginal Coordinates:")
print(points)

# Transformation menu
print("\nSELECT TRANSFORMATION")
print("1. Translation")
print("2. Scaling")
print("3. Rotation")
print("4. Reflection")
print("5. Shearing")

choice = int(input("\nEnter your choice: "))

operation = ""

if choice == 1:

    tx = float(input("Enter Tx: "))
    ty = float(input("Enter Ty: "))

    new_points = translation(points, tx, ty)
    operation = "Translation"

elif choice == 2:

    sx = float(input("Enter Sx: "))
    sy = float(input("Enter Sy: "))

    new_points = scaling(points, sx, sy)
    operation = "Scaling"

elif choice == 3:

    angle = float(input("Enter rotation angle: "))

    new_points = rotation(points, angle)
    operation = "Rotation"

elif choice == 4:

    print("\nREFLECTION OPTIONS")
    print("1. X-axis")
    print("2. Y-axis")
    print("3. Origin")
    print("4. Y = X")

    ref = int(input("Enter reflection choice: "))

    new_points, axis = reflection(points, ref)
    operation = "Reflection about " + axis

elif choice == 5:

    print("\nEnter Shearing Factors")

    shx = float(input("Enter X-shear factor: "))
    shy = float(input("Enter Y-shear factor: "))

    new_points = shearing(points, shx, shy)
    operation = "Shearing"

else:

    print("Invalid transformation choice!")
    exit()


# Display transformed coordinates
print("\nOriginal Coordinates:")
print(points)

print("\nTransformed Coordinates:")
print(np.round(new_points, 2))


# Visualize both shapes
visualize(points, new_points, shape, operation)
