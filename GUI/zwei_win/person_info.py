
import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from person import Person

class SecondWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Person Info")
        self.window.geometry("800x500")
        self.window["bg"] = "lightblue"


        self.image_frame = tk.Frame(self.window, width=100, height=50, bg="#696969")
        self.image_frame.grid(column=0, row=0, rowspan=5)

        self.image = PhotoImage(file="kuri.png")
        # self.image = self.image.subsample(5,5)

        self.image_lable = tk.Label(self.image_frame, image = self.image)
        self.image_lable.image = self.image
        self.image_lable.pack(padx=10, pady=10)

        # tk.Label(root, text = "Name").grid(column=1, row=0)
        # tk.Label(root, text = "Gender").grid(column=1, row=1)
        # tk.Label(root, text = "Eye Color").grid(column=1, row=2)
        # tk.Label(root, text = "Height (cm)").grid(column=1, row=3)
        # tk.Label(root, text = "Weight (kg)").grid(column=1, row=4)

        for i,elemnt in enumerate(["Name", "Gender", "Eye Color", "Height (cm)", "Weight (kg)"]):
            tk.Label(self.window, text = f"{elemnt}:", font=("Arial",14),bg="lightblue").grid(column=1, row=i, sticky="w", padx=5)

        self.name_entry = tk.Entry(self.window, font=("Arial",14))
        self.name_entry.grid(column=2, row=0, columnspan=2)

        self.gender = tk.StringVar(self.window)
        self.gender_combx = ttk.Combobox(self.window,width=20, textvariable=self.gender, font=("Arial",14))
        self.gender_combx['values']=("Male", "Female")
        self.gender_combx.grid(column=2, row=1, columnspan=2)
        self.gender_combx.current(0)

        self.eyeColor = tk.StringVar(self.window)
        self.eyeColor_combx = ttk.Combobox(self.window,width=20, textvariable=self.eyeColor, font=("Arial",14))
        self.eyeColor_combx['values']=("Braun", "Blue", "Black", "Olive", "Honey")
        self.eyeColor_combx.grid(column=2, row=2, columnspan=2)
        self.eyeColor_combx.current(0)

        self.height_entry = tk.Entry(self.window, font=("Arial",14))
        self.height_entry.grid(column=2, row=3)

        self.weight_entry = tk.Entry(self.window, font=("Arial",14))
        self.weight_entry.grid(column=2, row=4)

        self.submit_btn = tk.Button(self.window, text="Submit", font=("Arial",14,"bold"), command=self.submit)
        self.submit_btn.grid(column=2, row=5, columnspan=2)



    def submit (self):
        p = Person(self.name_entry.get(), self.gender.get(), self.eyeColor.get(), self.height_entry.get(), self.weight_entry.get())
        messagebox.showinfo("Person Info", str(p))



