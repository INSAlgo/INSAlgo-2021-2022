import sys
from collections import deque 
adjacencylist={}
n=int(input())
for i in range(n):
    adjacencylist[i]=[]

for i in range(n-1):
    s=input().split()
    adjacencylist[int(s[1])]+=[int(s[0])]

queue=deque()
rangs=[-1 for i in range(n)]
rangs[0]=0
nbrangs=[ 0 for i in range(10)]
nbrangs[0]=1
queue.append(0)

while len(queue)>0:
    current=queue.popleft()
    childs=adjacencylist[current]
    for child in childs :
        queue.append(child)
        rangs[child]=rangs[current]+1
        nbrangs[rangs[current]+1]+=1
print(*nbrangs)
