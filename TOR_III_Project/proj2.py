# A Huffman Tree Node 
import heapq 
import numpy as np
from PIL import Image
import os
import pandas as pd

class node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		# frequency of symbol 
		self.freq = freq 

		# symbol name (character) 
		self.symbol = symbol 

		# node left of current node 
		self.left = left 

		# node right of current node 
		self.right = right 

		# tree direction (0/1) 
		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 


# utility function to print huffman 
# codes for all symbols in the newly 
# created Huffman tree 
def printNodes(node, val=''): 

	# huffman code for current node 
	newVal = val + str(node.huff) 

	# if node is not an edge node 
	# then traverse inside it 
	if(node.left): 
		printNodes(node.left, newVal) 
	if(node.right): 
		printNodes(node.right, newVal) 

		# if node is edge node then 
		# display its huffman code 
	if(not node.left and not node.right): 
		print(f"{node.symbol} -> {newVal}") 
		
# Function to encode an image using Huffman coding
def huffman_encode_image(image_path):
    # Read the image
    image = np.array(Image.open(image_path))
    
    
    # Convert image to binary string
    binary_string = ''.join(format(byte, '08b') for row in image for pixel in row for byte in pixel)

    # print("Initial" , binary_string)
    # Split the binary string into blocks of 8 bits
    blocks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    print("Total number of blocks", len(blocks))

    # Convert blocks to a set to get unique blocks
    unique_blocks = set(blocks)

    # Print the number of unique blocks
    print("Number of unique blocks:", len(unique_blocks))

    # Calculate block frequencies
    block_freq = {}
    for block in blocks:
        if block in block_freq:
            block_freq[block] += 1
        else:
            block_freq[block] = 1

    # Convert frequencies to probabilities
    total_blocks = len(blocks)
    probabilities = {block: freq / total_blocks for block, freq in block_freq.items()}
    # print(probabilities)

    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(probabilities.items(), columns=['Block', 'Probability'])

    # Print the DataFrame in tabular format
    print(df)

    # Construct Huffman tree
    nodes = [node(prob, block) for block, prob in probabilities.items()]
    heapq.heapify(nodes)
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = '0'
        right.huff = '1'
        merged = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, merged)

    # Huffman Tree is ready!
    root = nodes[0]

    # print("Huffman Codes:")
    # printNodes(root)

    # Encode the image using Huffman codes
    encoded_image = ''.join(get_huffman_code(root, block) for block in blocks)

    entropy_before = calculate_entropy(probabilities)
    print()
    print(f"Entropy before compression: {entropy_before} bits")

    # Length of encoded data in pixels
    encoded_length = len(encoded_image)
    #For a 24-bit RGB color image: 24 bits per pixel.
    encoded_length_in_bits = encoded_length / 24

    # Calculate average code length 
    avg_code_length = 0
    entropy_after = 0
    for block, prob in probabilities.items():
        code_length = len(get_huffman_code(root, block))  # Get code length for each block
        avg_code_length += prob * code_length
        entropy_after += prob * np.log2(1/prob)

    print(f"Average length:  {avg_code_length}")

    return encoded_image, encoded_length_in_bits

def get_huffman_code(root, block):
    if not root:
        return ''
    if root.left is None and root.right is None and root.symbol == block:
        return root.huff
    left_code = get_huffman_code(root.left, block)
    if left_code:
        return root.huff + left_code
    right_code = get_huffman_code(root.right, block)
    if right_code:
        return root.huff + right_code
    return ''

def calculate_entropy(probabilities):
  entropy = 0
  for block, prob in probabilities.items():
    if prob > 0:  # Avoid log(0)
      entropy += prob * np.log2(1/prob)
  return entropy


# Open the JPEG image of David Huffman
image_path = "huffman_david_kaput.png"


# Get the size of the original image
original_size = os.path.getsize(image_path)

encoded_image, encoded_length = huffman_encode_image(image_path)

# Calculate the size of the encoded image in bytes
encoded_size = encoded_length / 8

print(f"Original size: {original_size} bytes")
print(f"Encoded size: {encoded_size:.2f} bytes")

print()