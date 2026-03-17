import tensorflow as tf
from tensorflow import keras

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Datensatz laden
iris = load_iris()

X= iris.data
y= iris.target

# Daten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Daten normalisieren
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Modell erstellen
# 4 Eingabe -> 10 Neuronen -> 8 Neuronen -> 3 Ausgaben
# 4 Eingaben = Iris-Merkmale
# 3 Ausgaben = 3 Blumenarten

model = keras.Sequential([
    keras.layers.Dense(10, activation="relu", input_shape=(4,)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(3, activation="softmax")
])

# Modell kompilieren
model.compile(
    optimizer = "adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Training
model.fit(X_train, y_train, epochs = 50)

# Model testen
loss, accuracy = model.evaluate(X_test,y_test)

print("Genauigkeit:", accuracy)

prediction = model.predict(X_test[:1])
# print(X_test)
print(prediction)
