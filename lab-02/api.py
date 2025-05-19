from flask import Flask, request, jsonify

app = Flask(__name__)

# Hàm mã hóa Vigenère
def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    encrypted_text = ''
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

# Hàm giải mã Vigenère
def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    decrypted_text = ''
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

# API mã hóa
@app.route('/api/vigenere/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    encrypted_text = vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

# API giải mã
@app.route('/api/vigenere/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    decrypted_text = vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Chạy server
if __name__ == '__main__':
    app.run(debug=True)
