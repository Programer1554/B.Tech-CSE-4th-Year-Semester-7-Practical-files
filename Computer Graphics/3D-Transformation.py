import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# ==========================================
# 1. SHAPE SELECTION AND COORDINATES
# ==========================================

def get_shape():

    print("\n========== SELECT 3D SHAPE ==========")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Tetrahedron")
    print("4. Square Pyramid")
    print("5. Custom 3D Shape")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        shape = "Cube"

        points = [
            [-1, -1, -1], [1, -1, -1],
            [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1],
            [1, 1, 1], [-1, 1, 1]
        ]

        faces = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [1, 2, 6, 5],
            [0, 3, 7, 4]
        ]

    elif choice == 2:
        shape = "Cuboid"

        points = [
            [-2, -1, -1], [2, -1, -1],
            [2, 1, -1], [-2, 1, -1],
            [-2, -1, 1], [2, -1, 1],
            [2, 1, 1], [-2, 1, 1]
        ]

        faces = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [1, 2, 6, 5],
            [0, 3, 7, 4]
        ]

    elif choice == 3:
        shape = "Tetrahedron"

        points = [
            [1, 1, 1],
            [-1, -1, 1],
            [-1, 1, -1],
            [1, -1, -1]
        ]

        faces = [
            [0, 1, 2],
            [0, 1, 3],
            [0, 2, 3],
            [1, 2, 3]
        ]

    elif choice == 4:
        shape = "Square Pyramid"

        points = [
            [-1, -1, 0],
            [1, -1, 0],
            [1, 1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]

        faces = [
            [0, 1, 2, 3],
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4]
        ]

    elif choice == 5:
        shape = "Custom 3D Shape"

        n = int(input("\nEnter number of vertices: "))

        if n < 4:
            raise ValueError("A 3D solid requires at least 4 vertices.")

        points = []

        print("\nEnter coordinates for each vertex:")

        for i in range(n):

            print(f"\nVertex {i + 1}")

            x = float(input("Enter X coordinate: "))
            y = float(input("Enter Y coordinate: "))
            z = float(input("Enter Z coordinate: "))

            points.append([x, y, z])

        # Face connectivity
        nf = int(input("\nEnter number of faces: "))

        if nf < 1:
            raise ValueError("Enter at least one face.")

        faces = []

        print("\nEnter vertex numbers for each face.")
        print("Example: 1 2 3 4")
        print("Use the vertex numbers entered above.")

        for i in range(nf):

            face = list(map(
                int,
                input(f"Face {i + 1}: ").split()
            ))

            if len(face) < 3:
                raise ValueError("Each face requires at least 3 vertices.")

            if any(v < 1 or v > n for v in face):
                raise ValueError("Invalid vertex number!")

            faces.append([v - 1 for v in face])

    else:
        raise ValueError("Invalid shape choice!")

    return np.array(points, dtype=float), faces, shape


# ==========================================
# 2. TRANSLATION
# ==========================================

def translation(points, tx, ty, tz):

    matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

    homogeneous = np.c_[points, np.ones(len(points))]

    return (homogeneous @ matrix.T)[:, :3]


# ==========================================
# 3. SCALING
# ==========================================

def scaling(points, sx, sy, sz):

    matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, sz]
    ])

    return points @ matrix.T


# ==========================================
# 4. ROTATION
# ==========================================

def rotation(points, angle, axis):

    theta = np.radians(angle)

    c = np.cos(theta)
    s = np.sin(theta)

    if axis == 1:  # X-axis

        matrix = np.array([
            [1, 0, 0],
            [0, c, -s],
            [0, s, c]
        ])

    elif axis == 2:  # Y-axis

        matrix = np.array([
            [c, 0, s],
            [0, 1, 0],
            [-s, 0, c]
        ])

    elif axis == 3:  # Z-axis

        matrix = np.array([
            [c, -s, 0],
            [s, c, 0],
            [0, 0, 1]
        ])

    else:
        raise ValueError("Invalid rotation axis!")

    return points @ matrix.T


# ==========================================
# 5. REFLECTION
# ==========================================

def reflection(points, choice):

    if choice == 1:       # XY plane

        matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, -1]
        ]

        name = "XY Plane"

    elif choice == 2:     # YZ plane

        matrix = [
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]

        name = "YZ Plane"

    elif choice == 3:     # XZ plane

        matrix = [
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ]

        name = "XZ Plane"

    elif choice == 4:     # Origin

        matrix = [
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, -1]
        ]

        name = "Origin"

    else:
        raise ValueError("Invalid reflection choice!")

    return points @ np.array(matrix).T, name


# ==========================================
# 6. SHEARING
# ==========================================

def shearing(points, shxy, shxz, shyx,
             shyz, shzx, shzy):

    matrix = np.array([
        [1, shxy, shxz],
        [shyx, 1, shyz],
        [shzx, shzy, 1]
    ])

    return points @ matrix.T


# ==========================================
# 7. 3D VISUALIZATION
# ==========================================

