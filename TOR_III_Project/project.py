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
# print(image_bits[:8])

# Split the image into blocks of 8bits
block_size = 8
image_blocks = [image_bits[i:i+block_size] for i in range(0, len(image_bits), block_size)]

print(image_blocks[0])

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

# Calculate probability distribution for each block
probabilities = {block: freq / total_blocks for block, freq in frequency.items()}
# print(probabilities)
print("Total num.of blocks: " , total_blocks)

# Apply Huffman algorithm
huffman_tree_root = huffman_algorithm(probabilities)

# Generate Huffman codes
codes = {}
generate_codes(huffman_tree_root, codes, "")
print("codes",codes)

# # Encode image data
# compressed_data = ""
# for block in image_blocks:
#   compressed_data += codes[block]

# Encode image data using Huffman codes
compressed_data = "".join(codes[block] for block in image_blocks)

# Calculate entropy after compression
compressed_length = len(compressed_data)
# entropy_after = -sum((len(code) / compressed_length) * np.log2(len(code) / compressed_length) for code in codes.values())
entropy_after = -sum((len(codes[block]) / compressed_length) * np.log2(len(codes[block]) / compressed_length) for block in image_blocks)

# Calculate average length of codewords
# expected_codeword_length = sum((freq / total_blocks) * len(code) for code, freq in zip(codes.values(), frequency.values()))
# Calculate average length of codewords
expected_codeword_length = sum((probabilities[block] * len(codes[block])) for block in image_blocks)

# Print entropy
print("Entropy after:", entropy_after)
print("Average length of the codewords: " , expected_codeword_length)

# Print frequencies and corresponding blocks
print("Frequencies and Blocks:")
for block, freq in frequency.items():
    print("Block:", block, "- Frequency:", freq)

# Find the block with the highest frequency
most_frequent_block = max(frequency, key=frequency.get)

# Retrieve its corresponding codeword
codeword_most_frequent = codes[most_frequent_block]

# Print the result
print("Codeword for the most frequent block:", codeword_most_frequent)