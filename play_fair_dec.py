def generate_matrix(key):
    matrix = []
    alphanumeric_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    for i in range(6):
        matrix.append([])
        for j in range(6):
            matrix[i].append(key[i*6+j])
            alphanumeric_chars = alphanumeric_chars.replace(key[i*6+j], '')  # Remove used characters
    return matrix

def generate_text(text):
    text = text.upper()
    text = text.replace(' ', '')
    text = ''.join(char if char.isalnum() else 'X' for char in text)
    if len(text) % 2 != 0:
        text += 'X'
    return text

def generate_key(key):
    key = key.upper()
    key = key.replace(' ', '')
    key = ''.join(char if char.isalnum() else '' for char in key)
    alphanumeric_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    for char in alphanumeric_chars:
        if char not in key:
            key += char
    return key

def decrypt(text, key):
    matrix = generate_matrix(key)
    
    decrypted = ""
    for i in range(0, len(text), 2):
        for j in range(6):
            if text[i] in matrix[j]:
                row1 = j
                col1 = matrix[j].index(text[i])
        for k in range(6):
            if text[i+1] in matrix[k]:
                row2 = k
                col2 = matrix[k].index(text[i+1])
    
        if row1 == row2:
            decrypted += matrix[row1][(col1-1) % 6] + matrix[row2][(col2-1) % 6]
        elif col1 == col2:
            decrypted += matrix[(row1-1) % 6][col1] + matrix[(row2-1) % 6][col2]
        else:
            decrypted += matrix[row1][col2] + matrix[row2][col1]
    return decrypted

if __name__ == '__main__':
    key = input("Enter key: ")
    encrypted = input("Enter encrypted text: ")

    decrypted = decrypt(generate_text(encrypted), generate_key(key))
    print(decrypted)
