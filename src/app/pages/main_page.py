#TODO: Fix columns not showing
import tkinter as tk

from ..gui_config import APP_MAIN_BACKGROUND_COLOR, SMALL_BUTTON_WIDTH, SMALL_TEXT_FONT, NORMAL_TEXT_FONT, MEDIUM_BUTTON_WIDTH
from ..utilities.gui import visual_grid
from ..utilities.button_functions import access_login_page, export_table, import_table, save_table, remove_selected_row, add_row
from ..utilities.search import perform_search
from ..table.table_gui import MyTableGUI
from ..table.table import AccountsTable

class MainPage(tk.Frame):
    def search_callback(self, var, index, mode):
        res_df = perform_search(self.search_entry.get())

        self.accounts_table.model.df = res_df
        self.accounts_table.redraw()

    def __init__(self, parent: tk.Frame, application):
        tk.Frame.__init__(self, parent)

        # Frame configuration
        self.configure(bg = APP_MAIN_BACKGROUND_COLOR)

        # Grid configuration
        self.columnconfigure((0, 1, 2, 3, 4, 6, 7, 8, 10), weight = 1, uniform = "column")
        self.columnconfigure(9, weight = 2, uniform = "column")
        self.columnconfigure(5, weight = 3, uniform = "column")
        self.rowconfigure(0, weight = 2, uniform = "row")
        self.rowconfigure(1, weight = 8, uniform = "row")
        self.rowconfigure((2, 3), weight = 1, uniform = "row")

        #visual_grid(self, 4, 11)

        # Back Button
        self.back_button = tk.Button(self)
        self. back_button.config(
            text = "Back",
            font = SMALL_TEXT_FONT,
            width = MEDIUM_BUTTON_WIDTH,
            command = lambda: access_login_page(application, [self.search_entry]))
        self.back_button.grid(row = 0, column = 0, sticky = "nw", padx = 25, pady = 25)

        # Search Bar
        self.entry_var = tk.StringVar()
        self.entry_var.trace_add("write", self.search_callback)

        self.search_entry = tk.Entry(self)
        self.search_entry.config(
            font = NORMAL_TEXT_FONT,
            textvariable = self.entry_var)
        self.search_entry.grid(row = 0, column = 5, sticky = "sew", pady = 10)

        # Import Button
        self.import_button = tk.Button(self)
        self.import_button.config(
            text = "Import",
            width = SMALL_BUTTON_WIDTH,
            command = lambda: import_table(self.accounts_table))
        self.import_button.grid(row = 2, column = 1, sticky = "n", pady = 10)

        # Export Button
        self.export_button = tk.Button(self)
        self.export_button.config(
            text = "Export",
            width = SMALL_BUTTON_WIDTH,
            command = lambda: export_table(self.accounts_table.get_df()))
        self.export_button.grid(row = 2, column = 2, sticky = "n", pady = 10)

        # Save Button
        self.save_button = tk.Button(self)
        self.save_button.config(
            text = "Save",
            width = SMALL_BUTTON_WIDTH,
            command = lambda: save_table(self.accounts_table.get_df()))
        self.save_button.grid(row = 2, column = 3, sticky = "n", pady = 10)

        # Add Button
        self.add_button = tk.Button(self)
        self.add_button.config(
            text = "Add",
            width = SMALL_BUTTON_WIDTH,
            command = lambda: add_row(self.accounts_table))
        self.add_button.grid(row = 2, column = 7, sticky = "n", pady = 10)

        # Remove Button
        self.remove_button = tk.Button(self)
        self.remove_button.config(
            text = "Remove",
            width = SMALL_BUTTON_WIDTH,
            command = lambda: remove_selected_row(self.accounts_table))
        self.remove_button.grid(row = 2, column = 8, sticky = "n", pady = 10)

        # Generate Password
        self.generate_password_button = tk.Button(self)
        self.generate_password_button.config(
            text = "Generate Password",
            state = tk.DISABLED)
        self.generate_password_button.grid(row = 2, column = 9, sticky = "n", pady = 10)

        # Accounts Table Widget
        self.table_frame = tk.Frame(self)
        self.table_frame.grid(row = 1, column = 0, columnspan = 11, sticky = "nsew", padx = 5)

        df = AccountsTable().get_df().copy()

        self.accounts_table = MyTableGUI(
            master = self.table_frame,
            generate_password_button = self.generate_password_button)
        
        # DataFrame contains no rows other than the header
        if df.empty:
            tmp = df.copy()
            tmp.loc[0] = ["" for _ in tmp.columns] # Create empty row
            df_to_show = tmp
                       
        else: 
            df_to_show = df

        self.accounts_table.model.df = df_to_show 
        self.accounts_table.show()

        for i in range(len(df.columns)):
            self.accounts_table.resizeColumn(i, 200)

        self.accounts_table.redraw()
