import customtkinter as ctk


root = ctk.CTk()
root.geometry("500x500")
root.title("Test CTK")

root._set_appearance_mode("Dark")

ctk.CTkButton(root, text="Button",fg_color="blue", corner_radius=30 ).pack()


root.mainloop()