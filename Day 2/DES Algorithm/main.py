from base64 import encode
from Crypto.Cipher import DES
import base32hex
import hashlib

password = "Password"
salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
key = password + salt
m = hashlib.md5(key.encode())
key = m.digest()
(dk, iv) = (key[:8], key[8:])
crypter = DES.new(dk, DES.MODE_CBC, iv)

def encrypt(text):
    plain_text = text.encode("utf-8")
    plain_text += '\x00'.encode("utf-8") * (8 - len(plain_text) % 8)
    ciphertext = crypter.encrypt(plain_text)
    encode_string= base32hex.b32encode(ciphertext)
    return encode_string

def decrypt(cipher):
    encrypted_string = base32hex.b32decode(cipher)
    decrypted_string = crypter.decrypt(encrypted_string)
    return decrypted_string

plain = "I see you"
enc = encrypt(plain)
dec = decrypt(enc)
print("Cipher: {}".format(enc))
print("De-Cipher: {}".format(dec))
