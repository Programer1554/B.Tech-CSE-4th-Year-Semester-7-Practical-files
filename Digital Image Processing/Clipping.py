import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found!")
    exit()

# Define clipping range
L_min = 50
L_max = 200

# Apply clipping
clipped = np.clip(image, L_min, L_max)

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(clipped, cmap="gray")
plt.title("Clipped Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("clipped_image.jpg", clipped)
