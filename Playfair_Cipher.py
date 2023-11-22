# Implement playfair cipher technique in python

def generate_matrix(key):
    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(key[i*5+j])
    return matrix

def generate_text(text):
    text = text.upper()
    text = text.replace('J', 'I')
    text = text.replace(' ', '')
    for i in range(0, len(text), 2):
        if i+1==len(text):
            text += 'X'
        elif text[i]==text[i+1]:
            text = text[:i+1] + 'X' + text[i+1:]
    return text

def generate_key(key):
    key = key.replace(' ', '')
    key = key.upper()
    key = key.replace('J', 'I')
    key = ''.join(dict.fromkeys(key))
    for i in range(65, 91):
        if int(chr(i) not in key) & int(chr(i)!='J'):
            key += chr(i)
    return key

def encrypt(text, key):
    matrix = generate_matrix(key)
    
    encrypted = ""
    for i in range(0, len(text), 2):
        print(text[i])
        for j in range(5):
            if text[i] in matrix[j]:
                row1 = j
                col1 = matrix[j].index(text[i])
        for k in range(5):
            if text[i+1] in matrix[k]:
                row2 = k
                col2 = matrix[k].index(text[i+1])
                
        if row1==row2:
            encrypted += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1==col2:
            encrypted += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            encrypted += matrix[row1][col2] + matrix[row2][col1]
    return encrypted

def decrypt(text, key):
    matrix = generate_matrix(key)
    
    decrypted = ""
    for i in range(0, len(text), 2):
        for j in range(5):
            if text[i] in matrix[j]:
                row1 = j
                col1 = matrix[j].index(text[i])
        for k in range(5):
            if text[i+1] in matrix[k]:
                row2 = k
                col2 = matrix[k].index(text[i+1])
    
        if row1==row2:
            decrypted += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1==col2:
            decrypted += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            decrypted += matrix[row1][col2] + matrix[row2][col1]
    return decrypted    

if __name__=='__main__':
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = int(input("\nEnter choice: "))
        if choice==1:
            text = input("\nEnter the plain text to be encrypted: ")
            key = input("Enter the key: ")    
            text = generate_text(text)
            key = generate_key(key)    
            encrypted = encrypt(text, key)
            print("Encrypted text: " + encrypted)
        elif choice==2:
            text = input("\nEnter the cipher text to be decrypted: ")
            key = input("Enter the key: ")    
            text = generate_text(text)
            key = generate_key(key)    
            decrypted = decrypt(text, key)
            print("Decrypted text: " + decrypted)
        elif choice==3:
            break