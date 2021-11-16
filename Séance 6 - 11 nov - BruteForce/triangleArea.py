def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        
        def calculateArea(a,b,c): 
            area = abs(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))/2 
            # la formule de calcul d'aire
            return area
            
        
        answer = 0
        for a in points:
            for b in points:
                for c in points:
                    answer = max(answer, calculateArea(a, b, c))
            
        return answer