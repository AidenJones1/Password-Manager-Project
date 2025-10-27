from tkinter import messagebox, Entry, END, filedialog, simpledialog
import pandas as pd

from ..utilities.login import attempt_login, change_master_password
from ..table.table import DEFAULT_DF, PASSWORDS_FILE_PATH, AccountsTable
from ..table.table_gui import MyTableGUI
from encryption.encryption import encrypt_text, decrypt_text

FILE_TYPES = [('Comma Separated Values', '*.csv')]

def access_main_page(application, entry: Entry):
    """Attempt to access the main page through the application. Show error message if denied."""
    successful_login = attempt_login(entry.get())

    if successful_login:
        entry.delete(0, END)
        application.show_page(1)

    else:
        messagebox.showwarning("Incorrect Password!", "The password you have entered is incorrect!")

def access_master_password_page(application, entry: Entry):
    """Access the main page through the application."""
    entry.delete(0, END)
    application.show_page(2)

def access_login_page(application, entries: list[Entry] = []):
    """Access the login page and reset any entries from the current page."""
    for entry in entries:
        entry.delete(0, END)

    application.show_page(0)

def change_password_confirm(application, current_password_entry: Entry, new_password_entry: Entry):
    """Attempt to change the master password to the application."""
    current_password = current_password_entry.get()
    new_password = new_password_entry.get()

    # Check if passwords are the same
    if current_password == new_password:
        messagebox.showwarning("Duplicate Password", "New password cannot be the same as the current password!")
        return

    # Confirm with the user
    confirm = messagebox.askyesno("Change Password?", "Are you sure you want to change the password?")

    if not confirm:
        return
    
    # Change Password
    successful_login = attempt_login(current_password)

    if successful_login:
        current_password_entry.delete(0, END)
        new_password_entry.delete(0, END)

        change_master_password(new_password)
        application.show_page(0)

    else:
        messagebox.showwarning("Incorrect Password!", "The current password you have entered is incorrect!")

def export_table(table_df: pd.DataFrame):
    """Attempt to export the table and save it as a .csv file"""
    file = filedialog.asksaveasfile(mode = "w", filetypes = FILE_TYPES, defaultextension = ".csv")

    # User cancel export
    if file is None:
        return
    
    text = table_df.to_csv(index = False, lineterminator = "\n")
    file.write(text)
    file.close()

def import_table(table: MyTableGUI):
    """Attempt to import a .csv file to be use as the table."""
    filepath = filedialog.askopenfile(title = "Select a file", initialdir = "/", filetypes = FILE_TYPES)

    # User cancels import
    if filepath is None:
        return
    
    try:
        new_table= pd.read_csv(filepath, low_memory = False)

        required_columns = list(DEFAULT_DF.columns)

        # Check for missing columns
        missing_columns = [c for c in required_columns if c not in new_table.columns]
        if missing_columns:
            return
        
        # Grab only the required columns in the order and normalize missing values
        selected_df = new_table[required_columns].copy().fillna("")

        table.model.df = selected_df
        table.redraw()

    except:
        return
    
def save_table(table_df: pd.DataFrame, skip_ask: bool = False):
    """Attempt to save the current table."""
    if skip_ask:
        save = True

    else:
        save = messagebox.askyesno("Save table?", "Save the current table?")

    if save:
        text = table_df.to_csv(lineterminator = "\n", index = False).encode()
        encrypt_text(text, PASSWORDS_FILE_PATH)

def remove_selected_row(table: MyTableGUI):
    """Remove the currently selected row."""
    remove = messagebox.askyesno("Remove Row?", "Do you want to remove the selected row?")

    if remove:
        table.deleteRow()
        table.model.resetIndex(drop = True)

def add_row(table: MyTableGUI):
    """Add a number of empty rows to the table specified by the user."""
    num = simpledialog.askinteger("Add Rows", "Add number of rows:")

    if num is None:
        return
    
    if num <= 0:
        messagebox.showerror(message = "Invalid input!")
        return 
    
    table.addRows(num)
    
    AccountsTable.update_df(table.get_df())