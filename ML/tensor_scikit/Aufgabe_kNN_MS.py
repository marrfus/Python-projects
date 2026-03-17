import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import math


#Trainingsdaten

X_train = np.array([
    [1,2],
    [2,3],
    [3,4],
    [6,7],
    [7,9]
])

# #Klassenlabels
y_train = np.array(["Rot","Rot","Blau","Blau","Blau"])

#Modell
knn = KNeighborsClassifier(n_neighbors=4,weights="distance")   #k=3. Wenn k=4 -> andere Klasse

#Modell trainieren
knn.fit(X_train,y_train)

#Neuer Punkt
X_new = np.array([[5,2]])

#Vorhersage
prediction = knn.predict(X_new)

print("Klassifikation: ",prediction[0])

dists, indxs = knn.kneighbors(X_new)
print("Distanzen:", dists)
print("Indizes der Nachbarn :" ,indxs)

for i  in range(len(X_train)):
    if y_train[i] == "Rot":
        plt.scatter(X_train[i,0],X_train[i,1], marker="o", color="red")
    else:
        plt.scatter(X_train[i,0],X_train[i,1], marker="s", color="blue")
        
#Neuer Punkt
if prediction[0]=="Rot":
    clr="red"
else: clr="blue"
plt.scatter(5,2, marker="x", s = 100, color=clr)

plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

#######   Manuelle Variante mit Distanz Wählen  ##########
#Distanz Tabelle erstellen
distances = []

for i in range(len(X_train)):
    distances.append([math.sqrt((X_train[i][0]-X_new[0][0])**2+(X_train[i][1]-X_new[0][1])**2),y_train[i]])
distances.sort(key= lambda x: x[0])    
print(distances)

def euclidean_distance(p1,p2):
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i]) ** 2
    return math.sqrt(sum)


def get_neighbors(X_train, y_train, test_point, k):
    w = [] #distanzgewicht = 1/d

    for i in range(len(X_train)):
        gewicht = 1/euclidean_distance(test_point, X_train[i])
        w.append((gewicht,y_train[i]))

    w.sort(key= lambda x: x[0],reverse=True)

    neighbors = w[:k]
    return neighbors

def predict_classification(X_train, y_train, test_point , k):
    
    neighbors = get_neighbors(X_train, y_train, test_point, k)
    class_votes = {} # {"B":sum(1/dist), "R":sum(1/dist)}    

    for gewicht, label in neighbors:
        if label in class_votes:
            class_votes[label] +=gewicht
        else:
            class_votes[label] = gewicht

    print('#####   Voting nach Distanz   #####')    
    print('Voting: ',class_votes,'\n')
    predicted_class = max(class_votes, key = class_votes.get)
    return predicted_class
    

test_point = [5,2]
k = 3

result = predict_classification(X_train, y_train,test_point,k)
print("Neuer Punkt:", test_point)
print("Vorhersage Klasse:", result)
