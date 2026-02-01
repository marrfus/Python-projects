import matplotlib.pyplot as plt

plt.title("Ein schöner Quadrat")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter([-2,-2,2,2],[-2,2,-2,2])
plt.annotate("A", (-2,-2))
plt.annotate("B", (-2,2))
plt.annotate("C", (2,2))
plt.annotate("D", (2,-2))

plt.plot([-2,-2],[-2,2])
plt.plot([-2,2],[2,2])
plt.plot([2,2],[2,-2])
plt.plot([-2,2],[-2,-2])

plt.text(-1.8,0, "A", color="blue", size=16)
plt.text(0,1.8, "B", color="#FFA500")
plt.text(1.7,0, "C", color="green", size=24)
plt.text(0,-1.8, "d", color="red", size=24)

plt.show()