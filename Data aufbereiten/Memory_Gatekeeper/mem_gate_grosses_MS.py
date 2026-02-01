import pandas as pd
from os import path

#Pfade Einrichtung
current_dir = path.dirname(path.abspath(__file__))

filename = path.join(current_dir,"grosses_dataset.csv")


# columns = ['pickup_zone', 'passengers']

# dtype_dict = {'pickup_zone':'category', 'passengers':'int8'}



df = pd.read_csv(
    filename, 
    nrows=100
    )
print(f"Erste 100 Zeilen um Dataset kennenzulernen:\n{df}")
print(f"\nData types:\n{df.dtypes}")

df_menge = pd.read_csv(
    filename,usecols=['menge']
)
print(f"\nMax menge = {df_menge['menge'].max()}\n")

dtype_dict = {
    'kategorie':'category',
    # 'filiale':'category',
    'menge':'int8',
    # 'preis':'float32',
    'kunden_bewertung':'int8'
}

df_curtain_colmns = pd.read_csv(
                                filename,
                                usecols=dtype_dict.keys(),
                                dtype=dtype_dict,
                                nrows=100)

print(f"Erste 100 Zeilen nur 3 Spalten mit optimierte Dtype:\n{df_curtain_colmns}")
print(f"\nData types:\n{df_curtain_colmns.dtypes}")

avg_bewertung = 0
n=0
for chunk in pd.read_csv(filename, usecols=['kunden_bewertung'],
                         dtype={'kunden_bewertung':'int8'}, chunksize=1000):
    avg_bewertung += chunk['kunden_bewertung'].mean()
    n+=1
print(f"Durschnittliche Bewertung = {(avg_bewertung/n):.2f}")