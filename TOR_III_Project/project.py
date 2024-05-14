import numpy as np
from PIL import Image

class Node:
  def __init__(self, freq, symbol):
    self.freq = freq
    self.symbol = symbol
    self.left = None
    self.right = None

def huffman_algorithm(c):
  n = len(c)

  # Initialize a priority queue Q with all symbols in c
  Q = [Node(freq, symbol) for symbol, freq in c.items()]

  # Construct Huffman tree
  for i in range(1, n):
    temp = Node(None, None)
    temp.left = get_min(Q)
    temp.right = get_min(Q)
    temp.freq = temp.left.freq + temp.right.freq
    insert(Q, temp)

  # Return root of Huffman tree
  return get_min(Q)

def get_min(Q):
  return Q.pop()

def insert(Q, node):
  Q.append(node)

def generate_codes(root, codes, prefix):
  if root is None:
    return
  if root.symbol is not None:
    codes[root.symbol] = prefix
    return

  generate_codes(root.left, codes, prefix + "0")
  generate_codes(root.right, codes, prefix + "1")

# Open the JPEG image of David Huffman
image_path = "david_huffman.jpg"
image = np.array(Image.open(image_path))

# Convert image to bits
image_bits = ''.join(format(int(byte), '08b') for byte in image.flatten())

# Split the image into blocks of 8bits
block_size = 8
image_blocks = [image_bits[i:i+block_size] for i in range(0, len(image_bits), block_size)]

# Calculate frequency of each bit
frequency = {}
for block in image_blocks:
  if block in frequency:
    frequency[block] += 1
  else:
    frequency[block] = 1

# Calculate entropy before compression
total_blocks = len(image_blocks)
entropy_before = -sum((freq / total_blocks) * np.log2(freq / total_blocks) for freq in frequency.values())
print("Entropy before: ", entropy_before)

# Apply Huffman algorithm
huffman_tree_root = huffman_algorithm(frequency)

# Generate Huffman codes
codes = {}
generate_codes(huffman_tree_root, codes, "")


# Encode image data
compressed_data = ""
for block in image_blocks:
  compressed_data += codes[block]

# Calculate entropy after compression
compressed_length = len(compressed_data)
entropy_after = -sum((len(code) / compressed_length) * np.log2(len(code) / compressed_length) for code in codes.values())

# Calculate average length of codewords
# TO-DO find the formula
expected_codeword_length = sum((freq / total_blocks) * len(code) for code, freq in zip(codes.values(), frequency.values()))
# Print entropy
print("Entropy after:", entropy_after)
print("Average length of the codewords: " , expected_codeword_length)