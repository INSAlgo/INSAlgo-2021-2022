class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        entrant=[[] for _ in range(n+1)]
        sortant = [[] for _ in range(n+1)]
        
        for link in trust:
            sortant[link[0]].append(link[1])
            entrant[link[1]].append(link[0])
        
        for i in range(1,n+1):
            if len(sortant[i])==0 and len(entrant[i])==n-1:
                return i
        else:
            return -1
