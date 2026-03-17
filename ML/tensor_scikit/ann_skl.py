from sklearn.neural_network import MLPClassifier
import numpy as np


#XOR-Logik
#Eingaben: [0,0], [0,1], [1,0], [1,1]

X = np.array([[0,0], [0,1], [1,0], [1,1]])

#Ergebnis XOR: 0,1,1,0
y = np.array([0,1,1,0]) 

#Netzwerk erstellen
mlp = MLPClassifier(hidden_layer_sizes=(4,),
                    activation="relu", 
                    solver="adam",
                    max_iter=2000, 
                    random_state=1)
#Training
mlp.fit(X,y)

#Vorhersage treffen
print("Vorhersage für XOR:")
for i in range(len(X)):
    pred = mlp.predict([X[i]])
    print(f"Input: {X[i]} -> Vorhersage: {pred[0]}")


#Ergebnisse:
# Vorhersage für XOR:
# Input: [0 0] -> Vorhersage: 0
# Input: [0 1] -> Vorhersage: 1
# Input: [1 0] -> Vorhersage: 1
# Input: [1 1] -> Vorhersage: 0

