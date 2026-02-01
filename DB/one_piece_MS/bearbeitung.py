import sqlite3
from sys import exit
import pandas as pd
import matplotlib.pyplot as plt
from os import path

#Pfade Einrichtung
current_dir = path.dirname(path.abspath(__file__))
# db = sqlite3.connect(r"C:\Users\MariaSizintseva\Desktop\MariaDocs\marrfusProgBackup\python\DB\one_piece_MS\one_piece.db")
db = sqlite3.connect(path.join(current_dir,"one_piece.db"))

# Tabelle in DataFrame laden
df = pd.read_sql_query("SELECT * FROM one_piece_data", db)

# #oder
# result = db.execute("""SELECT * FROM one_piece_data """)
# op_list = result.fetchall()
# print(op_list[0])
# print("-"*30)

db.close()
print("\nHead")
print (df.head())
# print("-"*30)

print("\nInfo")
print(df.info())

print("\nDescribe")
print(df.describe())

df = df.drop(columns=["rank","season"])
# df.drop(columns=["rank","season"], inplace=True)
print("\nRank and season are deleted")
print (df.columns)

df_gr = df.groupby('start', as_index=False, observed=False).agg({'average_rating':'mean'})
print("\nGroupby")
print(df_gr)

try:
    #in neuen DB speichern
    db_new = sqlite3.connect(path.join(current_dir,"one_piece_new.db"))
    # db_new.execute("""
    # CREATE TABLE IF NOT EXISTS one_piece_data (
    #         "Unnamed: 0" INTEGER,
    #         trend TEXT,
    #         episode INTEGER,
    #         name TEXT,
    #         "start" INTEGER,
    #         total_votes TEXT,
    #         average_rating REAL
    #         )
    # """)
    df.to_sql(
        "one_piece_data",
        db_new,
        if_exists="append",
        index=False
    )
    db_new.close()
except sqlite3.Error as e:
    print(f"Datenbankfehler: {e}")
    exit()


#plot
X = df_gr.start
Y = df_gr.average_rating

plt.plot(X,Y, c="red")
plt.title(f"Average rating pro year")
plt.xlabel("year")
plt.ylabel("avg_rating")
plt.show()