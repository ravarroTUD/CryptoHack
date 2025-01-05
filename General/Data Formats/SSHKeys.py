from Crypto.PublicKey import RSA

with open('/Users/ravarro/Desktop/CryptoHack/General/Data Formats/bruce_rsa.pub', "rb") as f:
    RSAkey = RSAkey = RSA.import_key(f.read())
    print(RSAkey.n)