import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found!")
    exit()

# Threshold value
T = 127

# Apply thresholding
thresholded = np.where(image >= T, 255, 0).astype(np.uint8)

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(thresholded, cmap="gray")
plt.title("Thresholded Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("thresholded_image.jpg", thresholded)
