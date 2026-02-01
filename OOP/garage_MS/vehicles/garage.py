
class Parkhaus:

    def __init__(self, etagen:int, plaetze_pro_etage:int):
        self.etagen = etagen
        self.pl_pro_et = plaetze_pro_etage
        self.besetzt = [""]*etagen*plaetze_pro_etage
        # self.besetzt = [[""]*plaetze_pro_etage for _ in range(etagen)]
    
    # Get-Methoden
    def getEtagen(self):
        return self.etagen
    
    def getPlaetzeProEtage(self):
        return self.pl_pro_et
    
    def getBesetzt(self):
        return self.besetzt
    
    def getKapazitaet(self):
        return self.etagen*self.pl_pro_et
    
    def getPosition(self, id:str):
        if id in self.besetzt:
            ind = self.besetzt.index(id)
            et = ind//self.pl_pro_et
            pl = ind - et*self.pl_pro_et +1  # Plätze fangen ab 1 an, Indexen - ab 0
            if et == 0: et = "E"
            return f"Position von {id}:  {et} Stock {pl} Platz."
    
    def getVisual(self):
        p = self.pl_pro_et
        i = (len(self.besetzt)-1)//p
        j = len(self.besetzt)-p        

        while i>=0:
            print(f"{i}: |{[self.besetzt[k] for k in range (j, j+p)]}|")
            i-=1
            j-=p


    
    #Set-Methoden
    def parkVehicle(self,id:str,type:str):     #TBD
        if "" in self.besetzt:
            if id not in self.besetzt:
                if type == "Auto" or type == "Motorrad":
                    self.besetzt[self.besetzt.index("")] = id
                    return f"Das Fahrzeug {id} ist erfolgreich geparkt"
                else:
                    return "Sorry, ich akzeptiere nur Autos oder Motorräde. Tchüss!"
            else:
                # raise Exception(f"Das Fahrzeug {id} is schon geparkt!")
                return f"Das Fahrzeug {id} is schon geparkt!"
        else:
            # raise Exception("Sorry, das Parkhaus ist voll. Dein Fahrzeug kann nicht geparkt werden")
            return "Sorry, das Parkhaus ist voll. Dein Fahrzeug kann nicht geparkt werden"
    
    def unparkVehicle(self, id:str):
        # if len(self.besetzt) != 0:
        if id in self.besetzt:
            self.besetzt[self.besetzt.index(id)] = ""
            return f"Das Fahrzeug {id} ist erfolgreich ausgeparkt."
        else:
            return f"Das Fahrzeug {id} ist nicht gefunden!"
        

                


    
    


    # def freiePlatz(self):


    # def parken(self,obj:object,):

    #     self.geparkt[obj.id] = (obj.etage, obj.platz)
    #     return Vehicle.geparkt
    
    # def ausparken(self, id:str):
    #     del Vehicle.geparkt[id]
    #     return Vehicle.geparkt
