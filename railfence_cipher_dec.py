no_row = int(input("Enter the number of rows: "))
encrypted = input("Enter the Encrypted Text: ")
import math
matrix = [['0' for i in range(len(encrypted))] for j in range(no_row)]

row = 0
column = 0
while column<len(encrypted):
    if row == 0:
        down = True
    if row == no_row-1:
        down = False
    matrix[row][column] = "*"
    column += 1
    if down:
        row += 1
    else:
        row -= 1

pointer = 0
for i in range(no_row):
    for j in range(len(encrypted)):
        if matrix[i][j] == "*":
            if pointer == len(encrypted):
                break
            matrix[i][j] = encrypted[pointer]
            pointer += 1

plain_text = ""

row = 0
column = 0
while column<len(encrypted):
    if row == 0:
        down = True
    if row == no_row-1:
        down = False
    plain_text+= matrix[row][column]
    column += 1
    if down:
        row += 1
    else:
        row -= 1


print("Decrypted text:", plain_text)