from tkinter import ttk
import tkinter as tk
import seaborn as sns
import functions




root = tk.Tk()
root.title("Arbeit mit Datasets")
root.geometry("900x500")
root["bg"] = "lightgray"
# skallierbare Fenster. Ich möchte 4 Frames in 1 Spalte
root.grid_columnconfigure(0, weight=1)
for i in range(4):
    root.grid_rowconfigure(i, weight=1)


#### Frame 1. Load Dataset ###
fr_open = tk.Frame(root, bg="lightgray")
fr_open.grid(row=0, column=0,sticky="ew",padx=10, pady=(10,0))

# row 0
tk.Label(fr_open, text="Download Data Set:",font=("Arial",9,"bold"), bg="lightgray").grid(row=0, column=0,columnspan=2, padx=5, pady=(5,2), sticky="w")

# row 1
var_radio = tk.StringVar()
var_radio.set(None)

rad_file = tk.Radiobutton(fr_open, text="Download from file",variable=var_radio, value="file",bg="lightgray",
                          command=lambda: functions.cmd_file(lbl_filename))
rad_file.grid(row=1, column=0,columnspan=2, padx=5, pady=(0,2), sticky="w")

lbl_filename = tk.Label(fr_open, text="", width=20, font=("Arial",10), bg="lightgray")
lbl_filename.grid(row=1, column=2, sticky="",pady=(0,2), padx=5)

# row 2
rad_seaborn = tk.Radiobutton(fr_open, text="Use seaborn Data Set",variable=var_radio, value="sea",bg="lightgray",
                             command=lambda: functions.cmd_sea(lbl_filename))
rad_seaborn.grid(row=2, column=0,columnspan=2, padx=5, pady=(0,5), sticky="w")

seaborn_options = sns.get_dataset_names()
var_opt = tk.StringVar()
var_opt.set(seaborn_options[0])
sea_list = tk.OptionMenu(fr_open, var_opt, *seaborn_options)
sea_list.grid(row=2, column=2,  pady=(0,5), sticky="")

btn_load = tk.Button(fr_open, text="Load",font=("Arial",10,"bold"), bg="lightgreen",
                     command=lambda: functions.cmd_btn_load(var_radio,lbl_load_stat, var_opt))
btn_load.grid(row=2, column=3, padx=5, pady=(0,5), sticky="w")

lbl_load_stat = tk.Label(fr_open, text="", width=40, font=("Arial",10,"bold"), bg="lightgray")
lbl_load_stat.grid(row=2, column=4, columnspan=6,sticky="ew",pady=(0,5), padx=1)



#### Frame 2. Tree status ###
fr_data_view = tk.Frame(root, bg="lightgray")
fr_data_view.grid(row=1, column=0, padx=10, sticky="ew")
fr_data_view.grid_columnconfigure(0, weight=1)


#Frame für Buttons, damit beide nebeneinander in eine Reihe werden
fr_buttons = tk.Frame(fr_data_view, bg="lightgray")
fr_buttons.grid(row=0, column=0,sticky="ew")  

btn_tree = tk.Button(fr_buttons, text="Show Tree", font=("Arial",10,"bold"), bg="lightgreen",
                     command=lambda: functions.show_tree(tree))
btn_tree.pack(side="left", padx=5, pady=5)

btn_del = tk.Button(fr_buttons, text="Delete Tree", font=("Arial",10,"bold"), bg="lightgreen",
                    command= lambda: functions.reset_treeView(tree))
btn_del.pack(side="left", padx=5, pady=5)


#Frame für Tree
fr_tree = tk.Frame(fr_data_view, bg="lightgray")
fr_tree.grid(row=1, column=0,sticky="ew") 

tree = ttk.Treeview(fr_tree, height=3)
tree.grid(row=0, column=1, columnspan=5,rowspan=3,sticky="ew",padx=5)
fr_tree.grid_columnconfigure(1, weight=1)

#Vertikal Scrollbar
vsb = ttk.Scrollbar(fr_tree,orient='vertical', command= tree.yview)
vsb.grid(row=0, column=6,rowspan=3, sticky="ns")
tree.configure(yscrollcommand=vsb.set)

#Horizontal Scrollbar
hsb = ttk.Scrollbar(fr_tree,orient='horizontal', command= tree.xview)
hsb.grid(row=3, column=1, columnspan=5,sticky="ew")
tree.configure(xscrollcommand=hsb.set)





###  Frame 3. Groupby  ###
fr_group = tk.Frame(root, bg="lightgray")
fr_group.grid(row=2, column=0, padx=10,sticky="ew")


#frame for grouping and plot (left)
fr_gr_plot = tk.Frame(fr_group, bg="lightgray")
fr_gr_plot.grid(row=0, column=0, padx=10,sticky="ew")

lbl_groupby = tk.Label(fr_gr_plot, text="Groupby:", font=("Arial",10), bg="lightgray")
lbl_groupby.grid(row=0, column=0,  padx=(5,2))

ent_groupby = tk.Entry(fr_gr_plot, width=15, font=("Arial",10))
ent_groupby.grid(row=0, column=1, padx=(0,10))

lbl_agg = tk.Label(fr_gr_plot, text=".agg:", font=("Arial",10), bg="lightgray")
lbl_agg.grid(row=0, column=2, padx=(0,2))

