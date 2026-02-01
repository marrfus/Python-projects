import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        self.root = root
        root.title("Hauptfenster")

        ttk.Button(root, text="Zweites Fenster öffnen",
                   command=self.open_second_window).pack(pady=10)

        # Label, das durch das zweite Fenster verändert werden soll
        self.label = ttk.Label(root, text="Noch keine Eingabe")
        self.label.pack(pady=10)

    def open_second_window(self):
        SecondWindow(self)

class SecondWindow:
    def __init__(self, main_window):
        self.main = main_window

        self.window = tk.Toplevel()
        self.window.title("Zweites Fenster")

        self.entry = ttk.Entry(self.window)
        self.entry.pack(pady=10)

        ttk.Button(self.window, text="An Hauptfenster senden",
                   command=self.send_to_main).pack(pady=10)

    def send_to_main(self):
        text = self.entry.get()
        self.main.label.config(text=f"Eingabe: {text}")
        self.window.destroy()

root = tk.Tk()
app = MainWindow(root)
root.mainloop()