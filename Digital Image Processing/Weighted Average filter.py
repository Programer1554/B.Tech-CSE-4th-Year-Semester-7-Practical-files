import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg")

if image is None:
    print("Image not found!")
    exit()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define weighted average kernel
kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=np.float32) / 16

# Apply filter
filtered = cv2.filter2D(image, -1, kernel)

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtered)
plt.title("Weighted Average Filter")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("weighted_filtered.jpg",
            cv2.cvtColor(filtered, cv2.COLOR_RGB2BGR))