def visualize(original, transformed, faces,
              shape, operation):

    fig = plt.figure(figsize=(11, 8))

    ax = fig.add_subplot(111, projection='3d')

    # Create original and transformed faces

    original_faces = [
        original[face] for face in faces
    ]

    transformed_faces = [
        transformed[face] for face in faces
    ]

    # Draw original shape

    original_collection = Poly3DCollection(
        original_faces,
        facecolors='blue',
        edgecolors='black',
        alpha=0.25,
        linewidths=1.5
    )

    ax.add_collection3d(original_collection)

    # Draw transformed shape

    transformed_collection = Poly3DCollection(
        transformed_faces,
        facecolors='orange',
        edgecolors='red',
        alpha=0.35,
        linewidths=1.5
    )

    ax.add_collection3d(transformed_collection)

    # Plot original vertices

    ax.scatter(
        original[:, 0],
        original[:, 1],
        original[:, 2],
        color='blue',
        s=40,
        label='Original Vertices'
    )

    # Plot transformed vertices

    ax.scatter(
        transformed[:, 0],
        transformed[:, 1],
        transformed[:, 2],
        color='red',
        s=40,
        label='Transformed Vertices'
    )

    # Label transformed vertices

    for i, (x, y, z) in enumerate(transformed):

        ax.text(
            x, y, z,
            f"P{i+1}",
            color='red',
            fontsize=8
        )

    # Calculate equal axis limits

    all_points = np.vstack([original, transformed])

    minimum = all_points.min(axis=0)
    maximum = all_points.max(axis=0)

    center = (minimum + maximum) / 2

    radius = max(np.max(maximum - minimum) / 2, 1)

    ax.set_xlim(center[0] - radius, center[0] + radius)
    ax.set_ylim(center[1] - radius, center[1] + radius)
    ax.set_zlim(center[2] - radius, center[2] + radius)

    ax.set_box_aspect((1, 1, 1))

    # Axis labels

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")

    ax.set_title(f"{shape} - {operation}")

    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.show()


# ==========================================
# 8. MAIN PROGRAM
# ==========================================

print("====================================")
print("       3D TRANSFORMATIONS")
print("====================================")

# Select shape and coordinates

points, faces, shape = get_shape()

print("\nOriginal Coordinates:")
print(points)

# Select transformation

print("\n========== SELECT TRANSFORMATION ==========")

print("1. Translation")
print("2. Scaling")
print("3. Rotation")
print("4. Reflection")
print("5. Shearing")

choice = int(input("\nEnter your choice: "))

operation = ""

# ==========================================
# TRANSLATION
# ==========================================

if choice == 1:

    print("\n========== TRANSLATION ==========")

    tx = float(input("Enter Tx: "))
    ty = float(input("Enter Ty: "))
    tz = float(input("Enter Tz: "))

    new_points = translation(points, tx, ty, tz)

    operation = "Translation"


# ==========================================
# SCALING
# ==========================================

elif choice == 2:

    print("\n========== SCALING ==========")

    sx = float(input("Enter Sx: "))
    sy = float(input("Enter Sy: "))
    sz = float(input("Enter Sz: "))

    new_points = scaling(points, sx, sy, sz)

    operation = "Scaling"


# ==========================================
# ROTATION
# ==========================================

elif choice == 3:

    print("\n========== ROTATION ==========")

    print("1. X-axis")
    print("2. Y-axis")
    print("3. Z-axis")

    axis = int(input("Select rotation axis: "))

    if axis not in [1, 2, 3]:
        raise ValueError("Invalid rotation axis!")

    angle = float(input("Enter rotation angle: "))

    new_points = rotation(points, angle, axis)

    axis_name = ["", "X-axis", "Y-axis", "Z-axis"][axis]

    operation = f"Rotation around {axis_name}"


# ==========================================
# REFLECTION
# ==========================================

elif choice == 4:

    print("\n========== REFLECTION ==========")

    print("1. XY Plane")
    print("2. YZ Plane")
    print("3. XZ Plane")
    print("4. Origin")

    ref = int(input("Enter reflection choice: "))

    new_points, plane = reflection(points, ref)

    operation = f"Reflection about {plane}"


# ==========================================
# SHEARING
# ==========================================

elif choice == 5:

    print("\n========== SHEARING ==========")

    shxy = float(input("Enter XY shear factor: "))
    shxz = float(input("Enter XZ shear factor: "))

    shyx = float(input("Enter YX shear factor: "))
    shyz = float(input("Enter YZ shear factor: "))

    shzx = float(input("Enter ZX shear factor: "))
    shzy = float(input("Enter ZY shear factor: "))

    new_points = shearing(
        points,
        shxy, shxz,
        shyx, shyz,
        shzx, shzy
    )

    operation = "Shearing"


else:

    raise ValueError("Invalid transformation choice!")


# ==========================================
# 9. DISPLAY RESULTS
# ==========================================

print("\n========== RESULTS ==========")

print("\nOriginal Coordinates:")
print(points)

print("\nTransformed Coordinates:")
print(np.round(new_points, 2))


# ==========================================
# 10. GRAPHICAL VISUALIZATION
# ==========================================

visualize(
    points,
    new_points,
    faces,
    shape,
    operation
)
