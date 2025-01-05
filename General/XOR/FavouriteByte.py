from pwn import xor

# Given data
hidden_data = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# Check single bytes ranging from 0-255
for byte in range(256):
    decrypt = xor(hidden_data, byte)

    if b'crypto{' in decrypt:
        print(decrypt.decode())