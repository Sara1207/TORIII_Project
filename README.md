# Huffman Image Encoder

By: Natalija Tashkova, Sara Pachemska and Berna Asanova

## Description

This project implements Huffman coding to compress images. The program reads an image, converts it to a binary string, calculates the frequencies of unique blocks of 8 bits, constructs a Huffman tree based on these frequencies, and then encodes the image using the Huffman codes. The program also calculates and displays the entropy before compression, along with the average codeword length, original and compressed image sizes.

## Results
### Picture 1
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/e08f55ba-890b-4275-892c-f590daf0f846)
#### .jpg format 
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/16e0f9f9-100c-4952-b273-abac80afa04e)

#### .jpeg format
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/43477626-2eba-4474-8da8-7fc8b40e966e)

#### .png format
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/2099499f-bbd3-4b0f-9cc6-1780b0eeb7a8)


### Picture 2
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/edcefedc-78cf-413f-a9a5-392c69dd5d95)
#### .jpg format 
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/e5c79142-c714-4b5b-9de4-fea24b450ed7)

#### .jpeg format
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/d81bc4df-a343-48ca-be61-b577900611d6)

#### .png format
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/0bf3860a-94a8-4ccd-86a8-8698a9c1b37a)


### Picture 3
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/bba84186-9883-4e58-99c9-8386cadc59a9)
#### .jpg format 
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/a51167e6-e0e4-4b8e-9c43-4e0abc055832)

#### .jpeg format
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/edfcc058-43bb-4ea2-8db6-f8f9be77205f)

#### .png format
![image](https://github.com/Sara1207/TORIII_Project/assets/94647330/6a859192-847e-4dca-a366-df6a9067e8be)



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
