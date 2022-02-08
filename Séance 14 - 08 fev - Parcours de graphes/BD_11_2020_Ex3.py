from collections import deque

N=int(input())

adj = [[]for _ in range(N)]
number = [0 for _ in range(10)]

for _ in range(N-1):
    A,B=map(int,input().split())
    adj[B].append(A)

q = deque()
q.append((0,0))

while q:
    current,lvl = q.popleft()
    number[lvl]+=1
    
    for nei in adj[current]:
        q.append((nei,lvl+1))

print(*number)
