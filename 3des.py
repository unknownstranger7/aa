from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Key should be 16 or 24 bytes long (Triple DES with two or three keys)
key = get_random_bytes(24)  # 3 keys of 8 bytes each
cipher = DES3.new(key, DES3.MODE_ECB)  # Triple DES in Electronic Codebook (ECB) mode

# Plaintext, it must be a multiple of 8 bytes
plaintext = b'SECRETEX'

# Ensure the plaintext is a multiple of 8 bytes by padding if needed
while len(plaintext) % 8 != 0:
    plaintext += b'\x00'

# Encrypt
ciphertext = cipher.encrypt(plaintext)

# Decrypt
decipher = DES3.new(key, DES3.MODE_ECB)
decrypted_plaintext = decipher.decrypt(ciphertext)

print("Original plaintext:", plaintext)
print("Encrypted ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
