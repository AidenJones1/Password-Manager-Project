import tkinter as tk

from ..gui_config import APP_MAIN_BACKGROUND_COLOR, NORMAL_TEXT_FONT, APP_MAIN_FOREGROUND_COLOR, LONG_BUTTON_WIDTH, SMALL_TEXT_FONT, SMALL_BUTTON_WIDTH
from ..utilities.button_functions import change_password_confirm, access_login_page
from ..utilities.gui import visual_grid

class MasterPasswordPage(tk.Frame):
    def __init__(self, parent: tk.Frame, application):
        tk.Frame.__init__(self, parent)

        # Frame configuration
        self.configure(bg = APP_MAIN_BACKGROUND_COLOR)

        # Grid configuration
        self.rowconfigure((0, 4), weight = 3, uniform = "row")
        self.rowconfigure((1, 2, 3), weight = 1, uniform = "row")
        self.columnconfigure((0, 1, 3, 4), weight = 10, uniform = "column")
        self.columnconfigure(2, weight = 1, uniform = "column")

        #visual_grid(self, 5, 5)

        # Current Password Label
        current_password_label = tk.Label(self)
        current_password_label.config(
            text = "Current Password:",
            font = NORMAL_TEXT_FONT,
            background = APP_MAIN_BACKGROUND_COLOR,
            foreground = APP_MAIN_FOREGROUND_COLOR)
        current_password_label.grid(row = 1, column = 1, sticky = "es", padx = 5)

        # Current Password Entry
        current_password_entry = tk.Entry(self)
        current_password_entry.config(
            show = "•",
            font = NORMAL_TEXT_FONT)
        current_password_entry.grid(row = 1, column = 2, columnspan = 2, sticky = "sw")

        # New Password Label
        new_password_label = tk.Label(self)
        new_password_label.config(
            text = "New Password:",
            font = NORMAL_TEXT_FONT,
            background = APP_MAIN_BACKGROUND_COLOR,
            foreground = APP_MAIN_FOREGROUND_COLOR)
        new_password_label.grid(row = 2, column = 1, sticky = "e", padx = 5)

        # New Password Entry
        new_password_entry = tk.Entry(self)
        new_password_entry.config(
            show = "•",
            font = NORMAL_TEXT_FONT)
        new_password_entry.grid(row = 2, column = 2, columnspan = 2, sticky = "w")

        # Confirm Button
        confirm_button = tk.Button(self)
        confirm_button.config(
            text = "Change Password",
            font = NORMAL_TEXT_FONT,
            width = LONG_BUTTON_WIDTH,
            command = lambda: change_password_confirm(application, current_password_entry, new_password_entry))
        confirm_button.grid(row = 3, column = 1, columnspan = 3, sticky = "n", pady = 5)

        # Cancel Button
        cancel_button = tk.Button(self)
        cancel_button.config(
            text = "Back",
            font = SMALL_TEXT_FONT,
            width = SMALL_BUTTON_WIDTH,
            command = lambda: access_login_page(application, [current_password_entry, new_password_entry]))
        cancel_button.grid(row = 0, column = 0, sticky = "nw", padx = 25, pady = 25)