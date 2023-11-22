encrypted = input("Enter the encrypted text: ")
key = input("Enter the Key: ")



num_rows = (len(encrypted) + len(key) - 1) // len(key)

matrix = [['x' for _ in range(len(key))] for _ in range(num_rows)]

sorted_key = sorted(key)
key_indices = [key.index(sorted_key[i]) for i in range(len(key))]

count = 0
for i in range (len(key)):
    for j in range(num_rows):
        matrix[j][key_indices[i]] = encrypted[count]
        count += 1


print("Decrypted text:", end=" ")

for i in range(num_rows):
    for j in range(len(key)):
            print(matrix[i][j], end="")

print()
