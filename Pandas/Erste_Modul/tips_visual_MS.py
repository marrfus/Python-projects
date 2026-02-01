import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")

# #A) Scatterplot
# plt.scatter(tips.total_bill, tips.tip, c="blue",edgecolors="blue", s=80, alpha=0.6)
# plt.title("Scatter: Rechnung-Trinkgeld")
# plt.xlabel("bill")
# plt.ylabel("tips")
# plt.show()

# #B) Histogramm
# plt.hist(tips.total_bill, bins=30, color="orange",edgecolor="black")
# plt.title("Histogramm: Rechnung")
# plt.xlabel("bill")
# plt.ylabel("frequency")
# plt.show()

# #C) Boxplot

# # tips nach Kategorien gruppieren
# gr_tips = tips.groupby("sex")["tip"]
# # listen für boxplot
# data = [group for name, group in gr_tips]
# labels = [name for name in gr_tips.groups.keys()]

# # zeichnen
# plt.boxplot(x=data, labels=labels, patch_artist=True)

# # tips.boxplot(column="tip",by="sex")

# plt.title("Boxplot: Trinkgeld pro Geschlecht")
# plt.xlabel("Geschlecht")
# plt.ylabel("Trinkgeld")
# plt.show()

# #D) Barplot
# plt.bar(tips.tip,tips.day, color="purple",edgecolor = "black")
# plt.title("Barplot: Trinkgeld pro Wochentag")
# plt.xlabel("Trinkgeld")
# plt.ylabel("Wochentag")
# plt.show()

#E) Subplots
# print(len(tips["size"]))
# print(len(tips["tip"]))

fig, axs =plt.subplots(1,2)

axs[0].hist(tips["tip"],color="red")
axs[0].set_title("Histogramm tips")


axs[1].scatter(tips["size"],tips["tip"], color="darkgreen")
axs[1].set_title("Scatter size vs tips")

plt.show()


