"""This modules manages the application."""
import tkinter as tk

from app.pages.app_login_page import LoginPage
from app.pages.main_page import MainPage
from app.pages.master_password_page import MasterPasswordPage
from app.utilities.gui import center_window
import app.gui_config as gui
from resources import resource_path

STARTING_PAGE = 0

PAGES = [LoginPage, MainPage, MasterPasswordPage]

class App(tk.Tk):
    _instance = None

    # Ensure only one instance exist
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)

        return cls._instance

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Window Setup
        self.title(gui.WINDOW_TITLE)

        icon = tk.PhotoImage(file = resource_path(gui.WINDOW_ICON_FILE_PATH))
        self.iconphoto(False, icon)

        self.geometry(gui.WINDOW_SIZE)
        self.resizable(gui.CAN_RESIZE_WINDOW_WIDTH, gui.CAN_RESIZE_WINDOW_HEIGHT)

        center_window(self)

        # Pages Setup
        main_view = tk.Frame(self)
        main_view.pack(side = "top", fill = "both", expand = True)

        main_view.grid_rowconfigure(0, weight = 1)
        main_view.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        self.pages = PAGES

        for F in self.pages:
            frame = F(main_view, self)

            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_page(STARTING_PAGE)


    def open(self):
        """Open the application."""
        self.mainloop()

    def show_page(self, page_number: int):
        """Show the specified page.\n
        Page Numbers:\n
        0 = Login Page\n
        1 = Main Page\n
        2 = Master Password Page\n"""

        frame = self.frames[self.pages[page_number]]
        frame.tkraise()
        