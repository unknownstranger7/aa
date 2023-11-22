key= input("Enter the key: ")
key=key.replace(" ","")
key=key.upper()

text= input("Enter the text: ")
text=text.replace(" ","")


#check the length of the key is a perfect square
import math
if not (math.sqrt(len(key)).is_integer()):
    print("The length of the key is not a perfect square")
    exit()

#check if the length of the text is the multiple of the root of the length of the key
if len(text) % int(math.sqrt(len(key))) != 0:
    print("The length of the text is not a multiple of the root of the length of the key")
    exit()

#convert the key to a matrix
key_matrix = []
for i in range(int(math.sqrt(len(key)))):
    key_matrix.append([])
    for j in range(int(math.sqrt(len(key)))):
        key_matrix[i].append(ord(key[i * int(math.sqrt(len(key))) + j]) - 65)
        