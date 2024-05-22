# Hill Cipher Web Application

## Overview

This is a web application that implements the Hill Cipher, a polygraphic substitution cipher based on linear algebra. The application allows users to encrypt and decrypt text files using a key matrix.

## Features

- Encrypt text files using a specified key.
- Decrypt text files using the inverse of the specified key.
- Simple web interface to upload files and enter the key.

## Requirements

- Python 3.x
- Flask
- NumPy

## Installation

1. **Clone the repository**:
- `git clone [git@github.com:Th3-l4dy/TpSecurity.git](https://github.com/Th3-l4dy/TpSecurity.git)
cd hill_cipher_web`
- or unzip the folder `hill_cipher_web`  i have attached some videos
- **Install the required packages**:
- `pip install -r requirements.txt`
- **Run the application**:
- `python app.py`
- **Open your web browser and navigate to**:
1. `http://127.0.0.1:5000`

## Usage

### Encryption

1. Upload a text file containing the plaintext.
2. Enter the key as a string (e.g., "abcd" for a 2x2 key matrix).
3. Select "Encrypt" mode.
4. Click "Submit" to download the encrypted file.

### Decryption

1. Upload the encrypted text file.
2. Enter the key used for encryption. The application will automatically compute the inverse key.
3. Select "Decrypt" mode.
4. Click "Submit" to download the decrypted file.

### Key Matrix

The key is entered as a string of characters. For example, if you enter "abcd" as the key:

- It will be converted to a 2x2 key matrix based on the ASCII values of the characters.
- During decryption, the inverse of this key matrix will be computed and used.

### Important Note

The key matrix must be invertible. If the key matrix is not invertible modulo 256, an error will be shown.

## Example

### Encryption

- **Plaintext**: "Th3-L4dy says Hello"
- **Key**: "abcd" (which corresponds to a 2x2 matrix)

### Decryption

- **Encrypted Text**: another plain text since the encrypted text has inprintable chars
- **Key**: "abcd" (the application will compute its inverse for decryption).

The decrypted text should match the original plaintext "Th3-L4dy says Hello". —> in an ideal scenario 

## Troubleshooting

- **Error: "The key matrix is not invertible modulo 256."**: Ensure the key forms an invertible matrix.
- **Unexpected characters in output**: Check if the input text and key are correctly formatted.

## Acknowledgments

- This project uses Flask for the web interface.
- NumPy is used for matrix operations.

`use` sample.txt for testing