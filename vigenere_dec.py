encrypted = input("Enter the encrypted text: ")
key = input("Enter the key: ")

encrypted = encrypted.lower()
key = key.lower()

encrypted = encrypted.replace(" ", "")
key = key.replace(" ", "")

encrypted_list = list(encrypted)
key_list = list(key)

decrypted_list = []
while len(key_list) < len(encrypted_list):
    key_list = key_list + key_list

for i in range (len(encrypted_list)):
    decrypted_list.append(chr(((ord(encrypted_list[i]) - 97) - (ord(key_list[i]) - 97)) % 26 + 97))

decrypted = "".join(decrypted_list)
print("The decrypted text is: " + decrypted)
