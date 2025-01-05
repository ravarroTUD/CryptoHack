from pwn import xor

# Given encrypted flag
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# XOR the known flag format
starting_format = b'crypto{'

# Find the first 7 letters of the partial key
partial_key = xor(flag[:7], starting_format)

# The first 7 known key is "myXORke" which is most likely to be "myXORkey"
key = b'myXORkey'

decrypted_key = xor(flag, key)

print(decrypted_key.decode())