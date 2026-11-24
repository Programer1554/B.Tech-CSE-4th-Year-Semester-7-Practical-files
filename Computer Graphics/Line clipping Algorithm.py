import matplotlib.pyplot as plt

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


# Calculate region code
def compute_code(x, y, xmin, ymin, xmax, ymax):

    code = INSIDE

    if x < xmin:
        code |= LEFT

    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM

    elif y > ymax:
        code |= TOP

    return code


# Cohen-Sutherland Line Clipping Algorithm
def cohen_sutherland(x1, y1, x2, y2,
                     xmin, ymin, xmax, ymax):

    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    print("\nInitial Region Codes:")
    print("First Endpoint:", format(code1, '04b'))
    print("Second Endpoint:", format(code2, '04b'))

    while True:

        # Both endpoints are inside
        if code1 == 0 and code2 == 0:

            print("\nLine Accepted!")
            return x1, y1, x2, y2

        # Both endpoints lie outside in a common region
        elif code1 & code2:

            print("\nLine Rejected!")
            return None

        else:

            # Select an outside endpoint
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Calculate intersection point
            if code_out & TOP:

                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            elif code_out & BOTTOM:

                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin

            elif code_out & RIGHT:

                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            elif code_out & LEFT:

                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Replace outside endpoint
            if code_out == code1:

                x1, y1 = x, y
                code1 = compute_code(
                    x1, y1, xmin, ymin, xmax, ymax
                )

            else:

                x2, y2 = x, y
                code2 = compute_code(
                    x2, y2, xmin, ymin, xmax, ymax
                )


# Input line coordinates
print("ENTER LINE COORDINATES")

x1 = float(input("Enter X1: "))
y1 = float(input("Enter Y1: "))

x2 = float(input("Enter X2: "))
y2 = float(input("Enter Y2: "))


# Input clipping window
print("\nENTER CLIPPING WINDOW")

xmin = float(input("Enter minimum X: "))
ymin = float(input("Enter minimum Y: "))

xmax = float(input("Enter maximum X: "))
ymax = float(input("Enter maximum Y: "))


# Validate clipping window
if xmin >= xmax or ymin >= ymax:
    raise ValueError("Invalid clipping window!")

# Apply clipping algorithm
result = cohen_sutherland(
    x1, y1, x2, y2,
    xmin, ymin, xmax, ymax
)


# Graphic visualization
plt.figure(figsize=(9, 8))

# Draw clipping window
window_x = [xmin, xmax, xmax, xmin, xmin]
window_y = [ymin, ymin, ymax, ymax, ymin]

plt.plot(window_x, window_y, 'g-', linewidth=2,
         label="Clipping Window")

# Draw original line
plt.plot([x1, x2], [y1, y2],
         'b--', linewidth=2,
         label="Original Line")

plt.scatter([x1, x2], [y1, y2],
            color="blue", s=60)

# Draw clipped line if accepted
if result is not None:

    cx1, cy1, cx2, cy2 = result

    plt.plot([cx1, cx2], [cy1, cy2],
             'r-', linewidth=3,
             label="Clipped Line")

    plt.scatter([cx1, cx2], [cy1, cy2],
                color="red", s=80)

    print("\nClipped Line Coordinates:")
    print("Starting Point:", (round(cx1, 2), round(cy1, 2)))
    print("Ending Point:", (round(cx2, 2), round(cy2, 2)))

else:

    print("No portion of the line is visible.")

# Graph settings
plt.title("Cohen-Sutherland Line Clipping Algorithm")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)

plt.grid(True, linestyle="--", alpha=0.5)
plt.axis("equal")
plt.legend()

plt.show()
