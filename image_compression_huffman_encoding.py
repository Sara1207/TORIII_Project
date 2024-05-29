# A Huffman Tree Node 
import heapq 
import numpy as np
from PIL import Image
import os
import pandas as pd

class node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		# symbol frequency
		self.freq = freq 

		# symbol name
		self.symbol = symbol 

		# left child node
		self.left = left 

		# right child node
		self.right = right 

		# tree direction 0 or 1
		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 


# Function to print huffman codes for the symbols
def printNodes(node, val=''): 

	# Huffman code for current node 
	current = val + str(node.huff) 

	#  Find the leaf node
	if(node.left): 
		printNodes(node.left, current) 
	if(node.right): 
		printNodes(node.right, current) 

	# If the node is a leaf node then print 
	if(not node.left and not node.right): 
		print(f"{node.symbol} -> {current}") 
		
# Function to encode an image using Huffman coding
def huffman_encode_image(image_path):
    # Read the image
    image = np.array(Image.open(image_path)) # Pixel values

    # Variable to store the binary data
    binary_string = ''

    # Iterate over each row in the image
    for row in image:
        # Iterate over each pixel in the row
        for pixel in row:
            # Iterate over each byte in the pixel
            for byte in pixel:
                # Convert the byte to binary and add it to the string
                binary_string += format(byte, '08b')

    # Initialize an empty list to store the blocks
    blocks = []

    # Iterate over the binary string in steps of 8 bits
    for i in range(0, len(binary_string), 8):
        # Extract a block of 8 characters
        block = binary_string[i:i+8]
        
        # Add the block to the list
        blocks.append(block)

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

    # Convert the dictionary to a pandas DataFrame for better visualization
    df = pd.DataFrame(probabilities.items(), columns=['Block', 'Probability'])

    # Print the DataFrame in tabular format
    print(df)

    # Construct Huffman tree
    nodes = [node(prob, block) for block, prob in probabilities.items()] # Create a node for each block
    heapq.heapify(nodes) # Create a min heap of the nodes
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = '0'
        right.huff = '1'
        merged = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, merged)

    # Root node of the Huffman tree
    root = nodes[0]

    # print("Huffman Codes:")
    # printNodes(root)

    # Variable to store the encoded image
    encoded_image = ''

    # Iterate over each block in the blocks list
    for block in blocks:
        # Get the Huffman code for the block
        huffman_code = get_huffman_code(root, block)
        
        encoded_image += huffman_code

    # Calculate entropy before compression
    entropy_before = calculate_entropy(probabilities)
    print(f"\nEntropy before compression: {entropy_before} bits")

    # Length of encoded data in pixels
    encoded_length = len(encoded_image)

    # Length of encoded data in bits
    encoded_length_in_bits = encoded_length / 24

    # Calculate average code length 
    avg_code_length = 0

    for block, prob in probabilities.items():
        # Length of the Huffman code for the block
        code_length = len(get_huffman_code(root, block))
        # Average code length
        avg_code_length += prob * code_length

    print(f"Average length:  {avg_code_length}")

    # Return the encoded image and its length in bits
    return encoded_image, encoded_length_in_bits 

# Function to get the Huffman code for a block
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

# Function to calculate entropy
def calculate_entropy(probabilities):
  entropy = 0
  for block, prob in probabilities.items():
    if prob > 0:
        # Calculate the entropy for this block
        block_entropy = prob * np.log2(1/prob)

        # Add the block's entropy to the total entropy
        entropy += block_entropy
  return entropy


# Open the image file
image_path = "testing_images/david_huffman.png"


# Size of the original image
original_size = os.path.getsize(image_path)

# Encode the image
encoded_image, encoded_length = huffman_encode_image(image_path)

# Calculate the size of the encoded image in bytes
encoded_size = encoded_length / 8

print(f"Original size: {original_size} bytes")
print(f"Encoded size: {encoded_size:.2f} bytes\n")