import pandas as pd
from encryption.encryption import decrypt_text
import io

PASSWORDS_FILE_PATH = "data/01.txt"
DEFAULT_DF = pd.DataFrame({"Name": [""], "Web URL": [""], "Username": [""], "Password": [""], "Category": [""], "Additional Information": [""]})

class AccountsTable():
    _instance = None
    _passwords_df: pd.DataFrame = DEFAULT_DF

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AccountsTable, cls).__new__(cls)

            text = decrypt_text("data/01.txt")
            res = pd.read_csv(io.StringIO(text), sep = ",")
            cls._passwords_df = res

        return cls._instance
    
    def __init__(self) -> None:
        pass

    @classmethod
    def get_df(cls):
        return cls._passwords_df
    
    @classmethod
    def update_df(cls, updated_df: pd.DataFrame):
        cls._passwords_df = updated_df