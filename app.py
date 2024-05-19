from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import numpy as np
from hill_cipher import hill_encrypt, hill_decrypt, is_invertible

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def key_to_matrix(key):
    key_length = len(key)
    n = int(key_length ** 0.5)
    if n * n < key_length:
        n += 1
    
    key = key.ljust(n * n, 'X')  # Pad the key with 'X' until its length is a perfect square
    key_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            key_matrix[i][j] = ord(key[i * n + j]) % 256

    return np.array(key_matrix)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    key = request.form['key']

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        with open(file_path, 'r') as f:  # Open in text mode
            data = f.read()

        mode = request.form['mode']

        try:
            key_matrix = key_to_matrix(key)
        except ValueError as e:
            return str(e)

        if not is_invertible(key_matrix, 256):
            return 'The key matrix is not invertible modulo 256.'

        if mode == 'encrypt':
            result = hill_encrypt(data, key_matrix)
            output_filename = 'encrypted_' + filename
        elif mode == 'decrypt':
            result = hill_decrypt(data, key_matrix)
            output_filename = 'decrypted_' + filename
        else:
            return 'Invalid mode'

        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        with open(output_path, 'w') as f:  # Open in text mode
            f.write(result)

        return send_file(output_path, as_attachment=True, download_name=output_filename)

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
