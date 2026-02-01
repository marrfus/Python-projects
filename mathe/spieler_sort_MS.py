

def ScoreSorter(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            #  score j kleiner als score j+1  ODER  score gleich, aber Name j kommt alphabetisch nach Name j+1
            # if a[j][1] < a[j+1][1] or (a[j][1] == a[j+1][1] and a[j][0] > a[j+1][0]):
            if a[j][1] < a[j+1][1]:
                tausch(a,j)
            if (a[j][1] == a[j+1][1] and a[j][0] > a[j+1][0]):
                tausch(a,j)


def tausch(a,j):
    a[j],a[j+1] = a[j+1],a[j]


# (Spielername, Score)
spieler_scores = [
   ("Alice", 150),
   ("Bob", 80),
   ("Charlie", 150),
   ("David", 220),
   ("Eve", 80)
]

ScoreSorter(spieler_scores)
print(f"Ergebnis: {spieler_scores}")