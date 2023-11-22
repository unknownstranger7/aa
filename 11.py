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

def sign_message(private_key, message):
    n, d = private_key
    signature = pow(message, d, n)
    return signature

def verify_signature(public_key, private_key_receiver, encrypted_value):
    n_receiver, d_receiver = private_key_receiver
    n_sender, e_sender = public_key
    decrypted_value = pow(encrypted_value, d_receiver, n_receiver)
    decrypted_value = str(decrypted_value)
    message = int(decrypted_value[0])
    signature = int(decrypted_value[1:])
    print("Message:", message)
    decrypted_signature = pow(signature, e_sender, n_sender)
    return message == decrypted_signature

def encrypt(public_key, plaintext):
    n, e = public_key
    c = pow(plaintext, e, n) 
    return c

def decrypt(private_key, ciphertext):
    n, d = private_key
    m = pow(ciphertext, d, n)  
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


p = generate_prime(16) 
q = generate_prime(16)
public_key, private_key = generate_keypair(p, q)
print(f"Public key Sender: {public_key} \nPrivate key Sender: {private_key}")
message = 4

print("Original message:", message)
signature = sign_message(private_key, message)
print("Signature:", signature)

concatenated_str = str(message) + str(signature)
concatenated_value = int(concatenated_str)

print("Concatenated value:", concatenated_value)

p_receiver = generate_prime(64)
q_receiver = generate_prime(64)
public_key_receiver, private_key_receiver = generate_keypair(p_receiver, q_receiver)
print(f"Public key Receiver: {public_key_receiver} \nPrivate key Receiver: {private_key_receiver}")

encrypted_value = encrypt(public_key_receiver, concatenated_value)
print("Encrypted value:", encrypted_value)

if verify_signature(public_key, private_key_receiver, encrypted_value):
    print("Signature is valid.")
else:
    print("Signature is invalid.")
