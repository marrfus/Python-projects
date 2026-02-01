import seaborn as sns
import matplotlib.pyplot as plt

#Datensaz
df = sns.load_dataset('flights')
print(df.head())
print(f"\nFählende Werte prüfen:\n{df.isna().sum()}")


#Aufgabe 1: Der Scatterplot (Punktwolke)
#Anzahl der Passagiere (passengers) über die Jahre (year)
# Färbe die Punkte nach den Monaten (month) ein, um zu sehen,
# ob es saisonaleMuster gibt.

#plot matrix
fig, ax = plt.subplots(1, 3, figsize=(10, 6))

#Scatterplot
sns.scatterplot(
    x='year',
    y= 'passengers',
    data=df,
    hue='month',          #Farbe nach Monat    
    ax=ax[0]
)
ax[0].set_title('Passengers pro year')

#Aufgabe 2: Der Linechart (Liniendiagramm)
#generellen Trend über die Jahre
sns.lineplot( 
    x='year',
    y= 'passengers',
    data=df,
    ax=ax[1])
ax[1].grid(True)
ax[1].set_title('Trend through years')

#Aufgabe 3: Kombinierte Analyse (Mehrere Linien)
sns.lineplot( 
    x='year',
    y= 'passengers',
    data=df,
    hue='month',
    palette=['red','orange','yellow','green','lightblue', 'blue','violet', 'gray', 'beige', 'lightgreen','pink','purple'],
    ax=ax[2]
    )
ax[2].set_title('Kombinierte Analyse')

plt.show()

