import numpy as np
import matplotlib.pyplot as plt
def kreis(r):
    alfa = np.linspace(0, 2*np.pi, 500)
    X = r*np.cos(alfa)+r
    Y = r*np.sin(alfa)+r

    plt.plot(X,Y, c="red")
    plt.title(f"Kreis mit Radius {r}")
    plt.xlabel("X")
    plt.ylabel("Y",rotation=0)
    plt.gca().set_aspect('equal')
    plt.axhline(linewidth=1)
    plt.axvline(linewidth=1)
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.scatter(0,0)
    plt.annotate("0", (0.2,0.2))
    plt.show()

while True:
    r = input("Gib bitte Radius Wert. Soll kleine als 10 sein.")
    try:
        r = float(r)
        if 0<r<=10:
            kreis(r)
            break
        else:
            print("Nur ein Wert zwischen 0 und 10")
    except ValueError:
        print("Das soll ein Zahl sein!")


# kreis(1)