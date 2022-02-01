class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        numIslands = 0
        visited = [[False for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and not visited[i][j]:
                    
                    d = deque()
                    d.append((j,i))
                    
                    while d:
                        currentX,currentY = d.popleft()
                        if currentX<0 or currentY<0 or currentX==n or currentY==m:
                            continue
                        if visited[currentY][currentX]:
                            continue
                        visited[currentY][currentX]=True
                        
                        if grid[currentY][currentX]=="0":
                            continue
                        
                        
                        d.append((currentX-1,currentY))
                        d.append((currentX+1,currentY))
                        d.append((currentX,currentY-1))
                        d.append((currentX,currentY+1))
                    numIslands+=1
        return numIslands
