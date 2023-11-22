enc_text = input("Enter the Encypted Text: ")

for key in range (0,26):
    plain_text = ""
    for i in enc_text:
        if i == ' ':
            plain_text +=  " "
        
        else: 
            val = ord(i)
            temp = ((val-97-key)%26)+97
            plain_text += (chr(temp))
    print("for the key: ",key, end='  ')
    print("plain text should be: ",plain_text)