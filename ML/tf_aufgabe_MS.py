# Mit nicht perfikten Daten.

import numpy as np

# Original Gerade: 
x = np.array([1,2,3,4], dtype=float)
y = np.array([3, 5, 7.1, 9], dtype=float) # kleine Abweichung

import tensorflow as tf
import keras

model = keras.Sequential([ keras.layers.Dense(1,input_shape=[1])])

model.compile(optimizer="sgd", loss="mean_squared_error")

history = model.fit(x,y, epochs=500, verbose=0)

w,b = model.layers[0].get_weights()
print(f"Gewicht w: {w}")   
print(f"Bias b: {b}")  

x_pred = np.array([5,6], dtype=float)
y_pred = model.predict(x_pred)

print("Neue Vorhersagen:", y_pred.flatten())


#Visualisierung
import matplotlib.pyplot as plt

plt.scatter(x,y, color='blue', label='Echte Traningsdaten')
plt.plot(x, model.predict(x), color='red', label='Gelernte Gerade')
plt.scatter(x_pred, y_pred, color='green', label='Vorhersage für neue x')

plt.xlabel('x')
plt.ylabel('y')
plt.title('ML-Modell: Vorhersage für neue Werte')
plt.legend()
plt.show()

plt.plot(history.history['loss'])
plt.xlabel('Epoche')
plt.ylabel('Loss (MSE)')
plt.title('Loss Kurve über die Epochen')
plt.show()