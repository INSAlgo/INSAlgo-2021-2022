class Solution:
    def climbStairs(self, n: int) -> int:
        
        stair=[0 for i in range(n+1)]
        stair[0] = 1
        
        for k in range(0,n+1):
            if(k>=1):
                stair[k] += stair[k-1]
            if(k>=2):
                stair[k] += stair[k-2]
        
        return(stair[n])
