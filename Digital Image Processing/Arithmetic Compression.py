import cv2
import numpy as np
import matplotlib.pyplot as plt
import struct
import bisect

# -------------------------------
# Bit Writer
# -------------------------------
class BitWriter:
    def __init__(self):
        self.data = bytearray()
        self.current_byte = 0
        self.bits_filled = 0

    def write_bit(self, bit):
        self.current_byte = (self.current_byte << 1) | bit
        self.bits_filled += 1

        if self.bits_filled == 8:
            self.data.append(self.current_byte)
            self.current_byte = 0
            self.bits_filled = 0

    def finish(self):
        if self.bits_filled > 0:
            self.current_byte <<= (8 - self.bits_filled)
            self.data.append(self.current_byte)

        return bytes(self.data)


# -------------------------------
# Bit Reader
# -------------------------------
class BitReader:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def read_bit(self):
        byte_index = self.position // 8

        if byte_index >= len(self.data):
            self.position += 1
            return 0

        bit_index = 7 - (self.position % 8)
        bit = (self.data[byte_index] >> bit_index) & 1
        self.position += 1

        return bit


# -------------------------------
# Arithmetic Encoder
# -------------------------------
BITS = 32
MAX_VALUE = (1 << BITS) - 1
HALF = 1 << (BITS - 1)
QUARTER = 1 << (BITS - 2)
THREE_QUARTERS = 3 * QUARTER


def arithmetic_encode(data, cumulative):
    low = 0
    high = MAX_VALUE
    pending = 0

    writer = BitWriter()

    def output_bit(bit):
        nonlocal pending
        writer.write_bit(bit)

        for _ in range(pending):
            writer.write_bit(1 - bit)

        pending = 0

    total = cumulative[-1]

    for symbol in data:
        symbol = int(symbol)

        current_range = high - low + 1

        high = low + (
            current_range * cumulative[symbol + 1] // total
        ) - 1

        low = low + (
            current_range * cumulative[symbol] // total
        )

        while True:
            if high < HALF:
                output_bit(0)

            elif low >= HALF:
                output_bit(1)
                low -= HALF
                high -= HALF

            elif low >= QUARTER and high < THREE_QUARTERS:
                pending += 1
                low -= QUARTER
                high -= QUARTER

            else:
                break

            low = low << 1
            high = (high << 1) | 1

    pending += 1

    if low < QUARTER:
        output_bit(0)
    else:
        output_bit(1)

    return writer.finish()


# -------------------------------
# Arithmetic Decoder
# -------------------------------
def arithmetic_decode(encoded_data, cumulative, data_length):
    low = 0
    high = MAX_VALUE
    code = 0

    reader = BitReader(encoded_data)

    for _ in range(BITS):
        code = (code << 1) | reader.read_bit()

    total = cumulative[-1]
    decoded = []

    for _ in range(data_length):
        current_range = high - low + 1

        value = (
            ((code - low + 1) * total - 1) // current_range
        )

        symbol = bisect.bisect_right(cumulative, value) - 1
        decoded.append(symbol)

        high = low + (
            current_range * cumulative[symbol + 1] // total
        ) - 1

        low = low + (
            current_range * cumulative[symbol] // total
        )

        while True:
            if high < HALF:
                pass

            elif low >= HALF:
                low -= HALF
                high -= HALF
                code -= HALF

            elif low >= QUARTER and high < THREE_QUARTERS:
                low -= QUARTER
                high -= QUARTER
                code -= QUARTER

            else:
                break

            low = low << 1
            high = (high << 1) | 1
            code = (code << 1) | reader.read_bit()

    return np.array(decoded, dtype=np.uint8)


# -------------------------------
# Main Program
# -------------------------------

image = cv2.imread("Rose.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
    exit()

height, width = image.shape
pixels = image.flatten()

# Calculate pixel frequencies.
# Add 1 to every frequency to avoid zero-frequency symbols.
frequencies = np.bincount(pixels, minlength=256) + 1

# Create cumulative frequency table
cumulative = np.zeros(257, dtype=np.int64)
cumulative[1:] = np.cumsum(frequencies)

# Encode
encoded_data = arithmetic_encode(pixels, cumulative)

# Save compressed data:
# Height + Width + 256 frequencies + encoded bitstream
with open("arithmetic_compressed.bin", "wb") as file:
    file.write(struct.pack(">II", height, width))
    file.write(frequencies.astype(">u4").tobytes())
    file.write(encoded_data)

# Decode
decoded_pixels = arithmetic_decode(
    encoded_data, cumulative, len(pixels)
)

# Reconstruct image
decoded_image = decoded_pixels.reshape(height, width)

# Save reconstructed image
cv2.imwrite("arithmetic_decoded.jpg", decoded_image)

# Check reconstruction
print("Arithmetic Coding Completed!")
print("Original Image Size:", pixels.nbytes, "bytes")
print("Encoded Data Size:", len(encoded_data), "bytes")
print("Compressed File Size:", 8 + 1024 + len(encoded_data), "bytes")
print("Images Identical:", np.array_equal(image, decoded_image))

# Display images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(decoded_image, cmap="gray")
plt.title("Arithmetic Decoded Image")
plt.axis("off")

plt.tight_layout()
plt.show()
