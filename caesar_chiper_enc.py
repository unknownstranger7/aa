plain_text = input("Enter the plain Text: ")
key = int(input("Enter the numeric key: "))

plain_text_lower = plain_text.lower()
encrypted_text = ""
for i in plain_text_lower:
    if i == ' ':
        encrypted_text+=' '
    else:
        value_i = ord(i)
        new_val = ((value_i+key-97)%26)
        encrypted_text += chr(new_val+97)
print("The Encrypted Text is: ")
print(encrypted_text)