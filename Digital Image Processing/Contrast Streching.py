import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found!")
    exit()

# Find minimum and maximum intensity
r_min = np.min(image)
r_max = np.max(image)

# Apply Contrast Stretching
if r_max == r_min:
    stretched = image.copy()
else:
    stretched = ((image - r_min) / (r_max - r_min) * 255)
    stretched = stretched.astype(np.uint8)

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(stretched, cmap="gray")
plt.title("Contrast Stretched Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("contrast_stretched.jpg", stretched)
