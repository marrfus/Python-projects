import tkinter as tk


valid_users = {"Ali":111, "Maria":754}

# alle Elementen von rechte Frame löschen
def clean_frame():
    for widget in fr_data.winfo_children():
        widget.destroy()

def login():
        
    def confirm_login():    
        global valid_users
        name = ent_username.get()
        password = ent_password.get()
        if name in valid_users and str(password) == str(valid_users[name]):
            status.set(f"Successfull login\nWelcome, {name}!")
        else:
            status.set(f"!!! ERROR !!!\nInvalid username or password")

    # zuerst alle Elementen von rechte Frame löschen
    clean_frame()
    #dann neue erstellen
    tk.Label(fr_data, text="Username: ", font=("Arial",9), bg="lightgray").grid(row=1, rowspan=2,column=0,pady=5,padx=10, sticky="se")

    ent_username = tk.Entry(fr_data, font=("Arial",11))
    ent_username.grid(row=1, rowspan=2,column=1,pady=5, sticky="sew")

    tk.Label(fr_data, text="Password: ", font=("Arial",9), bg="lightgray").grid(row=3,rowspan=2, column=0,pady=5, padx=10, sticky="ne")

    ent_password = tk.Entry(fr_data, font=("Arial",11),show="*")
    ent_password.grid(row=3,rowspan=2, column=1,pady=5, sticky="new")

    btn_login_recht = tk.Button(fr_data, text="Login", font=("Arial",12),bg="lightgreen", command=confirm_login)
    btn_login_recht .grid(row=5, column=0,columnspan=2, pady=5,padx=20)

    status = tk.StringVar()
    status.set("")
    lbl_status = tk.Label(fr_data, textvariable = status, font=("Arial",9), bg="lightgray")
    lbl_status.grid(row=6,rowspan=2, column=0,columnspan=2,pady=5, padx=10, sticky="new")


def signup():

    def signup_recht():
        global valid_users
        name = ent_username.get()
        password = ent_password.get()
        repeat_pass = ent_repeat_password.get()

        if name in valid_users:
            status.set(f"!!! ERROR !!!\nUser {name} is already exist.")
        elif name != "":
            if password=="":
                status.set(f"!!! ERROR !!!\nYou need to set a password!")
            elif str(password) == str(repeat_pass):
                valid_users[name]=password
                status.set(f"Password for {name} is successfully saved.\nYou can login.")
            else:
                status.set(f"!!! ERROR !!!\nPasswords don't match! Try again.")
        else: 
            status.set(f"!!! ERROR !!!\nEnter your name, please.")

    # zuerst alle Elementen von rechte Frame löschen
    clean_frame()    
    #dann neue erstellen
    tk.Label(fr_data, text="Username: ", font=("Arial",9), bg="lightgray").grid(row=1, rowspan=2,column=0,pady=5,padx=10, sticky="se")

    ent_username = tk.Entry(fr_data, font=("Arial",11))
    ent_username.grid(row=1, rowspan=2,column=1,pady=5, sticky="sew")

    tk.Label(fr_data, text="Password: ", font=("Arial",9), bg="lightgray").grid(row=3,rowspan=2, column=0,pady=5, padx=10, sticky="ne")

    ent_password = tk.Entry(fr_data, font=("Arial",11))
    ent_password.grid(row=3,rowspan=2, column=1,pady=5, sticky="new")

    tk.Label(fr_data, text="repeat\nPassword: ", font=("Arial",9), bg="lightgray").grid(row=5,rowspan=2, column=0,pady=5, padx=10, sticky="ne")

    ent_repeat_password = tk.Entry(fr_data, font=("Arial",11))
    ent_repeat_password.grid(row=5,rowspan=2, column=1,pady=5, sticky="new")

    btn_signup_recht = tk.Button(fr_data, text="Sign up", font=("Arial",12),bg="lightgreen", command=signup_recht)
    btn_signup_recht .grid(row=8, column=0,columnspan=2, pady=5,padx=20)

    status = tk.StringVar()
    status.set("")
    lbl_status = tk.Label(fr_data, textvariable = status, font=("Arial",9), bg="lightgray")
    lbl_status.grid(row=9,rowspan=2, column=0,columnspan=2,pady=5, padx=10, sticky="new")

def about():
    # zuerst alle Elementen von rechte Frame löschen
    clean_frame()
    txt_about = tk.Text(fr_data,  width=35, height=10, font=("Arial", 10), bg="lightgray")
    txt_about.grid(row=0, column=0, padx=10,sticky="ewns")
    txt_about.insert(1.0,"Welcome to a global Login Center!\n\nHere you can just login or not.\nIf you still have no account - no problem.\nJust sign up and enjoy endless loginning!")


root = tk.Tk()
root.geometry("400x300")
root.title("Login/Sign up")
root.configure(bg="lightgray")

# Linkes Frame
fr_btns = tk.Frame(root,height=25,width=100, bg="gray")
fr_btns.grid(row=0, column=0,  padx=10, pady=10, sticky="new")

btn_login = tk.Button(fr_btns, text="Login", font=("Arial",12),bg="lightblue", command=login)
btn_login.grid(row=1, column=0, pady=25,padx=20)

btn_signup = tk.Button(fr_btns, text="Sign up",  font=("Arial",12),bg="lightblue", command=signup)
btn_signup.grid(row=3,column=0,padx=20)

btn_about = tk.Button(fr_btns, text="About", font=("Arial",12),bg="lightblue", command=about)
btn_about.grid(row=5, column=0, pady=60,padx=20)

# Rechtes Frame
fr_data = tk.Frame(root,height=300,width=250, bg="lightgray")
fr_data.grid(row=0, column=1, pady=10, sticky="ew")





root.mainloop()