import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

#XOR-Logik
#Eingaben: [0,0], [0,1], [1,0], [1,1]

X = np.array([[0,0], [0,1], [1,0], [1,1]])

#Ergebnis XOR: 0,1,1,0
y = np.array([0,1,1,0]) 

model = models.Sequential([
    layers.Dense(8, activation="relu", input_shape=(2,)),
    layers.Dense(4, activation="relu"),
    layers.Dense(1, activation="sigmoid", )    
    ])

model.compile(optimizer = 'adam',
              loss = "binary_crossentropy",
              metrics = ["accuracy"]
              )

model.fit(X,y, epochs=500, verbose=0)

prediction = model.predict(X)

for i, pred in enumerate(prediction):
    print(f"Input: {X[i]} -> Wahrscheinlichkeit: {pred[0]}")


#Ergebnisse
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 76ms/step
# Input: [0 0] -> Wahrscheinlichkeit: 0.32867637276649475
# Input: [0 1] -> Wahrscheinlichkeit: 0.8684011697769165
# Input: [1 0] -> Wahrscheinlichkeit: 0.7370729446411133
# Input: [1 1] -> Wahrscheinlichkeit: 0.3286946415901184