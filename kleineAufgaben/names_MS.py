from random import shuffle

def get_names(*names):
    print(f"Von allen Würdigen: \n")
    for name in names:
        print(f"{name}")
    print("\nWählen wir die Würdigsten aus. So...")
    list_n = list(names)
    shuffle(list_n)
    return list_n[0]
    

n=get_names("Abdullah","Alena","Maria","Daria","Ali","Rayen")
print(f"\n {n} is on duty today und macht Frühstück für alle")