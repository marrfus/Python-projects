
def zaehle_woerter(text):
    if type(text)!= str:
        text=input("Schreiben mir bitte etwas und ich zähle alle Wörter drin.  ")
    
    #Leerzeichen von Amfang und am Ende entfernen!!!
    text = text.strip()
    print(text)  
    woerter=1
    if text=="": #or set(text)=={" "}:
        woerter = 0
    else:
        for i in range (len(text)): 
            if text[i]==" " and text[i+1]!=" ":
                woerter += 1
    return woerter




