from pandastable import Table
from .table import AccountsTable
import tkinter as tk
import string
import random

class MyTableGUI(Table):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MyTableGUI, cls).__new__(cls)

        return cls._instance
    
    def __init__(self, master, generate_password_button: tk.Button, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.generate_password_button = generate_password_button
        self.showtoolbar = False
        self.showstatusbar = False
        self.enable_menus = False
    
    def handle_double_click(self, event):
        rowclicked = self.get_row_clicked(event)
        colclicked = self.get_col_clicked(event)

        # Get cell value at row and column
        cell_value = None
        if rowclicked is not None and colclicked is not None:
            try:
                cell_value = self.model.df.iat[rowclicked, colclicked]
            except:
                try:
                    cell_value = self.model.df.iloc[rowclicked, colclicked]
                except:
                    cell_value = None

        # keep the last double-clicked cell info for later use
        self._last_double_clicked = {"row": rowclicked, "col": colclicked, "value": cell_value}
        
        if colclicked == 3:
            self.generate_password_button.config(
                state = tk.ACTIVE,
                command = lambda: self.generate_password(rowclicked))

        else:
            self.generate_password_button.config(state = tk.DISABLED)

        super().handle_double_click(event)

    def get_df(self):
        return self.model.df
    
    def generate_password(self, index):
        """Generates a 15-18 character password containing at least an uppercase letter, a lowercase letter, a number,
        and a special character."""
        characterlist = "" + string.ascii_letters + string.digits + string.punctuation

        while True:
            generated_password = ""

            for i in range(random.randint(15, 18)):
                randomchar = random.choice(characterlist)
                generated_password += randomchar

            hasCapital = False
            hasLower = False
            hasDigit = False
            hasSpecialChar = False
            for character in generated_password:
                if hasCapital == False and character.isupper():
                    hasCapital = True

                elif hasLower == False and character.islower():
                    hasLower = True

                elif hasDigit == False and character.isdigit():
                    hasDigit = True

                elif hasSpecialChar == False and character in string.punctuation:
                    hasSpecialChar = True

                if hasCapital and hasLower and hasDigit and hasSpecialChar:
                    df = self.get_df().copy()
                    df.at[index, "Password"] = generated_password

                    self.clearSelected()
                    self.generate_password_button.config(state = tk.DISABLED)

                    self.model.df = df
                    AccountsTable().update_df(df)

                    self.redraw()
                    return
                