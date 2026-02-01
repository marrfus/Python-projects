import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox

from person import Person

root = tk.Tk()
root.geometry("800x600")
root["bg"] = "lightblue"

def submit ():
    p = Person(name_entry.get(), gender.get(),eyeColor.get(), height_entry.get(), weight_entry.get())
    messagebox.showinfo("Person Info", str(p))
    

image_frame = tk.Frame(root, width=100, height=50, bg="#696969")
image_frame.grid(column=0, row=0, rowspan=5)



image = PhotoImage(file="kuri.png")
# image = image.subsample(5,5)

image_lable = tk.Label(image_frame, image = image)
image_lable.pack(padx=10, pady=10)

# tk.Label(root, text = "Name").grid(column=1, row=0)
# tk.Label(root, text = "Gender").grid(column=1, row=1)
# tk.Label(root, text = "Eye Color").grid(column=1, row=2)
# tk.Label(root, text = "Height (cm)").grid(column=1, row=3)
# tk.Label(root, text = "Weight (kg)").grid(column=1, row=4)

for i,elemnt in enumerate(["Name", "Gender", "Eye Color", "Height (cm)", "Weight (kg)"]):
    tk.Label(root, text = f"{elemnt}:", font=("Arial",14),bg="lightblue").grid(column=1, row=i, sticky="e",padx=5)

name_entry = tk.Entry( font=("Arial",14))
name_entry.grid(column=2, row=0, columnspan=2)

gender = tk.StringVar()
gender_combx = ttk.Combobox(root,width=20, textvariable=gender, font=("Arial",14))
gender_combx['values']=("Male", "Female")
gender_combx.grid(column=2, row=1, columnspan=2)
gender_combx.current(0)

eyeColor = tk.StringVar()
eyeColor_combx = ttk.Combobox(root,width=20, textvariable=eyeColor, font=("Arial",14))
eyeColor_combx['values']=("Braun", "Blue", "Black", "Olive", "Honey")
eyeColor_combx.grid(column=2, row=2, columnspan=2)
eyeColor_combx.current(0)

height_entry = tk.Entry( font=("Arial",14))
height_entry.grid(column=2, row=3, columnspan=2)

weight_entry = tk.Entry( font=("Arial",14))
weight_entry.grid(column=2, row=4, columnspan=2)

submit_btn = tk.Button(root, text="Submit",font=("Arial",14,"bold"), command=submit)
submit_btn.grid(column=3, row=5, columnspan=2)

root.mainloop()