import math
import random 
from sympy import isprime

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randrange(1, phi)
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

def is_prime(num):
    if isprime(num):
        return True
    else:
        return False

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

p = generate_prime(10)
q = generate_prime(10)
public_key, private_key = generate_keypair(p, q)

message = 427337
ciphertext = encrypt(public_key, message)
print(f'Public key: {public_key} \nPrivate key: {private_key}')
decrypted_message = decrypt(private_key, ciphertext)

print("Original message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted message:", decrypted_message)
