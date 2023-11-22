import math

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            break
        
    d = mod_inverse(e, phi)
    return ((n, e), (n, d))

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(public_key, plaintext):
    n, e = public_key
    c = (plaintext ** e) % n
    return c

def decrypt(private_key, ciphertext):
    n, d = private_key
    m = (ciphertext ** d) % n
    return m

def sign_message(private_key, message):
    n, d = private_key
    signature = pow(message, d, n)
    return signature

def verify_signature(public_key, message, signature):
    n, e = public_key
    decrypted_signature = pow(signature, e, n)
    return message == decrypted_signature

p = 1223
q = 1151
public_key, private_key = generate_keypair(p, q)
message = 4

print("Original message:", message)
signature = sign_message(private_key, message)


concatenated_str = str(message) + str(signature)
concatenated_value = int(concatenated_str)

print("Concatenated value:", concatenated_value)

encrypted_value = encrypt(public_key, concatenated_value)
print("Encrypted value:", encrypted_value)

# Receiver's decryption
decrypted_value = decrypt(private_key, encrypted_value)

print("Decrypted value:", decrypted_value)
# Extract the original message and signature
decrypted_str = str(decrypted_value)
message_str = decrypted_str[:len(str(message))]
signature_str = decrypted_str[len(str(message)):]

# Convert back to integers
message = int(message_str)
signature = int(signature_str)

print("Decrypted message:", message)
print("Decrypted signature:", signature)

if verify_signature(public_key, message, signature):
    print("Signature is valid.")
else:
    print("Signature is invalid.")
