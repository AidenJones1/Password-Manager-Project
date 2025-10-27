from cryptography.fernet import Fernet

# key is generated
key = Fernet.generate_key()

with open("./0/filekey.key", "wb") as keyfile:
    keyfile.write(key)