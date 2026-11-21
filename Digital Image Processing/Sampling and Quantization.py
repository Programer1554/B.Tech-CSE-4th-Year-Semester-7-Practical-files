import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found!")
    exit()

# ---------------- Sampling ----------------

# Sampling factor
sampling_factor = 4

# Reduce image resolution
sampled = image[::sampling_factor, ::sampling_factor]

# Resize sampled image for display
sampled_display = cv2.resize(
    sampled,
    (image.shape[1], image.shape[0]),
    interpolation=cv2.INTER_NEAREST
)

# ---------------- Quantization ----------------

# Number of intensity levels
levels = 4

# Calculate quantization step
step = 256 // levels

# Apply quantization
quantized = (image // step) * step

# Convert to uint8
quantized = quantized.astype(np.uint8)

# ---------------- Display ----------------

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(sampled_display, cmap="gray")
plt.title("Sampling")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(quantized, cmap="gray")
plt.title("Quantization")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save outputs
cv2.imwrite("sampled_image.jpg", sampled_display)
cv2.imwrite("quantized_image.jpg", quantized)
