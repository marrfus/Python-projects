import numpy as np
import matplotlib.pyplot as plt

X, Y = np.linspace(-10, 10, 201), np.zeros(201)
positionen=[]
for i in range(201):
    if -5<=X[i]<=5:
        positionen.append(i)
Y[positionen[0]:positionen[len(positionen)-1]]=1

plt.plot(X,Y)
plt.show()
