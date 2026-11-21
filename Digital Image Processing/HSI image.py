import numpy as np
from PIL import Image


def hsi_to_rgb(h, s, i):
    """
    Convert HSI values to RGB.
    h: hue in degrees [0, 360)
    s: saturation in [0, 1]
    i: intensity in [0, 1]
    Returns (r, g, b) each in [0, 1].
    """
    h = h % 360
    h_rad = np.deg2rad(h)

    if 0 <= h < 120:
        b = i * (1 - s)
        r = i * (1 + (s * np.cos(h_rad)) / np.cos(np.deg2rad(60) - h_rad))
        g = 3 * i - (r + b)
    elif 120 <= h < 240:
        h_rad -= np.deg2rad(120)
        r = i * (1 - s)
        g = i * (1 + (s * np.cos(h_rad)) / np.cos(np.deg2rad(60) - h_rad))
        b = 3 * i - (r + g)
    else:
        h_rad -= np.deg2rad(240)
        g = i * (1 - s)
        b = i * (1 + (s * np.cos(h_rad)) / np.cos(np.deg2rad(60) - h_rad))
        r = 3 * i - (g + b)

    return np.clip(r, 0, 1), np.clip(g, 0, 1), np.clip(b, 0, 1)


def create_hsi_image(width=512, height=512, intensity=0.5, output_path="hsi_image.png"):
    """
    Create an HSI color image:
      - Hue varies left to right (0° to 360°)
      - Saturation varies top to bottom (0 to 1)
      - Intensity is constant
    """
    img = np.zeros((height, width, 3), dtype=np.float64)

    for y in range(height):
        s = y / (height - 1)  # saturation from 0 (top) to 1 (bottom)
        for x in range(width):
            h = (x / width) * 360  # hue from 0 to 360 degrees
            r, g, b = hsi_to_rgb(h, s, intensity)
            img[y, x] = [r, g, b]

    img_uint8 = (img * 255).astype(np.uint8)
    Image.fromarray(img_uint8, mode="RGB").save(output_path)
    print(f"HSI image saved to {output_path}")
    return img_uint8


if __name__ == "__main__":
    create_hsi_image(width=512, height=512, intensity=0.5, output_path="hsi_image.png")
