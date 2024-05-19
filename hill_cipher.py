import numpy as np

def hill_encrypt(message, key_matrix):
    n = key_matrix.shape[0]
    message = [ord(char) % 256 for char in message]
    while len(message) % n != 0:
        message.append(ord('X') % 256)

    ciphertext = []
    for i in range(0, len(message), n):
        block = np.array(message[i:i + n])
        cipher_block = np.dot(key_matrix, block) % 256
        ciphertext.extend(cipher_block)

    return ''.join(chr(int(c)) for c in ciphertext)

def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    ciphertext = [ord(char) % 256 for char in ciphertext]

    # Calculate inverse of the key matrix
    try:
        key_matrix_inv = np.linalg.inv(key_matrix)
    except np.linalg.LinAlgError:
        raise ValueError("Key matrix is not invertible")

    key_matrix_inv = (key_matrix_inv * np.linalg.det(key_matrix) * np.linalg.inv(np.linalg.det(key_matrix))) % 256
    plaintext = []
    for i in range(0, len(ciphertext), n):
        block = np.array(ciphertext[i:i + n])
        plain_block = np.dot(key_matrix_inv, block) % 256
        plaintext.extend(plain_block)

    return ''.join(chr(int(p)) for p in plaintext)

def is_invertible(key_matrix, modulo):
    try:
        inv = np.linalg.inv(key_matrix)
        return np.allclose(np.dot(key_matrix, inv), np.eye(key_matrix.shape[0]))
    except np.linalg.LinAlgError:
        return False
