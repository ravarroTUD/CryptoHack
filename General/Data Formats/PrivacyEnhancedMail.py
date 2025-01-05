from Crypto.PublicKey import RSA
from base64 import b64encode, b16encode

# Open and read the .pem file and import key into variable 'RSAkey'
with open('/Users/ravarro/Desktop/CryptoHack/General/Data Formats/privacy_enhanced_mail.pem', "rb") as f:
    RSAkey = RSA.import_key(f.read())
    print(RSAkey.d)