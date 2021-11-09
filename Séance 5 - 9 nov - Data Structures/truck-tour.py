def truckTour(petrolpumps):
    d = deque()
    for i in petrolpumps:
        print(i[0]-i[1])
        d.append(i[0]-i[1])
    
    sumSegLeft = 0
    minFuelNeeded = 0
    currentId=0
    while(d):
        currentSum = 0
        for value in d:
            if currentSum<0:
                sumSegLeft+=d.popleft()
                minFuelNeeded=min(minFuelNeeded,sumSegLeft)
                break
            currentSum+=value
        else:
            if minFuelNeeded+currentSum<0:
                sumSegLeft+=d.popleft()
                minFuelNeeded=min(minFuelNeeded,sumSegLeft)
            else:
                return currentId 
        currentId+=1
                
