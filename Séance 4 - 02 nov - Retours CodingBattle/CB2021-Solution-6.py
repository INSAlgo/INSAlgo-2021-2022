from math import gcd
from random import randint
import collections,sys
# factorisation par l'algorithme de brent des grands nombres
def brent(N):
   if N%2==0: return 2
   y,c,m = randint(1, N-1),randint(1, N-1),randint(1, N-1)
   g,r,q = 1,1,1
   while g==1:             
       x = y
       for i in range(r):
          y = ((y*y)%N+c)%N
       k = 0
       while (k<r and g==1):
          ys = y
          for i in range(min(m,r-k)):
             y = ((y*y)%N+c)%N
             q = q*(abs(x-y))%N
          g = gcd(q,N)
          k = k + m
       r = r*2
   if g==N:
       while True:
          ys = ((ys*ys)%N+c)%N
          g = gcd(abs(x-ys),N)
          if g>1:  break
   return g
def factorize(n1):
    if n1==0: return []
    if n1==1: return [1]
    n=n1
    b=[]
    p=0
    mx=1000000
    while n % 2 ==0 : b.append(2);n//=2
    while n % 3 ==0 : b.append(3);n//=3
    i=5
    inc=2
    while i <=mx:
       while n % i ==0 : b.append(i); n//=i
       i+=inc
       inc=6-inc
    while n>mx:
      p1=n
      while p1!=p:
          p=p1
          p1=brent(p)
      b.append(p1);n//=p1 
    if n!=1:b.append(n)   
    return sorted(b)
	
	
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
n=int(lines[0])
if n <= 4:
    print(0)
    sys.exit(0)
# Compter le nombre de facteurs de n+4, mais certains facteurs sont invalides
li=factorize(n+4)
nfac = 1
ctr = collections.Counter(li).values()
for fc in ctr:
    nfac *= (fc+1)
# On enlève la moitié des facteurs pour pas garder les doublons
nfac //= 2
# On enlève le facteur 1 parce qu'il donnerait x = -1
nfac -= 1
# On enlève le facteur 2 s'il existe parce qu'il donnerait x = 0
if li[0] == 2:
    nfac -= 1
# On rajoute le facteur sqrt(n) si n+4 est un carré parfait (parce que le nfac//=2 le tue avec l'arrondi)
if sum(v%2 for v in collections.Counter(li).values()) == 0:
    nfac += 1
print(nfac)
