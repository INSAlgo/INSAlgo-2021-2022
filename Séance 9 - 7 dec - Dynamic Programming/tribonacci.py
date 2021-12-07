class Solution:
    def tribonacci(self, n: int) -> int:
        
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 1
        
        
        tab=[0 for i in range(n+1)]
        tab[0]=0
        tab[1]=1
        tab[2]=1
        
        for i in range(3,n+1):
            tab[i]=tab[i-1]+tab[i-2]+tab[i-3]
        
        return tab[n]
