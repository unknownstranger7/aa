no_row = int(input("Enter the number of rows: "))
message = input("Enter the message: ")



matrix = [['0' for i in range(len(message))] for j in range(no_row)]

row = 0
column = 0
while column<len(message):
    if row == 0:
        down = True
    if row == no_row-1:
        down = False
    matrix[row][column] = message[column]
    column += 1
    if down:
        row += 1
    else:
        row -= 1
        
# print(matrix)

encrypted = ""
for i in range(no_row):
    for j in range(len(message)):
        if matrix[i][j] != '0':
            encrypted += matrix[i][j]
print("Encrypted text:", encrypted)


