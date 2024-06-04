# encrypting
from cryptography.fernet import Fernet
message = "prerna".encode()
key = b'PpeiY4Mree5nkOye-RMJ8RoWLOxgvFagpWIs-jWgDPs='
print(key)
f = Fernet(key)
encrypted = f.encrypt(message)
strEncrypted = str(encrypted, "utf8")
# print(encrypted)
print(strEncrypted)
# decrypting

decrypted = f.decrypt(encrypted)
strDecrypted = str(decrypted, "utf8")
print(strDecrypted)
# print(decrypted)
