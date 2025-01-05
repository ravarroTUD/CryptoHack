from pwn import xor

# Given keys
k1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2k1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
k2k3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flagk1k3k2 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# XOR to get key2 and key3
k2 = xor(k2k1, k1)
k3 = xor(k2k3, k2)

# XOR all keys to get flag
flag = xor(flagk1k3k2, xor(k1, xor(k2, k3)))

print(flag.decode())