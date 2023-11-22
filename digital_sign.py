import random
import math
from sympy import isprime

def is_prime(num):
    if isprime(num):
        return True
    else:
        return False




def generate_keypair(bits):
    p, q = generate_prime(bits), generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Commonly used value for 'e'
    d = mod_inverse(e, phi)
    return ((n, e), (n, d))

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Digital Signature Generation and Verification
def sign_message(private_key, message):

    n, d = private_key
    message_bytes = message.encode()
    message_int = int.from_bytes(message_bytes, byteorder='big')
    signature = pow(message_int, d, n)
    return signature

def verify_signature(public_key, message, signature):

    n, e = public_key
    message_bytes = message.encode()
    message_int = int.from_bytes(message_bytes, byteorder='big')
    decrypted_signature = pow(signature, e, n)
    return message_int == decrypted_signature

# Example usage
key_size = 2048  # Adjust the key size as needed
private_key, public_key = generate_keypair(key_size)
message = "Your file content here"
signature = sign_message(private_key, message)

print("Original message:", message)
print("Signature:", signature)
  
# Simulate recipient verifying the signature
is_valid = verify_signature(public_key, message, signature)

if is_valid:
    print("Signature is valid. The file is from the sender.")
else:
    print("Signature is invalid. The file may have been tampered with.")
