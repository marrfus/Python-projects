import random
from datetime import datetime, timedelta
import pandas as pd
from os import path

#Pfade Einrichtung
current_dir = path.dirname(path.abspath(__file__))

#resource
resource = ["User_A","User_B","System_Bot"]



Activities = [
    "Order Received",
    "Check Inventory",
    "Payment confirmed",
    "Pack Item",
    "Ship Order",
    "Deliver Order"
]

#EventLog:
data = []
for case_id in range(1, 6):
    start = datetime(2026, 1, 13+case_id, 8, 0, 0)
    current = start
    for activity in Activities:
        current += timedelta(minutes=random.randint(30, 120))
        data.append([case_id, activity, current,random.choice(resource),
                     round(random.uniform(2.0, 5.0), 2)])

print(data)

#in csv schreiben
df = pd.DataFrame(data, columns=["case_id", "activity", "timestamp", "resource", "cost"])

df.to_csv(path.join(current_dir,"event_log.csv"), index=False)
print("CSV-Datei ist erstellt")
