import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("Rose.jpg")

# Check if image is loaded successfully
if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create figure
plt.figure(figsize=(12, 10))

# Display original image
plt.subplot(3, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

# Extract and display all 8 bit planes
for i in range(8):
    bit_plane = (gray >> i) & 1

    # Convert binary values (0 and 1) to visible values (0 and 255)
    bit_plane = bit_plane * 255

    plt.subplot(3, 3, i + 2)
    plt.imshow(bit_plane, cmap='gray', vmin=0, vmax=255)
    plt.title(f"Bit Plane {i}")
    plt.axis("off")

plt.tight_layout()
plt.show()
