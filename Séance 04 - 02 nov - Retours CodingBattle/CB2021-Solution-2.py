import sys
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
times = list(map(int, lines[0].split()))
dico = {"F": 0,"P": 1,"A": 2}
n = int(lines[1])
# On soustrait le temps de chaque livre au temps du jury de sa catégorie
for i in range(n):
            a = lines[2+i].split()
            times[dico[a[0]]] -= int(a[1])
# si l'un des temps restant d'un juré est négatif, on affiche non
res = 1
for i in range(len(times)):
            res = res and times[i]>=0
print("oui" if res else "non")
