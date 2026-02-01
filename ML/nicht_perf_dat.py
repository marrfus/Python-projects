import numpy as np

x= np.array([1,2,3,4], dtype=float)
y= np.array([5, 7.2, 8.9, 11.1], dtype=float) #mit Abweichung

import tensorflow as tf
import keras
model = keras.Sequential([keras.layers.Dense(1, input_shape=[1])])
model.compile(optimizer='sgd', loss="mean_squared_error")
history = model.fit(x,y, epochs=500, verbose=0)

import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.xlabel('Epoche')
plt.ylabel('Loss (MSE)')
plt.title('Fehleremtwicklung beim Training')
plt.show()

y_pred = model.predict(x)

plt.scatter(x,y, color='blue', label='Daten mit Rauschen')
plt.plot(x,y_pred, color='red', label='Gelernte Gerade')
plt.xlabel('x')
plt.ylabel('y')
plt.title('ML-Model: Anpassung an verrauchte Daten')
plt.legend()
plt.show()