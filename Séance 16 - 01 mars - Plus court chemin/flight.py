import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        memoi = {} #car sans memoization ça passe paaaaaaaaaaaaas
        
        def dfs(currentFlight, currentNum):
            
            if currentNum > k:
                return math.inf
            
            elif currentFlight == dst: # if start = end
                return 0
            
            elif (currentFlight, currentNum) in memoi:
                return memoi[(currentFlight, currentNum)]

            cheapest = math.inf
            
            for flight in flights:
                
                if flight[0] == currentFlight:
                    cheapest = min(cheapest, flight[2] + dfs(flight[1], currentNum + 1))

            memoi[(currentFlight, currentNum)] = cheapest #memoization
            
            return cheapest
        
        answer = dfs(src, -1) 
        print(memoi, src, dst)
        
        if(answer!=math.inf):
            return answer
        else:
            return -1
