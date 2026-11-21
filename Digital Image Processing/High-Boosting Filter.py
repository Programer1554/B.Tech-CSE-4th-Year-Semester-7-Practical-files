import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg")

if image is None:
    print("Image not found!")
    exit()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert image to float
image_float = image.astype(np.float32)

# Apply low-pass filter
blurred = cv2.GaussianBlur(image_float, (5, 5), 0)

# High-boost parameter
A = 1.5

# Apply High-Boost Filtering
high_boost = A * image_float - blurred

# Clip values to valid range
high_boost = np.clip(high_boost, 0, 255)

# Convert to uint8
high_boost = high_boost.astype(np.uint8)

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(high_boost)
plt.title("High-Boost Filter")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("high_boost_filtered.jpg",
            cv2.cvtColor(high_boost, cv2.COLOR_RGB2BGR))
