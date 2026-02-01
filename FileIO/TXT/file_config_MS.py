import tkinter as tk
import os

absolut_path = os.path.abspath(__file__)
folder_path = os.path.dirname(absolut_path)

def open_file():
    text_el.delete(1.0, tk.END)
    file_name = entry_el.get()
    try:
        with open(f"{folder_path}/{file_name}", "r+") as file:
            inhalt = file.read()
            text_el.insert(tk.END, inhalt)
            txt.set(f"Status: {file_name} opend successfully")
    except FileNotFoundError:        
        txt.set(f"Error: File {file_name} not found.")



def save_file():
    file_name = entry_el.get()
    try:
        with open(f"{folder_path}/{file_name}", "w") as file:
            text_box_inhalt = text_el.get("1.0",tk.END)
            file.write(text_box_inhalt)
            text_el.delete(1.0, tk.END)# 1 Zeile, Zeichen index 0
            txt.set(f"Status: {file_name} is successfully saved.")
            entry_el.delete(0,tk.END)# 0 index          
    except FileNotFoundError:
        txt.set(f"Error: File {file_name} not found.")


root = tk.Tk()
root.geometry("460x500")
root.title("Datei Aufgabe")
root.configure(bg="lightgray")

tk.Label(root, text="File Name:", font=("Arial",12), bg="lightgray").grid(row=0, column=0,padx=3,pady=5,sticky="e")

entry_el = tk.Entry(root, font=("Arial",12))
entry_el.grid(row=0, column=1,padx=5, sticky="ew",pady=5)

btn_open = tk.Button(root, text="Open",font=("Arial",12),bg="lightblue",command=open_file)
btn_open.grid(row=0,column=2,padx=5, sticky="e",pady=5)
btn_save = tk.Button(root, text="Save",font=("Arial",12),bg="lightblue",command=save_file)
btn_save.grid(row=0,column=3,padx=5, sticky="e",pady=5)

text_el = tk.Text(root, width=30, height=25)
text_el.grid(row=1, column=0, rowspan=3, columnspan=4,padx=10,pady=10,sticky="ew")

txt=tk.StringVar()
txt.set("Status: ")
stat_label = tk.Label(root, textvariable=txt, font=("Arial",12),bg="lightgray")
stat_label.grid(row=4, column=0, columnspan=4, sticky="w")


root.mainloop()