import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2*np.pi, 500)
Ya = np.sin(X)
Yb = 0.5*np.sin(5*X)
Ysum = Ya +Yb

A = plt.plot(X,Ya,label="Welle A", c="red",linestyle="dashed")
B = plt.plot(X,Yb, label="Welle B", c="green")
SUM = plt.plot(X,Ysum, label="Welle A+B", c="brown",linestyle="dotted")
plt.title("Sinus Wellen")
plt.xlabel("X")
plt.ylabel("Y",rotation=0)
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)

plt.legend()
plt.show()
