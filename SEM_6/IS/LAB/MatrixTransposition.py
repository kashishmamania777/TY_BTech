import math

def encrypt_transposition(plaintext, key):
    # Remove spaces and convert to uppercase
    plaintext = ''.join(plaintext.split()).upper()
    
    # Calculate number of columns and rows
    cols = len(key)
    rows = math.ceil(len(plaintext) / cols)
    
    # Pad the plaintext if necessary
    plaintext += '_' * (cols * rows - len(plaintext))
    
    # Create the matrix
    matrix = [[''] * cols for _ in range(rows)]
    index = 0
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = plaintext[index]
            index += 1
    
    # Print the encryption matrix
    print("Encryption Matrix:")
    for row in matrix:
        print(row)
    
    # Read off the columns according to the key
    ciphertext = ''
    for col in key:
        col_index = int(col) - 1
        ciphertext += ''.join(matrix[row][col_index] for row in range(rows))
    
    return ciphertext

def decrypt_transposition(ciphertext, key):
    cols = len(key)
    rows = math.ceil(len(ciphertext) / cols)
    
    # Create the matrix
    matrix = [[''] * cols for _ in range(rows)]
    
    # Fill the matrix column by column according to the key
    index = 0
    for col in key:
        col_index = int(col) - 1
        for row in range(rows):
            if index < len(ciphertext):
                matrix[row][col_index] = ciphertext[index]
                index += 1
    
    # Print the decryption matrix
    print("Decryption Matrix:")
    for row in matrix:
        print(row)
    
    # Read off the matrix row by row
    plaintext = ''
    for row in matrix:
        plaintext += ''.join(row)
    
    # Remove padding
    plaintext = plaintext.rstrip('_')
    
    return plaintext

# Get user input
plaintext = input("Enter the message to encrypt: ")
key = input("Enter the key (e.g., 3142 for a 4-column transposition): ")

# Encrypt the message
encrypted = encrypt_transposition(plaintext, key)
print(f"Encrypted message: {encrypted}")

# Decrypt the message
decrypted = decrypt_transposition(encrypted, key)
print(f"Decrypted message: {decrypted}")
