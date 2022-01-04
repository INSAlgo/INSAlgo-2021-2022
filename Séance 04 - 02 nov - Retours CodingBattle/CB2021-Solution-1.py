import sys
from math import ceil
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
# Moyenne des deux couleurs arrondie à l'entier au dessus
moy = ceil((int(lines[0])+int(lines[1]))/2)
print(moy)
