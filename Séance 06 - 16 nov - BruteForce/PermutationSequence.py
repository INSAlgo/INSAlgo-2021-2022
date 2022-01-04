from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        S=""
        for i in range(1,n+1):
            S+=str(i)
        V=permutations(S,n)
        i=0
        for v in V:
            if i==k-1:
                return ''.join(v)
            i+=1
