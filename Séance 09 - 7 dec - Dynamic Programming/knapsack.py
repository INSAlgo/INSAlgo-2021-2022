
def unboundedKnapsack(k, arr):
    knapsack=[0 for i in range(k+1)]
    knapsack[0]=1
    for i in range(len(knapsack)):
        if knapsack[i]==0:
            continue
        else:
            currentmax=i
        for elem in arr:
            if i+elem<=k:
                knapsack[i+elem]=1
    return currentmax

for i in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(unboundedKnapsack(k,arr))