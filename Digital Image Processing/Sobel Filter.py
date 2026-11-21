import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg")

if image is None:
    print("Image not found!")
    exit()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Apply Sobel filters
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculate gradient magnitude
magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Normalize to 0-255
magnitude = cv2.normalize(
    magnitude, None, 0, 255,
    cv2.NORM_MINMAX
)

magnitude = magnitude.astype(np.uint8)

# Convert individual gradients to displayable format
sobel_x_display = cv2.convertScaleAbs(sobel_x)
sobel_y_display = cv2.convertScaleAbs(sobel_y)

# Display images
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(sobel_x_display, cmap="gray")
plt.title("Horizontal Sobel (Gx)")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(sobel_y_display, cmap="gray")
plt.title("Vertical Sobel (Gy)")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(magnitude, cmap="gray")
plt.title("Sobel Edge Magnitude")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save outputs
cv2.imwrite("sobel_x.jpg", sobel_x_display)
cv2.imwrite("sobel_y.jpg", sobel_y_display)
cv2.imwrite("sobel_edges.jpg", magnitude)
