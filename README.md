# Huffman Image Encoder

By: Natalija Tashkova, Sara Pachemska and Berna Asanova

## Description

This project implements Huffman coding to compress images. The program reads an image, converts it to a binary string, calculates the frequencies of unique blocks of 8 bits, constructs a Huffman tree based on these frequencies, and then encodes the image using the Huffman codes. The program also calculates and displays the entropy before compression, along with the average codeword length, original and compressed image sizes.

## Requirements

- Python 3.x
- `numpy`
- `Pillow`
- `pandas`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/huffman-image-encoder.git
   cd huffman-image-encoder

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate

3. Install the required packages:

    ```bash
    pip install -r requirements.txt

4. How to Run
    ```bash
    python huffman_image_encoder.py
