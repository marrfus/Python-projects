import pandas as pd
from os import path
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import seaborn as sns

def cmd_file(lbl_filename):   
    global to_load 
    lbl_filename["bg"]="white"
    #destroy seaborn list?   
    # filename = fd.askopenfilename(title="Open a File", initialdir="C:/Users/MariaSizintseva/Desktop/MariaDocs/marrfusProgBackup/python/Projekt_MS/data_files")
    filename = fd.askopenfilename(title="Open a File")
    if filename:
        if path.isfile(filename):
            lbl_filename["text"]= path.basename(filename)  
            to_load = filename            
    else:
        lbl_filename["text"]="No file selected."


def cmd_sea(lbl):  
    #destroy file label   
    lbl["text"]=""
    lbl["bg"]="lightgray"
    

def cmd_btn_load(var_radio, lbl_load_stat, var_opt):    
    global to_load,df
    #read data from file
    if var_radio.get()=="file":
        #if csv
        if to_load[-4:]==".csv":
            df = pd.read_csv(to_load)
            lbl_load_stat["text"]= ".csv file is sucessfully loaded"
        elif to_load[-5:]== ".xlsx":
            df = pd.read_excel(to_load)
            lbl_load_stat["text"]= ".xlsx file is sucessfully loaded"
        else:
            lbl_load_stat["text"]= "Wrong type of file. Choose another"

    #load from seaborn   
    elif var_radio.get()=="sea":
        sea_dataset = var_opt.get()
        df = sns.load_dataset(sea_dataset)
        lbl_load_stat["text"]= f"Dataset {sea_dataset} is successfully loaded"
    else: 
        lbl_load_stat["text"]= "Choose radiobutton"

    ######  TREE   ######
def show_tree(tree):
    global df
    df_columns = list(df.columns) 

    # Treeview zuerst komplett resetten (Spalten + Inhalte):
    tree.delete(*tree.get_children())
    tree["columns"] = df_columns

    # Sitz: headings anzeigen
    tree["show"] = "headings"   

    # Spalten Definieren (heading)
    for col in df_columns:
        tree.heading(col,text=col)
        tree.column(col, width=100, anchor='center')

    #Convertiere DataFrame in eine Liste von Listen
    if df.shape[0]<500:  
        df_rows = df.astype(str).values.tolist()
    else:  #wenn es zu viel Reihen gibt
        df_rows = df.head(50).astype(str).values.tolist()

    for row in df_rows:
            tree.insert('',tk.END, values=row)

def reset_treeView(tree):    
    children = tree.get_children()
    if children:
        tree.delete(*children)
    tree["columns"] = ()
    tree["show"] = "" 

def cmd_apply_group(ent_groupby, ent_agg, res_ind, txt_gr_stat):
    global df, df_group    
    spalten_liste = [x.strip() for x in ent_groupby.get().split(',')]
    
    #oder mithilfe dictionary
    agg_input = ent_agg.get()  # "tip:mean,total_bill:sum"
    agg_dict = {}
    for item in agg_input.split(','):
        col, func = item.split(':')
        agg_dict[col.strip()] = [func.strip()] 
    if res_ind.get():       
        df_group = df.groupby(spalten_liste, observed=False).agg(agg_dict).reset_index()
    else:
        df_group = df.groupby(spalten_liste, observed=False).agg(agg_dict)

    txt_gr_stat.delete("1.0", "end")
    txt_gr_stat.insert("end", df_group)

def cmd_save():
    # file_path = fd.asksaveasfile(initialdir="C:/Users/MariaSizintseva/Desktop/MariaDocs/marrfusProgBackup/python/Projekt_MS/data_files",
    #                               defaultextension=".csv", title="Save zour file", filetypes=[("CSV File","*.csv"),("All files","*.*")])
    file_path = fd.asksaveasfile(defaultextension=".csv", title="Save zour file", filetypes=[("CSV File","*.csv"),("All files","*.*")])
    df_group.to_csv(file_path)

def cmd_plot(var_plot_opt):
    global df_group  
    match  var_plot_opt.get(): 
        case "bar":
            plt.bar(df_group[df_group.columns[0]],df_group[df_group.columns[1]])
            plt.title(f"Bar plot {df_group.columns[0]} nach {df_group.columns[1]}")
            plt.show()
        case "pie":
            plt.pie(df_group[df_group.columns[1]],labels=df_group[df_group.columns[0]])
            plt.title(f"Pie plot {df_group.columns[0]} nach {df_group.columns[1]}")
            plt.show()

def cmd_apply_cut(ent_neue_spalte, ent_cut_spalte, ent_bins, ent_labels, txt_cut_stat,tree):
    neue_spalte = ent_neue_spalte.get().strip()
    cut_spalte = ent_cut_spalte.get().strip()
    bins_list = [int(x.strip()) for x in ent_bins.get().split(',')]   
    labels_list = [x.strip() for x in ent_labels.get().split(',')]
    df[neue_spalte] = pd.cut(
        df[cut_spalte],
        bins = bins_list,
        labels = labels_list
        )
    show_tree(tree)
    #show new column in frame
    txt_cut_stat.delete("1.0", "end")
    txt_cut_stat.insert("end", df[neue_spalte])

#global vars
# to_load = tk.StringVar()
to_load = ""
df = pd.DataFrame()
df_group = pd.DataFrame()
    
        