import pandas as pd
import csv
from os import path

#Pfade Einrichtung
current_dir = path.dirname(path.abspath(__file__))

filename = path.join(current_dir,"taxis.csv")

columns = ['pickup_zone', 'passengers']

dtype_dict = {'pickup_zone':'category', 'passengers':'int8'}



df = pd.read_csv(
    filename, 
    nrows=100,
    usecols=columns,
    dtype=dtype_dict
    )
print(f"Erste 100 Zeilen nur 2 Spalten mit optimierte Dtype:\n{df}")

total_fare = 0
for chunk in pd.read_csv(filename, usecols=['fare'], dtype={'fare':'float32'}, chunksize=1000):
    total_fare += chunk['fare'].sum()

print(f"Total fare = {total_fare}")