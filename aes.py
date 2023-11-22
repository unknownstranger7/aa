from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Key should be 16, 24, or 32 bytes long (AES-128, AES-192, or AES-256)
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

# Plaintext
plaintext = b'Secret Message'
print(f'Original PlainText : {plaintext}')
# Encrypt
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Decrypt
cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted_plaintext = cipher.decrypt(ciphertext)

# Verify integrity
try:
    cipher.verify(tag)
    print("Encrypted Message is : ", ciphertext)
    print("Decryption successful")
    print("Decrypted text:", decrypted_plaintext.decode('utf-8'))
except ValueError:
    print("Decryption failed")
