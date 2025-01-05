from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Open and read the .der x509 file and get the modulus in the RSA key
with open('/Users/ravarro/Desktop/CryptoHack/General/Data Formats/2048b-rsa-cert.der', "rb") as f:
    certificate = x509.load_der_x509_certificate(f.read(), default_backend)
    modulus = certificate.public_key().public_numbers().n
    print(modulus)