
from random import shuffle, randint



def team_vorbereiten(team_liste, aufgaben_liste):
    shuffle(team_liste)
    shuffle(aufgaben_liste)
    return team_liste, aufgaben_liste

def verteile_aufgaben(team_liste, gemischte_aufgaben):
    # for index, name in enumerate(team_liste):
    #     print(f"{name} ist zuständig für: {gemischte_aufgaben[index]}")
    print("."*50)
    #wer ist die kleinste: Aufgaben oder Teilnehmer liste?
    anzahl_zuordnungen = min(len(team_liste),len(gemischte_aufgaben))
    # for name in team_liste:
    for i in range (anzahl_zuordnungen):
        protokoll_liste.append((team_liste[i], gemischte_aufgaben[i]))
        print(f"{team_liste[i]} ist zuständig für: {gemischte_aufgaben[i]}")       
        i+=1
    print("."*50)
    
def check_durchfuerung(protokoll):
    i = 0
    while i<len(protokoll):
        t = randint(1,10)
        if t>=8:
            print(f'ACHTUNG! "{protokoll[i-1][1]}" benötigt eine längere Nachbereitung!')
        i+=1
    print("/////// Durchführung completed ///////")






#Hauptprogram
if __name__=="__main__":

    #Alles definieren
    protokoll_liste = []
    teammitglieder = ["Alice", "Bob", "Charlie", "David", "Eve"]
    aufgaben = ["Protokol führen", "Zeitnehmer sein", "Themen zusammenfassen", "Nächste Schritte planen", "Präsentation halten"]

    #Aufgabenverteilung
    mix_liste, mix_aufgaben = team_vorbereiten(teammitglieder, aufgaben)
    verteile_aufgaben(mix_liste,mix_aufgaben)
    check_durchfuerung(protokoll_liste)
