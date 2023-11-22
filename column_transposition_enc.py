text = input("Enter the Input Text: ")
key = input("Enter the Key: ")


num_rows = ((len(text)) // len(key) )+1

matrix = [['x' for _ in range(len(key))] for _ in range(num_rows)]

for i in range(len(text)):
    matrix[i // len(key)][i % len(key)] = text[i]


sorted_key = sorted(key)
key_indices = [key.index(sorted_key[i]) for i in range(len(key))]

print("Encrypted text: ", end = "")
for i in range(len(key)):
    for j in range(num_rows):
            print(matrix[j][key_indices[i]], end = "")
print()



