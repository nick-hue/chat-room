from tkinter import *
import customtkinter as ctk
from PIL import Image
import server 
import client

# FONTS
BUTTON_FONT_BOLD=('Open Sans', 32, 'bold')
ENTRY_FONT_BOLD=('Open Sans', 26, 'bold')


# WIDGET ATTRIBUTES
BUTTON_HEIGHT=100
BUTTON_WIDTH=200

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chat Room")
        self.geometry("800x400")
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky=NSEW)

        self.host_button = ctk.CTkButton(self.main_frame, text="HOST", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT_BOLD, command=self.host)
        self.host_button.grid(row=0, column=0, padx=100, pady=150, sticky=NSEW)

        self.join_button = ctk.CTkButton(self.main_frame, text="JOIN", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT_BOLD, command=self.join)
        self.join_button.grid(row=0, column=1, padx=100, pady=150, sticky=NSEW)

    def host(self):
        self.main_frame.grid_forget()

        self.chat_name_var = ctk.StringVar()

        ctk.CTkLabel(self, text="Chat room name: ").grid(row=0, column=0, padx=20, pady=100, sticky=NSEW)
        self.chat_name_entry = ctk.CTkEntry(self, textvariable=self.chat_name_var, font=ENTRY_FONT_BOLD)
        self.chat_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky=NSEW)

        ctk.CTkLabel(self, text="IP ADDRESS: ").grid(row=1, column=0, padx=20, pady=100, sticky=NSEW)
        self.ip_address_entry = ctk.CTkEntry(self, textvariable=self.chat_name_var, font=ENTRY_FONT_BOLD)
        self.ip_address_entry.grid(row=1, column=1, padx=20, pady=10, sticky=NSEW)

        ctk.CTkLabel(self, text="PORT: ").grid(row=2, column=0, padx=20, pady=100, sticky=NSEW)
        self.port_number_entry = ctk.CTkEntry(self, textvariable=self.chat_name_var, font=ENTRY_FONT_BOLD)
        self.port_number_entry.grid(row=2, column=1, padx=20, pady=10, sticky=NSEW)

    def join(self):
        pass


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()

