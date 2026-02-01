import numpy as np

x = np.array ([1,2,3,4], dtype=float)
x_new = np.array ([5,6,7], dtype=float)  #für neue Vorhersagen
# y = np.array ([2,4,6,8], dtype=float)  #y=2x
y = np.array ([5,7,9,11], dtype=float)  #y=2x + 3

import tensorflow as tf
import keras

model = keras.Sequential([keras.layers.Dense(1, input_shape=[1])])
    
model.compile(
    optimizer="sgd",
    loss="mean_squared_error"
)
 
model.fit(x,y, epochs=1000, verbose=0) #epochs = steps
 
# prediction = model.predict(np.array([5]))
# print(prediction)  

y_new_pred = model.predict(x_new)
print("Neue Vorhersagen", y_new_pred.flatten())

#y = w.x +b   w=gewicht(Steigung), b - Verschiebung

w,b = model.layers[0].get_weights()
print(f"Gewicht w: {w}")   
print(f"Bias b: {b}")   


# #Visualisierung
# import matplotlib.pyplot as plt

# y_pre = model.predict(x)

# plt.scatter(x,y, color='blue', label='Originale Daten')#Originalpunkte
# plt.plot(x,y_pre, color='red', label = 'Vorghersage')#Gelernte Gerade

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('ML-Modell: Gerade lernen')
# plt.legend()
# plt.show()