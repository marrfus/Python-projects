import tkinter as tk
from tkinter import messagebox



def login():
    valid_users = {"Ali":111, "Maria":754, "Stefan":666, "1":1}
    name = username_entry.get()
    password = password_entry.get()
    if name in valid_users and str(password) == str(valid_users[name]):
        messagebox.showinfo("Successfull",f"Welcome, {name}!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

window = tk.Tk()

window.title("Important Application")
window.geometry("500x400")

tk.Label(window, text = "User name:").grid(column=1, row=2, columnspan=2)
username_entry = tk.Entry(window, width=30)
username_entry.grid(column=3, row=2)

tk.Label(window, text="Password:").grid(column=1, row=3, columnspan=2)
password_entry = tk.Entry(window, width=30)
password_entry.grid(column=3,row=3)

message_lable = tk.Label(window, width=30)
message_lable.grid(column=1,row=4)

btn_login = tk.Button(window, text="Login", command=login, width=10)
btn_login.grid(pady=10)

# --- Start ---
window.mainloop()