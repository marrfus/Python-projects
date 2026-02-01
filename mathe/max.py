
bargeld_initial=100
bargeld = 100
kreditkartenlimit=50
kontostand = 200
 
einkauf = 3*15.5+4.25+30
bargeld-=einkauf
bargeld+=5.5
 
if bargeld >= kreditkartenlimit:
    vergleich1=True
else:
    vergleich1=False
 
if kontostand!=200:
    vergleich2 = True
else:
    vergleich2=False
 
if (bargeld>100)or((kontostand>200)and(bargeld>10)):
    print("Max ist reich")
else:
    print("Max ist nicht reich")
 
snacks=['Apfel', 'Riegel', 'Nüsse']
if('Riegel' in snacks):
    print("Riegel ist im Angebot")
else:
    print("Kein Riegel ist im Angebot")
 
bargeld_initial_backup = 100
print(f"Sind Bargeld before Änderung und Backup dieselbe? {bargeld_initial is bargeld_initial_backup}")
print(f"Sind Bargeld und Backup dieselbe? {bargeld is bargeld_initial_backup}")