ent_agg = tk.Entry(fr_gr_plot, width=15, font=("Arial",10))
ent_agg.grid(row=0, column=3, padx=(0,10))

#checkbox
res_ind = tk.BooleanVar()
chk_res_ind = tk.Checkbutton(fr_gr_plot, text="reset_index",bg="lightgray",
                             variable=res_ind)
chk_res_ind.grid(row=0, column=4, padx=10)

btn_apply_group = tk.Button(fr_gr_plot, text="Apply",width=5,font=("Arial",10,"bold"), bg="lightgreen",
                            command= lambda: functions.cmd_apply_group(ent_groupby, ent_agg, res_ind,txt_gr_stat))
btn_apply_group.grid(row=0, column=5, padx=(10,0))

lbl_plot_param= tk.Label(fr_gr_plot, text="Plot type:",font=("Arial",10), bg="lightgray")
lbl_plot_param.grid(row=1, column=0, pady=(10,0), padx=(5,2))

var_plot_opt=tk.StringVar()
plot_options = ["bar", "pie"]
var_plot_opt.set(plot_options[0])
opt_plot= tk.OptionMenu(fr_gr_plot, var_plot_opt, *plot_options)
opt_plot.grid(row=1, column=1, pady=(10,0))

btn_plot = tk.Button(fr_gr_plot, text="Plot",font=("Arial",10,"bold"), bg="lightgreen",
                     command= lambda: functions.cmd_plot(var_plot_opt))
btn_plot.grid(row=1, column=2, pady=(10,0), padx=10)


#frame for group stat (right)
fr_gr_stat = tk.Frame(fr_group,width=25, bg="lightgray")
fr_gr_stat.grid(row=0, column=1, padx=(10,0),sticky="ew")


tk.Label(fr_gr_stat, text="Grouped Dataset", font=("Arial",10), bg="lightgray").grid(row=0,column=0,pady=(0,2),sticky="w")

txt_gr_stat = tk.Text(fr_gr_stat, height=5, width=25, bg="white")
txt_gr_stat.grid(row=1,column=0,pady=(0,10))
# txt_gr_stat.pack(fill="both", expand=True,pady=(0,10))

btn_save = tk.Button(fr_gr_stat, text="Save",font=("Arial",10,"bold"), bg="lightgreen",
                     command= lambda: functions.cmd_save())
btn_save.grid(row=1, column=1, pady=(10),padx=10,sticky="s")



###  Frame 4. Kategories  ###
fr_cut_stat = tk.Frame(root, bg="lightgray")
fr_cut_stat.grid(row=3, column=0, padx=10, sticky="ew")

# Frame cut (left)
fr_cut = tk.Frame(fr_cut_stat, bg="lightgray")
fr_cut.pack(side="left", padx=(0,10))

lbl_neue_spalte = tk.Label(fr_cut, text="Neue Spalte:", font=("Arial",10), bg="lightgray")
lbl_neue_spalte.grid(row=0, column=0, padx=(5,2), pady=(0,10),sticky="n")

ent_neue_spalte = tk.Entry(fr_cut, width=10, font=("Arial",10))
ent_neue_spalte.grid(row=0,column=1,padx=(0,10), pady=(0,10),sticky="n")

lbl_cut_spalte = tk.Label(fr_cut, text="Cut Spalte:", font=("Arial",10), bg="lightgray")
lbl_cut_spalte.grid(row=0, column=2,padx=(5,2), pady=(0,10),sticky="n")

ent_cut_spalte = tk.Entry(fr_cut, width=10, font=("Arial",10))
ent_cut_spalte.grid(row=0, column=3, padx=(0,10), pady=(0,10),sticky="n")

lbl_bins = tk.Label(fr_cut, text="Bins:", font=("Arial",10), bg="lightgray")
lbl_bins.grid(row=1,rowspan=3, column=0, padx=(5,2))

ent_bins = tk.Entry(fr_cut, width=10, font=("Arial",10))
ent_bins.grid(row=1, rowspan=3, column=1, padx=(0,10))

lbl_labels = tk.Label(fr_cut, text="Labels:", font=("Arial",10), bg="lightgray")
lbl_labels.grid(row=1,rowspan=3, column=2, padx=(5,2))

ent_labels = tk.Entry(fr_cut, width=10, font=("Arial",10))
ent_labels.grid(row=1, rowspan=3, column=3, padx=(0,10))

btn_apply_cut = tk.Button(fr_cut, text="Apply",font=("Arial",10,"bold"), bg="lightgreen",
                          command= lambda: functions.cmd_apply_cut(ent_neue_spalte, ent_cut_spalte, ent_bins, ent_labels,txt_cut_stat, tree))
btn_apply_cut.grid(row=1,rowspan=3, column=4, padx=10)

# Frame cut stat (right)
fr_stat = tk.Frame(fr_cut_stat,width=42, bg="lightgray")
fr_stat.pack(side="left",padx=(10,0))

tk.Label(fr_stat, text="Cut status", font=("Arial",10), bg="lightgray").pack(pady=(0,2),anchor="w")

txt_cut_stat = tk.Text(fr_stat, height=5, width=42, bg="white")
txt_cut_stat.pack(fill="both", expand=True, pady=(0,10))


root.mainloop()