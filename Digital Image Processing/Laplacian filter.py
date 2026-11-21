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

# Define Laplacian kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
], dtype=np.float32)

# Apply Laplacian filter
laplacian = cv2.filter2D(gray, cv2.CV_32F, kernel)

# Convert result to displayable image
laplacian_display = cv2.convertScaleAbs(laplacian)

# Sharpen image using Laplacian
sharpened = cv2.addWeighted(
    gray, 1.0,
    laplacian_display, 1.0,
    0
)

# Display images
plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(laplacian_display, cmap="gray")
plt.title("Laplacian Filter")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(sharpened, cmap="gray")
plt.title("Sharpened Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save outputs
cv2.imwrite("laplacian_edges.jpg", laplacian_display)
cv2.imwrite("laplacian_sharpened.jpg", sharpened)
