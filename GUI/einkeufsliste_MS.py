import tkinter as tk


def press_enter(event):
    ein_list.insert(tk.END, entry_el.get())
    entry_el.delete(0,tk.END)

def list_update():
    upd_val = entry_el.get()
    ein_list.insert(tk.END, upd_val)
    entry_el.delete(0,tk.END)
    

root = tk.Tk()
root.title("Einkaufsliste")
root.geometry("400x300")

tk.Label(root, text="Was fügen wir in die Liste hinzu?").pack()

entry_el = tk.Entry(root)
entry_el.pack(pady=5)
entry_el.bind("<Return>", press_enter)

btn = tk.Button(root, text = "Einfügen", command=list_update)
btn.pack()

tk.Label(root, text="Heute zu kaufen:").pack(pady=7)
ein_list = tk.Listbox(root, height=5)
ein_list.pack()

root.mainloop()