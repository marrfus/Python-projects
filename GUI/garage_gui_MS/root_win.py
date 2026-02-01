
import tkinter as tk
from tkinter import ttk
from garage import ParkingGarage, Floor, ParkingSpace, Wagen



class Garage_Gui:

    # init von Visual
    def __init__(self, root):
        
        self.root = root

        self.root.title("Die Garage")
        self.root.geometry("600x620") # Fenstergröße


        #PARKHAUS DATEN

        # Grid-Spalte dehnbar machen
        for i in range(4):
            self.root.columnconfigure(i, weight=1)

        tk.Label(self.root, text="Parkhaus Daten",font=("Arial",12,"bold")).grid(row=0, column=0, columnspan=4, sticky="w", pady=10)

        self.sep = ttk.Separator(self.root, orient="horizontal").grid(row=1,column=0,columnspan=5,sticky="ew", pady=10)

        self.floors = tk.Entry(self.root, width=7, font=("Arial",14,"bold"))
        self.floors.grid(row=2, column=0, sticky="",pady=5)
        self.cars_per_floor = tk.Entry(self.root, width=7, font=("Arial",14,"bold"))
        self.cars_per_floor.grid(row=2, column=1, sticky="",pady=5)

        tk.Label(self.root, text="Etagen Anzahl",font=("Arial",9,"bold")).grid(row=3, column=0, sticky="")
        tk.Label(self.root, text="Parkplatz pro etage",font=("Arial",9,"bold")).grid(row=3, column=1, sticky="")

        self.create_ph = tk.Button(self.root, text="Einlegen",font=("Arial",10,"bold"), bg="lightblue", command=self.btn_create_ph)
        self.create_ph.grid(row=2, column=3, sticky="")

        self.sep2 = ttk.Separator(self.root, orient="horizontal").grid(row=4,column=0,columnspan=5,sticky="ew", pady=10)



        #FAHRZEUGE DATEN
        tk.Label(self.root, text="Fahrzeuge Daten",font=("Arial",12,"bold")).grid(row=5, column=0, columnspan=4, sticky="w", pady=10)

        self.sep3 = ttk.Separator(self.root, orient="horizontal").grid(row=6,column=0,columnspan=5,sticky="ew", pady=10)
        
        self.car_licence_plate = tk.Entry(self.root, width=7, font=("Arial",14,"bold"))
        self.car_licence_plate.grid(row=7, column=0, sticky="",pady=5)
        self.moto_licence_plate = tk.Entry(self.root, width=7, font=("Arial",14,"bold"))
        self.moto_licence_plate.grid(row=7, column=3, sticky="",pady=5)

        tk.Label(self.root, text="Auto Kennzeichen",font=("Arial",9,"bold")).grid(row=8, column=0, sticky="")
        tk.Label(self.root, text="Moto Kennzeichen",font=("Arial",9,"bold")).grid(row=8, column=3, sticky="")

        self.create_car = tk.Button(self.root, text="Auto Einlegen",font=("Arial",10,"bold"), bg="lightblue", command=self.btn_create_car)
        self.create_car.grid(row=7, column=1, sticky="")
        self.create_moto = tk.Button(self.root, text="Moto Einlegen",font=("Arial",10,"bold"), bg="lightblue", command=self.btn_create_moto)
        self.create_moto.grid(row=7, column=4, sticky="")

        self.sep4 = ttk.Separator(self.root, orient="horizontal").grid(row=9,column=0,columnspan=5,sticky="ew", pady=10)


        #OPERATIONNEN
        tk.Label(self.root, text="Operationnen",font=("Arial",12,"bold")).grid(row=10, column=0, sticky="", pady=10)

        self.ph_status = tk.Button(self.root, text="PH Status",font=("Arial",10,"bold"), bg="lightblue", command=self.btn_parking_status)
        self.ph_status.grid(row=10, column=3, columnspan=2, sticky="", pady=10)

        self.status_field = tk.Frame(self.root, height=200, bg="white")
        self.status_field.grid(row=11, column=3, sticky="nsew", columnspan=2,rowspan=7, padx=10, pady=10)
        self.status_text = tk.Text(self.status_field, height=15, width=30, bg="white")
        self.status_text.pack(fill="both", expand=True)

        self.licence_plate_to_park = tk.Entry(self.root, width=7, font=("Arial",14,"bold"))
        self.licence_plate_to_park.grid(row=11, column=0, sticky="",pady=5)
        self.licence_plate_to_leave = tk.Entry(self.root, width=7, font=("Arial",14,"bold"))
        self.licence_plate_to_leave.grid(row=13, column=0, sticky="",pady=5)
        self.licence_plate_to_search = tk.Entry(self.root, width=7, font=("Arial",14,"bold"))
        self.licence_plate_to_search.grid(row=15, column=0, sticky="",pady=5)

        tk.Label(self.root, text="Kennzeichen",font=("Arial",9,"bold")).grid(row=12, column=0, sticky="")
        tk.Label(self.root, text="Kennzeichen",font=("Arial",9,"bold")).grid(row=14, column=0, sticky="")
        self.search_label = tk.Label(self.root, text="Kennzeichen",font=("Arial",9,"bold"))
        self.search_label.grid(row=16, column=0, sticky="")

        self.park = tk.Button(self.root, text="Parken",font=("Arial",10,"bold"), bg="lightblue", command=self.btn_park)
        self.park.grid(row=11, column=1, sticky="w")
        self.leave = tk.Button(self.root, text="Rausfahren",font=("Arial",10,"bold"), bg="lightblue",command=self.btn_leave)
        self.leave.grid(row=13, column=1, sticky="w")
        self.search = tk.Button(self.root, text="Suchen",font=("Arial",10,"bold"), bg="lightblue",command=self.btn_search)
        self.search.grid(row=15, column=1, sticky="w")


        #STATUS LABELS

        # for key, value in {"create_ph_status":2, "create_car_status":7,"create_moto_status":7,"park_status":11,"leave_status":12,"search_status":13}.items():
        #     self.key = tk.Label(self.root, text="",font=("Segoe UI Emoji", 14))
        #     if key=="create_moto_status":
        #         self.key.grid(row=value, column=6, sticky="")
        #     else:
        #         self.key.grid(row=value, column=2, sticky="")

        self.create_ph_status = tk.Label(self.root, text="",font=("Segoe UI Emoji", 14))
        self.create_ph_status.grid(row=2, column=2, sticky="")

        self.create_car_status = tk.Label(self.root, text="",font=("Segoe UI Emoji", 14))
        self.create_car_status.grid(row=7, column=2, sticky="")

        self.create_moto_status = tk.Label(self.root, text="",font=("Segoe UI Emoji", 14))
        self.create_moto_status.grid(row=7, column=6, sticky="")


        self.park_status = tk.Label(self.root, text="",font=("Segoe UI Emoji", 14))
        self.park_status.grid(row=11, column=2, sticky="")

        self.leave_status = tk.Label(self.root, text="",font=("Segoe UI Emoji", 14))
        self.leave_status.grid(row=13, column=2, sticky="")

        self.search_status = tk.Label(self.root, text="",font=("Segoe UI Emoji", 14))
        self.search_status.grid(row=15, column=2, sticky="") 


        #cars and autos list
        self.vehicles = {}
        

    # Functional
    
    #Create a parking
    def btn_create_ph(self):
        self.ph = ParkingGarage(int(self.floors.get()), int(self.cars_per_floor.get()))
        self.create_ph_status["text"] = "✔️"

    # parking status
    def btn_parking_status(self):
        self.status_text.delete("1.0", "end")
        self.status_text.insert("end", self.ph.getStatus())

    #Create a car 
    def btn_create_car(self):
        self.car=Wagen(self.car_licence_plate.get(), "Auto")
        self.vehicles[self.car_licence_plate.get()] = self.car
        self.create_car_status["text"] = "✔️"

    #Create a motorcycle
    def btn_create_moto(self):
        self.moto=Wagen(self.moto_licence_plate.get(), "Moto")
        self.vehicles[self.moto_licence_plate.get()] = self.moto
        self.create_moto_status["text"] = "✔️"

    def btn_park(self):
        self.ph.parkWagen(self.vehicles[self.licence_plate_to_park.get()])
        self.park_status["text"] = "✔️"

    def btn_leave(self):
        self.ph.removeWagen(self.licence_plate_to_leave.get())
        self.leave_status["text"] = "✔️"

    def btn_search(self):
        # self.ph.findWagenById(self.licence_plate_to_search.get())
        self.search_status["text"] = "✔️"
        self.search_label["text"] = self.ph.findWagenById(self.licence_plate_to_search.get())

        

    





# root.mainloop()
  
