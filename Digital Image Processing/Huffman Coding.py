import cv2
import numpy as np
import matplotlib.pyplot as plt
import heapq
from collections import Counter

# -------------------------------
# Huffman Tree Node
# -------------------------------
class Node:
    def __init__(self, symbol=None, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right


# -------------------------------
# Build Huffman Tree
# -------------------------------
def build_huffman_tree(pixels):
    frequency = Counter(int(pixel) for pixel in pixels)

    heap = []
    counter = 0

    for symbol, freq in frequency.items():
        node = Node(symbol=symbol)
        heapq.heappush(heap, (freq, counter, node))
        counter += 1

    # Handle an image containing only one pixel value
    if len(heap) == 1:
        return heap[0][2]

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        parent = Node(left=left, right=right)

        heapq.heappush(
            heap,
            (freq1 + freq2, counter, parent)
        )
        counter += 1

    return heap[0][2]


# -------------------------------
# Generate Huffman Codes
# -------------------------------
def generate_codes(node, code="", codes=None):
    if codes is None:
        codes = {}

    # Leaf node
    if node.symbol is not None:
        codes[node.symbol] = code if code else "0"
        return codes

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

    return codes


# -------------------------------
# Encode Image
# -------------------------------
def encode_image(pixels, codes):
    encoded = ""

    for pixel in pixels:
        encoded += codes[int(pixel)]

    return encoded


# -------------------------------
# Decode Image
# -------------------------------
def decode_image(encoded, root):
    decoded = []

    # Special case: only one unique pixel value
    if root.symbol is not None:
        decoded = [root.symbol] * len(encoded)
        return np.array(decoded, dtype=np.uint8)

    current = root

    for bit in encoded:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.symbol is not None:
            decoded.append(current.symbol)
            current = root

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

# Build Huffman tree
huffman_tree = build_huffman_tree(pixels)

# Generate codes
huffman_codes = generate_codes(huffman_tree)

# Encode image
encoded_data = encode_image(pixels, huffman_codes)

# Decode image
decoded_pixels = decode_image(encoded_data, huffman_tree)

# Reconstruct image
decoded_image = decoded_pixels.reshape(height, width)

# Save reconstructed image
cv2.imwrite("huffman_decoded.jpg", decoded_image)

# -------------------------------
# Display Results
# -------------------------------

print("Huffman Coding Completed!")
print("\nHuffman Codes:")

for symbol, code in sorted(huffman_codes.items()):
    print(f"Pixel {symbol}: {code}")

original_size = pixels.size * 8
compressed_size = len(encoded_data)

print("\nOriginal Size:", original_size, "bits")
print("Encoded Size:", compressed_size, "bits")

if compressed_size > 0:
    ratio = original_size / compressed_size
    print("Compression Ratio:", round(ratio, 2), ":1")

print("Images Identical:", np.array_equal(image, decoded_image))

# Display original and decoded images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(decoded_image, cmap="gray")
plt.title("Huffman Decoded Image")
plt.axis("off")

plt.tight_layout()
plt.show()
