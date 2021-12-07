
def getWays(n, c):
    
    knapsack=[0 for i in range(n+1)]
    knapsack[0]=1
    for i in range(len(c)):
        
        for j in range(c[i],n+1):
            knapsack[j] += knapsack[j-c[i]]

    return knapsack[n]
