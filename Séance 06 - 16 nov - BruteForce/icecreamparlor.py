def icecreamParlor(m, arr):
    for x in range(len(arr)):
        n=m-arr[x]
        for y in range(len(arr)):
            o=n-arr[y]
            if(o==0) and x!=y:
                return (x+1,y+1)
