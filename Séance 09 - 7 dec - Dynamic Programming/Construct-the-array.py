def countArray(n, k, x):
    dp=[0,1]
    for i in range(1,n):

        buf=dp[1]+dp[0]*(k-2)    
        dp[1]=dp[0]*(k-1)
        dp[0]=buf
    if x==1:
        return(dp[1]%1000000007)
    else:
        return(dp[0]%1000000007)