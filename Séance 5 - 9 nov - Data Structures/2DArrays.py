def hourglassSum(arr):
    max = -9*7
    
    for i in range(4):
        
        for j in range(4):
            
            sumH=arr[j][i]+arr[j][i+1]+arr[j][i+2]+arr[j+1][i+1]+arr[j+2][i]+arr[j+2][i+1]+arr[j+2][i+2]
            if sumH>max:
                max=sumH
    return max
