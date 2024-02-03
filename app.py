from tkinter import *
import customtkinter as ctk
from PIL import Image
import server 
import client

# FONTS
BUTTON_FONT_BOLD=('Open Sans', 32, 'bold')

# WIDGET ATTRIBUTES
BUTTON_HEIGHT=100
BUTTON_WIDTH=200

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chat Room")
        self.geometry("800x400")
        self.resizable(False, False)

        self.host_button = ctk.CTkButton(self, text="HOST", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT_BOLD, command=self.host)
        self.host_button.grid(row=0, column=0, padx=100, pady=150)

        self.join_button = ctk.CTkButton(self, text="JOIN", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT_BOLD, command=self.join)
        self.join_button.grid(row=0, column=1, padx=100, pady=150)

    def host(self):
        pass

    def join(self):
        pass


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()

