from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from keys import KEY, INITIALIZATION_VECTOR

class Cipher:
    def encrypt(data: bytes) -> bytes:
        cipher = AES.new(KEY, AES.MODE_CBC, INITIALIZATION_VECTOR)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        return ciphertext


    def decrypt(ciphertext: bytes) -> bytes:
        decipher = AES.new(KEY, AES.MODE_CBC, INITIALIZATION_VECTOR)
        plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

        return plaintext
 