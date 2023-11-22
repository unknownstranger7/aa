#10 a
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Prepare data
data = b"Your data to be signed"

# Sign the data
signature = private_key.sign(
    data,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Verify the signature
try:
    public_key.verify(
        signature,
        data,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Signature is valid.")
except:
    print("Signature is invalid.")
