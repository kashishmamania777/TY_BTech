def encrypt_shift(plaintext, key):
    ciphertext = ""
    for char in plaintext.lower():
        if char.isalpha():
            shifted = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            ciphertext += shifted
        else:
            ciphertext += char
    return ciphertext.upper()

def decrypt_shift(ciphertext, key):
    plaintext = ""
    for char in ciphertext.lower():
        if char.isalpha():
            shifted = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            plaintext += shifted
        else:
            plaintext += char
    return plaintext

# Example usage
key = 15
message = "hello"
encrypted = encrypt_shift(message, key)
decrypted = decrypt_shift(encrypted, key)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
