import tkinter as tk
from tkinter import messagebox

from person_info import SecondWindow

class MainWindow:
    def __init__(self, root):
        self.root = root

        self.root.title("Important Application")
        self.root.geometry("400x170")

        tk.Label(self.root, text = "User name:").grid(column=1, row=2, columnspan=2, pady=5)
        self.username_entry = tk.Entry(self.root, width=20)
        self.username_entry.grid(column=3, row=2, columnspan=2)

        tk.Label(self.root, text="Password:").grid(column=1, row=3, columnspan=2, pady=10)
        self.password_entry = tk.Entry(self.root, width=20)
        self.password_entry.grid(column=3,row=3, columnspan=2)

        self.message_lable = tk.Label(self.root, width=20)
        self.message_lable.grid(column=1,row=4)

        self.btn_login = tk.Button(self.root, text="Login", command=self.login, width=10)
        self.btn_login.grid(column=3,row=4, pady=10)

    def open_second_window(self):
            SecondWindow(self.root)


    def login(self):
        valid_users = {"Ali":111, "Maria":754, "Stefan":666, "1":1}
        name = self.username_entry.get()
        password = self.password_entry.get()
        if name in valid_users and str(password) == str(valid_users[name]):
            self.open_second_window()
            # messagebox.showinfo("Successfull",f"Welcome, {name}!")
        else:
            messagebox.showerror("Error", "Invalid username or password")

  

    

