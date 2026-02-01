import sqlite3
import json
from sys import exit
from os import path


#Pfade Einrichtung
current_dir = path.dirname(path.abspath(__file__))
# db = sqlite3.connect(r"C:\Users\MariaSizintseva\Desktop\MariaDocs\marrfusProgBackup\python\DB\one_piece_MS\one_piece.db")
db = sqlite3.connect(path.join(current_dir,"one_piece.db"))

# db.execute("DROP TABLE one_piece_data")
db.execute("""
CREATE TABLE IF NOT EXISTS one_piece_data (
           "Unnamed: 0" INTEGER,
           rank TEXT,
           trend TEXT,
           season INTEGER,
           episode INTEGER,
           name TEXT,
           start INTEGER,
           total_votes TEXT,
           average_rating REAL
           )
""")


op_data = []
# Datei vorhanden?
try:
    json_file = open(path.join(current_dir,"one_piece.json"), "r")
except FileNotFoundError:
    print("Datei one_piece.json nicht gefunden.")
    exit()

# JSON auslesen und umwandeln
try:
    op_data = json.load(json_file, object_hook = lambda obj: list(obj.values()))
except json.JSONDecodeError as e:
    print(f"Fehler im JSON-Code: {e}")
    exit()
# print(op_data[0])
try:
    # db = sqlite3.connect(r"C:\Users\MariaSizintseva\Desktop\MariaDocs\marrfusProgBackup\python\DB\one_piece_MS\one_piece.db")
    # Daten einfügen
    nd = 0
    for arr in op_data:
        db.execute("""INSERT INTO one_piece_data
            ("Unnamed: 0", "rank", trend, season, episode, name, "start", total_votes, average_rating)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            [arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8]])
        nd += 1
    # Änderung permanent machen (Commit)
    db.commit()
    # Wie viele Datensätze gibt es und wie viele wurden eingefügt?
    result = db.execute("SELECT COUNT(*) FROM one_piece_data")
    number = result.fetchone()[0]
    print(f"{number} Datensätze insgesamt.")
    print(f"{nd} Datensätze eingefügt.")
except sqlite3.Error as e:
    print(f"Datenbankfehler: {e}")
    exit()
