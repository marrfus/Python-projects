import customtkinter as ctk
import csv

def add_data():
    name = ent_name.get()
    age = ent_age.get()
    city = ent_city.get()
    data = [name, age, city]

    #Writer
    with open("my.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    #data löschen!!
    ent_name.delete(0,ctk.END)
    ent_age.delete(0,ctk.END)
    ent_city.delete(0,ctk.END)


def show_data():
    #zuerst delete text in textbox
    txt_box.delete(1.0,ctk.END)
    #Reader
    with open("my.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            data_line = ", ".join(line)
            txt_box.insert(ctk.END,f"{data_line}\n")


root = ctk.CTk()
root.geometry("300x300")
root.title("Info Enter")
root.configure(fg_color="lightgray")

ctk.CTkLabel(root, text="Name: ", font=("Arial",11),bg_color="lightgray").place(x=20, y=20)
ent_name = ctk.CTkEntry(root, font=("Arial",11))
ent_name.place(x=60, y=20)

ctk.CTkLabel(root, text="Age: ", font=("Arial",11),bg_color="lightgray").place(x=20, y=60)
ent_age = ctk.CTkEntry(root, font=("Arial",11))
ent_age.place(x=60, y=60)

ctk.CTkLabel(root, text="City: ", font=("Arial",11),bg_color="lightgray").place(x=20, y=100)
ent_city = ctk.CTkEntry(root, font=("Arial",11))
ent_city.place(x=60, y=100)

btn_add = ctk.CTkButton(root, text="   Add   ", font=("Arial",11),width=30, fg_color="blue", command=add_data)
btn_add.place(x=210, y=100)

btn_show = ctk.CTkButton(root, text="Show all", font=("Arial",11),width=30, fg_color="blue", command=show_data)
btn_show.place(x=210, y=140)

txt_box = ctk.CTkTextbox(root, width=260, height=80)
txt_box.place(x=20, y=180)



root.mainloop()