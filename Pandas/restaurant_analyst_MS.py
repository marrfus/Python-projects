import pandas as pd
import seaborn as sns 


df = sns.load_dataset('tips')

print(df.head())
print("-"*30+"\n ### Aufgabe 1 ###")

# Aufgabe 1: Überblick verschaffen 
print(df['day'].unique())
print(df['day'].value_counts())

print("-"*30+"\n ### Aufgabe 2 ###")

#Aufgabe 2: Neue Metrik einfügen
df.insert(2, 'tip_pct', (df['tip']/df['total_bill']))
print(df.head())

print("-"*30+"\n ### Aufgabe 3 ###")

#Aufgabe 3: Kategorien bilden
cats = ['Günstig', 'Normal', 'Teuer']
bns = [0,15,25,100]

df['bill_class'] = pd.cut(df['total_bill'], bins=bns, labels=cats)
print(df.head())

print("-"*30+"\n ### Aufgabe 4 ###")

#Aufgabe 4: Gruppen-Analyse
df_gr = df.groupby('bill_class', as_index=False, observed=False).agg({
                                                                            'tip':'mean',
                                                                            'size':'max',
                                                                            'day':'count'
                                                                        })
print(df_gr)

print("-"*30+"\n ### Aufgabe 5 ###")

# Aufgabe 5: Die Übersichtstabelle
df_pivot = df.pivot_table(
    values='tip_pct', 
    index='day', 
    columns='time', 
    aggfunc='mean')

print(df_pivot.reset_index())
print(df.isna().any())

