import requests

# Request encrypted flag from CryptoHack
def decrypt(ciphertext):
    url = f'http://aes.cryptohack.org/block_cipher_starter/decrypt/{ciphertext}'
    response = requests.get(url)
    return response.json()

# Request decrypted ciphertext CryptoHack
def encrypt_flag():
    url = 'http://aes.cryptohack.org/block_cipher_starter/encrypt_flag'
    response = requests.get(url)
    return response.json()['ciphertext']

def main():
    # Get and print the encrypted flag
    ciphertext = encrypt_flag()
    print("Ciphertext:", ciphertext)

    # Get and print the decrypted ciphertext
    plaintext = decrypt(ciphertext)["plaintext"]
    print("Decrypted ciphertext:", bytes.fromhex(plaintext).decode())

# Run def main()
if __name__ == "__main__":
    main()


    