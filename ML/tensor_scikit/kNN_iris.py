from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import numpy as np

iris = load_iris()


X = iris.data # Merkmale
y = iris.target # Klassen

print("Feature-Namen", iris.feature_names)
print("Klassen:", iris.target_names)
print("Anzahl Daten:", len(X))

# Wir teilen die Daten 80% Training, 20% test
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

k = 5

knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

y_predict = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_predict)
print("Genauigkeit:",accuracy)

new_flower = np.array([[5.1,3.5,1.4,0.2]])

prediction = knn.predict(new_flower)

print("Vorhersagte Klasse:", iris.target_names[prediction][0])
