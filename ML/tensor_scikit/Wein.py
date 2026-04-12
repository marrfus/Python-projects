import xgboost as xgb 
from sklearn.datasets import load_wine 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, classification_report

# 1. Daten laden 
print("Lade Wein-Daten...") 
wine = load_wine() 
X = wine.data       # Die 13 chemischen Merkmale 
y = wine.target     # Die Zielvariable: Weinsorte (0, 1 oder 2) 
 
print(f"Anzahl der Weine im Datensatz: {len(X)}") 
 
# 2. Daten aufteilen 
# Teile die Daten in Trainings- und Testdaten auf (z. B. 80% Training, 20% Test). 

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
 
# 3. Das XGBoost-Modell erstellen 
# Wichtig: Da wir Kategorien (Weinsorten) vorhersagen, nutze wieder den Classifier. 
model = xgb.XGBClassifier(
    n_estimators = 50,  #50 Bäume
    learning_rate = 0.1, #Schrittgröße beim Lernen
    max_depth = 3,  #Maximale Tiefe jedes Baums
    use_label_encoder = False,
    eval_metric = 'mlogloss'
)
 
# 4. Das Modell trainieren 
# Trainiere das Modell mit den Trainingsdaten.
model.fit(X_train,y_train)

# 5. Vorhersagen treffen 
# Nutze das trainierte Modell für die Testdaten. 
predictions = model.predict(X_test)   #y_pred

# 6. Auswertung 
# Berechne die Genauigkeit (Accuracy) und drucke sie aus. 
accuracy = accuracy_score(y_test,predictions)
print(f"Genauigkeit: {accuracy * 100:.2f}%") 

# Optional: Lass dir den detaillierten Bericht ausgeben 
print(classification_report(y_test, predictions, target_names=wine.target_names)) 