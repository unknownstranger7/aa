import math
def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(len(matrix)):
            determinant += (-1) ** i * matrix[0][i] * det(minor(matrix, 0, i))
        return determinant

def minor(matrix, i, j):
    minor_matrix = []
    for row in range(len(matrix)):
        if row != i:
            minor_row = []
            for col in range(len(matrix)):
                if col != j:
                    minor_row.append(matrix[row][col])
            minor_matrix.append(minor_row)
    return minor_matrix

def cofactor(matrix):
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            sign = (-1) ** (i + j)
            minor_mat = minor(matrix, i, j)
            cofactor_row.append(sign * det(minor_mat))
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix

def adjugate(matrix):
    adjugate_matrix = []
    for i in range(len(matrix)):
        adjugate_row = [matrix[j][i] for j in range(len(matrix))]
        adjugate_matrix.append(adjugate_row)
    return adjugate_matrix


def inverse(matrix):
    det_matrix = det(matrix)
    if det_matrix == 0:
        return None
    else:
        cofactor_matrix = cofactor(matrix)
        adjugate_matrix = adjugate(cofactor_matrix)
        inverse_matrix = []
        for i in range (len(adjugate_matrix)):
            inverse_matrix.append([])

        for i in range(len(adjugate_matrix)):
            for j in range(len(adjugate_matrix)):
                inverse_matrix[i].append(adjugate_matrix[i][j] / det_matrix)
            
        
        return inverse_matrix


key= input("Enter the key: ")   
text= input("Enter the text: ")

#check if the length of the key is a perfect square
if not (math.sqrt(len(key)).is_integer()):
    print("The length of the key must be a perfect square")
    exit()

#if the length of the length of the text is not a multiple of the length of the key, add x's to the end of the text
if len(text) % len(key) != 0:
    for i in range(len(key) - (len(text) % len(key))):
        text += "x"

#convert the key to a matrix
key_matrix = []
for i in range(int(math.sqrt(len(key)))):
    key_matrix.append([])
    for j in range(int(math.sqrt(len(key)))):
        key_matrix[i].append(ord(key[i * int(math.sqrt(len(key))) + j]) - 97)
        
#convert the text to a matrix
text_matrix = []
for i in range(int(len(text) / len(key))):
    text_matrix.append([])
    for j in range(int(math.sqrt(len(key)))):
        text_matrix[i].append(ord(text[i * int(math.sqrt(len(key))) + j]) - 97)

#multiply the key matrix by the text matrix
product_matrix = []
for i in range(len(text_matrix)):
    product_matrix.append([])
    for j in range(len(key_matrix[0])):
        product_matrix[i].append(0)
        for k in range(len(key_matrix)):
            product_matrix[i][j] += key_matrix[i][k] * text_matrix[k][j]
        product_matrix[i][j] = product_matrix[i][j] % 26

#convert the product matrix to a string
product_string = ""
for i in range(len(product_matrix)):
    for j in range(len(product_matrix[0])):
        product_string += chr(product_matrix[i][j] + 97)
        
print("Encrypted text: " + product_string)
