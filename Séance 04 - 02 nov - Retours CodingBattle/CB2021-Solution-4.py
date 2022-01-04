import sys
from math import sqrt,floor
#given the list of points already taken (HU) and the new point p, return True if the Hull turns right and False if it turns left
def turnRight(HU, p) -> bool:
    if len(HU) <= 1:
        return True
    cross_product = (HU[-1][0] - HU[-2][0]) * (p[1] - HU[-2][1]) - (HU[-1][1] - HU[-2][1]) * (p[0] - HU[-2][0])
    if cross_product <= 0:
        return True
    else:
        return False
H, L = map(int, input().split())
highest = [-1 for _ in range(L)]
for i in range(H):
    line = input()
    for j in range(L):
        #keep only the highest X for each position
        if line[j] == 'X' and highest[j] == -1:
            highest[j] = H - i - 1
#The upper convex hull must only make right hand turns
SupHull = []
for i in range(L):
    if highest[i] != -1:
        while not turnRight(SupHull, (i, highest[i])):
            SupHull.pop(-1)
        SupHull.append((i, highest[i]))
clothLen = 0
#Calculate the length of the cloth (length of the convex hull + height of right and left points of the hull) 
for i in range(len(SupHull) - 1):
    clothLen += sqrt((SupHull[i][0] - SupHull[i + 1][0]) ** 2 + (SupHull[i][1] - SupHull[i + 1][1]) ** 2)
clothLen += SupHull[0][1] + SupHull[-1][1]
print(floor(clothLen))
