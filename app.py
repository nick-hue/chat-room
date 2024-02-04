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
        #self.geometry("800x400")
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky=NSEW)

        self.host_button = ctk.CTkButton(self.main_frame, text="HOST", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT_BOLD, command=self.host)
        self.host_button.grid(row=0, column=0, padx=100, pady=150, sticky=NSEW)

        self.join_button = ctk.CTkButton(self.main_frame, text="JOIN", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT_BOLD, command=self.join)
        self.join_button.grid(row=0, column=1, padx=100, pady=150, sticky=NSEW)

    def host(self):
        self.main_frame.destroy()
        self.host_frame = ctk.CTkFrame(self, corner_radius=0)
        self.host_frame.grid(row=0, column=0, sticky=NSEW)

        entry_width = 200
        entry_height = 20
        
        self.chat_name_var = ctk.StringVar()
        self.chat_name_var.set("Chat Room")
        ctk.CTkLabel(self.host_frame, text="Chat room name: ", font=ENTRY_FONT_BOLD, anchor='w').grid(row=0, column=0, padx=20, pady=20, sticky=NSEW)
        self.chat_name_entry = ctk.CTkEntry(self.host_frame, textvariable=self.chat_name_var, width=entry_width, height=entry_height, font=ENTRY_FONT_BOLD)
        self.chat_name_entry.grid(row=0, column=1, padx=20, pady=10)

        self.ip_address_var = ctk.StringVar()
        self.ip_address_var.set('127.0.0.1')
        ctk.CTkLabel(self.host_frame, text="IP ADDRESS: ", font=ENTRY_FONT_BOLD, anchor='w').grid(row=1, column=0, padx=20, pady=20, sticky=NSEW)
        self.ip_address_entry = ctk.CTkEntry(self.host_frame, textvariable=self.ip_address_var, width=entry_width, height=entry_height, font=ENTRY_FONT_BOLD)
        self.ip_address_entry.grid(row=1, column=1, padx=20, pady=10)

        self.port_number_var = ctk.StringVar()
        self.port_number_var.set(12345)
        ctk.CTkLabel(self.host_frame, text="PORT: ", font=ENTRY_FONT_BOLD, anchor='w').grid(row=2, column=0, padx=20, pady=20, sticky=NSEW)
        self.port_number_entry = ctk.CTkEntry(self.host_frame, textvariable=self.port_number_var, width=entry_width, height=entry_height, placeholder_text=12345, font=ENTRY_FONT_BOLD)
        self.port_number_entry.grid(row=2, column=1, padx=20, pady=10)

        self.bind('<Return>', self.make_chat_room)

        self.make_chat_button = ctk.CTkButton(self.host_frame, text="Host", font=BUTTON_FONT_BOLD, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=self.make_chat_room)
        self.make_chat_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

    def make_chat_room(self, *args):
        print(f"Creating chat room [{self.chat_name_var.get()}] in {self.ip_address_var.get()}:{self.port_number_var.get()}")
        server.host_connection(self.ip_address_var.get(), self.port_number_var.get(), 2)

        self.host_frame.destroy()

        self.chat



    def join(self):
        pass


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()

