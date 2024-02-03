from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import controller
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chat Room")
        self.geometry("400x650")
        self.resizable(False, False)

        self.grid_rowconfigure((0,1,2), weight=1)



if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()

