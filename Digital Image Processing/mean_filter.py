import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Mean Filter
filtered = cv2.blur(image, (3, 3))

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtered)
plt.title("Mean Filter")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("mean_filtered.jpg",
            cv2.cvtColor(filtered, cv2.COLOR_RGB2BGR))
