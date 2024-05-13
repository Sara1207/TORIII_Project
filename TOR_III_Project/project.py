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

# Calculate frequency of each bit
frequency = {}
for bit in image_bits:
  if bit in frequency:
    frequency[bit] += 1
  else:
    frequency[bit] = 1

# Calculate entropy before compression
total_bits = len(image_bits)
entropy_before = -sum((freq / total_bits) * np.log2(freq / total_bits) for freq in frequency.values())
print("Entropy before: ", entropy_before)

# Apply Huffman algorithm
huffman_tree_root = huffman_algorithm(frequency)

# Generate Huffman codes
codes = {}
generate_codes(huffman_tree_root, codes, "")


# Encode image data
compressed_data = ""
for bit in image_bits:
  compressed_data += codes[bit]

# Calculate entropy after compression
compressed_length = len(compressed_data)
entropy_after = -sum((len(code) / compressed_length) * np.log2(len(code) / compressed_length) for code in codes.values())

# Calculate average length of codewords
expected_codeword_length = 0
# Print entropy
print("Entropy after:", entropy_after)
print("Average length of the codewords: " , expected_codeword_length)