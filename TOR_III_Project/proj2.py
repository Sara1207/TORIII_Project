# A Huffman Tree Node 
import heapq 
import numpy as np
from PIL import Image


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

    print("Initial" , binary_string)
    # Split the binary string into blocks of 8 bits
    blocks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

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
    print(probabilities)
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
    print("Huffman Codes:")
    printNodes(root)

    # Encode the image using Huffman codes
    encoded_image = ''.join(get_huffman_code(root, block) for block in blocks)

    entropy_before = calculate_entropy(probabilities)
    print(f"Entropy before compression: {entropy_before} bits")

    # Length of encoded data in bits
    encoded_length = len(encoded_image)

    # Calculate average code length 
    avg_code_length = 0
    entropy_after = 0
    for block, prob in probabilities.items():
        code_length = len(get_huffman_code(root, block))  # Get code length for each block
        avg_code_length += prob * code_length
        entropy_after += prob * np.log2(1/prob)

    print(f"Average length:  {avg_code_length}")

    return encoded_image

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
image_path = "david_huffman.jpg"
encoded_image = huffman_encode_image(image_path)
# print("Encoded", encoded_image)




