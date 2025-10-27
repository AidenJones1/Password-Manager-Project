import tkinter as tk

from ..gui_config import APP_MAIN_BACKGROUND_COLOR, NORMAL_TEXT_FONT, LONG_BUTTON_WIDTH, SMALL_TEXT_FONT, MEDIUM_BUTTON_WIDTH, APP_MAIN_FOREGROUND_COLOR
from ..utilities.button_functions import access_main_page, access_master_password_page
from ..utilities.gui import visual_grid

class LoginPage(tk.Frame):
    def __init__(self, parent: tk.Frame, application):
        tk.Frame.__init__(self, parent)

        # Frame configuration
        self.configure(bg = APP_MAIN_BACKGROUND_COLOR)

        # Grid configuration
        self.rowconfigure((0, 3), weight = 3, uniform = "row")
        self.rowconfigure((1, 2), weight = 1, uniform = "row")
        self.columnconfigure((0, 1, 3, 4), weight = 10, uniform = "column")
        self.columnconfigure(2, weight = 1, uniform = "column")

        #visual_grid(self, 4, 5)

        # Password Label
        enter_password_label = tk.Label(self)
        enter_password_label.config(
            text = "Enter Password:",
            font = NORMAL_TEXT_FONT,
            foreground = APP_MAIN_FOREGROUND_COLOR,
            background = APP_MAIN_BACKGROUND_COLOR)
        enter_password_label.grid(row = 1, column = 1, sticky = "e", padx = 5)
        
        # Password Entry
        password_entry = tk.Entry(self)
        password_entry.config(
            show = "•",
            font = NORMAL_TEXT_FONT)
        password_entry.grid(row = 1, column = 2, columnspan = 2, sticky = "w")

        # Login Button
        login_button = tk.Button(self)
        login_button.config(
            text = "Login",
            font = NORMAL_TEXT_FONT,
            width = LONG_BUTTON_WIDTH,
            command = lambda: access_main_page(application, password_entry))
        login_button.grid(row = 2, column = 1, columnspan = 3)

        # Change Master Password Button
        master_password_button = tk.Button(self)
        master_password_button.config(
            text = "Change Password",
            font = SMALL_TEXT_FONT,
            width = MEDIUM_BUTTON_WIDTH,
            command = lambda: access_master_password_page(application, password_entry))
        master_password_button.grid(row = 3, column = 4, sticky = "se", padx = 25, pady = 25)