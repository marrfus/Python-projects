import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

#Trainingsdaten

X_train = np.array([
    [1,2],
    [2,3],
    [3,3],
    [6,5],
    [7,7]    
])

#Klassenlabels
y_train = np.array(["Rot","Rot","Blau","Blau","Rot"])

#Modell
knn = KNeighborsClassifier(n_neighbors=3)   #k=3

#Modell trainiren
knn.fit(X_train,y_train)

#Neuer Punkt
X_new = np.array([[3,2]])

#Vorhersage
prediction = knn.predict(X_new)

print("Klassifikation:", prediction[0])

distances, indices = knn.kneighbors(X_new)
print("Distanzen:", distances)
print("Indizes der Nachbarn :" ,indices)

for i  in range(len(X_train)):
    if y_train[i] == "Rot":
        plt.scatter(X_train[i,0],X_train[i,1], marker="o", color="red")
    else:
        plt.scatter(X_train[i,0],X_train[i,1], marker="s", color="blue")

#Neuer Punkt
plt.scatter(3,2, marker="x", s = 200)
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()