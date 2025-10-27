from cryptography.fernet import Fernet
import pandas as pd
import io
from resources import resource_path

def encrypt_text(plain_text, file_path):
    with open(resource_path("00/filekey.key"), "rb") as keyfile:
        key = keyfile.read()
    
    if key is not None:
        f = Fernet(key)
        cipher_text = f.encrypt(plain_text)

        with open(resource_path(file_path), "wb") as file:
            file.write(cipher_text)

def decrypt_text(file_path):
    with open(resource_path("00/filekey.key"), "rb") as keyfile:
        key = keyfile.read()

    if key is not None:
        f = Fernet(key)
        
        with open(resource_path(file_path), "rb") as file:
            cipher_text = file.read()

            plain_text = f.decrypt(cipher_text).decode()

            return plain_text
    return ""
        
#with open("./data/my_passwords.csv", "rb") as file:
#    text = file.read()

#    encrypt_text(text, "./data/01.txt")

#text = decrypt_text("./data/01.txt")
#res = pd.read_csv(io.StringIO(text), sep = ",")
#print(res)