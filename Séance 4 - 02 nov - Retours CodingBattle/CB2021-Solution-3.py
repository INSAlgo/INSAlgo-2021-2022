#parsing
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
l, L = map(int, lines[0].split())
grid = []
for i in range(l):
            grid.append(lines[i + 1])
sumkept = 0
coordskept = ""
#on parcourt tout le paysage
for i in range(l-2):
            for j in range(L-2):
                sum=0
		#on calcul le score pour chaque photo 3 par 3
                for a in range(3):
                    for b in range(3):
                        if grid[i+a][j+b]=="X":
                            sum+=1
		#si le score est maximal, on le garde en mémoire
                if sum >= sumkept:
                    sumkept = sum
                    coordskept = str(i + 1)+" "+ str(j + 1)
                
#On affiche les coordonnées pour lesquelles on avait le score maximal
print(coordskept)
