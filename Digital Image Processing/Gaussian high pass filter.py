import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("Rose.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found!")
    exit()

# Fourier Transform
F = np.fft.fft2(image)
F_shift = np.fft.fftshift(F)

# Image dimensions
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

# Distance matrix
u = np.arange(rows) - crow
v = np.arange(cols) - ccol
U, V = np.meshgrid(v, u)

D = np.sqrt(U**2 + V**2)

# Cutoff frequency
D0 = 50

# Gaussian High-Pass Filter
H = 1 - np.exp(-(D**2) / (2 * D0**2))

# Apply filter
G_shift = F_shift * H

# Inverse Fourier Transform
G = np.fft.ifftshift(G_shift)
filtered = np.abs(np.fft.ifft2(G))

# Frequency spectrum
spectrum = np.log(1 + np.abs(F_shift))

# Display
plt.figure(figsize=(12, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(spectrum, cmap="gray")
plt.title("Frequency Spectrum")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(H, cmap="gray")
plt.title("GHPF Mask")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(filtered, cmap="gray")
plt.title("Gaussian High-Pass")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save result
cv2.imwrite("gaussian_high_pass.jpg",
            np.uint8(np.clip(filtered, 0, 255)))
