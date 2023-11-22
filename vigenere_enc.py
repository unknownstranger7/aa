plain_text = input("Enter the plain text: ")
key = input("Enter the key: ")
plain_text = plain_text.lower()
key = key.lower()
plain_text = plain_text.replace(" ", "")
key = key.replace(" ", "")
plain_text_list = list(plain_text)
key_list = list(key)

cipher_text_list = []

while len(key_list) < len(plain_text_list):
    key_list = key_list + key_list

for i in range (len(plain_text_list)):
    cipher_text_list.append(chr(((ord(plain_text_list[i]) - 97) + (ord(key_list[i]) - 97)) % 26 + 97))

cipher_text = "".join(cipher_text_list)
print("The cipher text is: " + cipher_text)
