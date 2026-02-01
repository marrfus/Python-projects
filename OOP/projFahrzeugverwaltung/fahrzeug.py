class Fahrzeug:

    def __init__(self, marke:str, model:str, baujahr:int, farbe:str):
        self.marke = marke
        self.model = model
        self.baujahr = baujahr
        self.farbe = farbe
        self.motorGestartet = False

    #Get-Methoden
    def getMarke(self):
        return self.marke
    
    def getModel(self):
        return self.model
    
    def getBaujahr(self):
        return self.baujahr
    
    def getFarbe(self):
        return self.farbe
    
    def getMotorGestartet(self):
        return self.motorGestartet
    

    # Setter (Set-Methoden)
    def setFarbe(self, new_color):
        if type(new_color) != str:
            raise ValueError("Farbe muss ein String sein")
        self.farbe = new_color

    def setBaujahr(self, jahr):
        if type(jahr) != int:
            raise ValueError("Baujahr muss ein Int sein")
        self.baujahr = jahr

    #Methoden
    def starten(self):
        self.motorGestartet = True
        print(f"Der Motor des {self.marke} {self.model} wurde gestartet.")
    
    def ausschalten(self):
        self.motorGestartet = False
        print(f"Der Motor des {self.marke} {self.model} wurde ausgeschaltet.")

    def informationenAusgeben(self):
        print(f"Marke: {self.marke}\nModel: {self.model}\nBaujahr: {self.baujahr}\nFarbe: {self.farbe}\nmotorGestartet: {self.motorGestartet}")

    def fahren(self):
        if self.motorGestartet:
            print(f"{self.marke} {self.model} fährt.")
        else:
            print(f"Bitte zuerst den Motor starten um zu fahren!")