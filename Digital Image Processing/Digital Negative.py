import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found!")
    exit()

# Digital Negative
negative = 255 - image

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(negative, cmap="gray")
plt.title("Digital Negative")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("digital_negative.jpg", negative)
