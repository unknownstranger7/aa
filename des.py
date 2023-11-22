from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Key should be 8 bytes long (56 bits)
key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)  # DES in Electronic Codebook (ECB) mode

# Plaintext, it must be a multiple of 8 bytes
plaintext = b'SECRETEX'

# Ensure the plaintext is a multiple of 8 bytes by padding if needed
while len(plaintext) % 8 != 0:
    plaintext += b'\x00'

# Encrypt
ciphertext = cipher.encrypt(plaintext)

# Decrypt
decipher = DES.new(key, DES.MODE_ECB)
decrypted_plaintext = decipher.decrypt(ciphertext)

print("Original plaintext:", plaintext)
print("Encrypted ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
