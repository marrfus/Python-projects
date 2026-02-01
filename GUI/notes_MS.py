
import tkinter as tk

def sum_calc():
    return sum([int(mathe_entry.get()), int(physic_entry.get()), int(deutsch_entry.get()), int(bio_entry.get())])

def calc_sum():
    # summe = sum([int(mathe_entry.get()), int(physic_entry.get()), int(deutsch_entry.get()), int(bio_entry.get())])
    summe = sum_calc()
    old_val = calc_lable['text']
    if "Avg" in old_val and "Sum" not in old_val:
        calc_lable.config(text = f"Sum: {summe}  {old_val}")
    else:
        calc_lable.config(text = f"Sum: {summe}")

        
    
def calc_avg():
    # avg = sum([int(mathe_entry.get()), int(physic_entry.get()), int(deutsch_entry.get()), int(bio_entry.get())])/4
    avg = sum_calc()/4
    old_val = calc_lable['text']
    
    calc_lable.config(text = f"Avg: {avg}  {old_val}")
window = tk.Tk()

window.title("Notes")
window.geometry("400x300")

mathe = tk.Label(window, text = "Mathe", font=("Arial",12), bg="light blue", width=10, height=1)
mathe.grid(row=1, column=0, padx=10, pady=10)
mathe_entry = tk.Entry(window)
mathe_entry.grid(row=1, column=1, padx=10, pady=10)

deutsch = tk.Label(window, text = "Deutsch", font=("Arial",12), bg="light blue", width=10, height=1)
deutsch.grid(row=3, column=0, padx=10, pady=10)
deutsch_entry = tk.Entry(window)
deutsch_entry.grid(row=3, column=1, padx=10, pady=10, )

physic = tk.Label(window, text = "Physic", font=("Arial",12), bg="light blue", width=10, height=1)
physic.grid(row=5, column=0, padx=10, pady=10)
physic_entry = tk.Entry(window)
physic_entry.grid(row=5, column=1, padx=10, pady=10)

bio = tk.Label(window, text = "Biology", font=("Arial",12), bg="light blue", width=10, height=1)
bio.grid(row=7, column=0, padx=10, pady=10)
bio_entry = tk.Entry(window)
bio_entry.grid(row=7, column=1,padx=10, pady=10)

btn_sum = tk.Button(window, text = "Sum", font=("Arial",12), bg="light yellow", width=5, command=calc_sum)
btn_sum.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="e")

btn_avg = tk.Button(window, text = "Avg", font=("Arial",12), bg="light yellow", width=5, command=calc_avg)
btn_avg.grid(row=9, column=1, columnspan=2,padx=10, pady=10, sticky="w")

calc_lable = tk.Label(window, font=("Arial",12,"bold"))
calc_lable.grid(column=1, row=10, columnspan=3)
# --- Start ---
window.mainloop()
