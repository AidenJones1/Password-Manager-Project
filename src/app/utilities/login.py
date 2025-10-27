from encryption.encryption import decrypt_text, encrypt_text

def attempt_login(entry: str):
    master_password = decrypt_text("data/00.txt")
    return entry == master_password

def change_master_password(new_password: str):
    encrypt_text(new_password.encode(), "data/00.txt")