import matplotlib.pyplot as plt

lable = ["A", "B", "C"]
size = [20,50,30]

plt.pie(size,labels=lable)
plt.title("Pie Chart")
plt.show()