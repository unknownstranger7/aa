enc_text = input("Enter the encypted text: ")
key =int(input("Enter the numeric key: "))


plain_text= ''
for i in enc_text:
    if i == ' ':
        plain_text +=  " "
    
    else: 
        val = ord(i)
        temp = ((val-97-key)%26)+97
        plain_text += (chr(temp))
print("The Plain Text is: ")
print(plain_text)
