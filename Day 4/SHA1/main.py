import hashlib

plain = input("Plain Text: ")
hash = hashlib.sha1(plain.encode())

print("SHA1 Equivalent of String: {}".format(hash.digest()))
print("Hexadecimal Equicalent of SHA1: {}".format(hash.hexdigest()))
