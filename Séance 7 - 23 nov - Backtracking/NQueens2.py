class Solution:
    def totalNQueens(self, n: int) -> int:
        
        
        board = [[0 for _ in range(n)]for _ in range(9)]
        global numSolutions
        numSolutions=0
        
        def validPosition(board,position:(int,int))-> bool:
            
            for x in range(position[0],-1,-1):
                
                if board[x][position[1]]:
                    return False
            
            currentX,currentY = position[0],position[1]
            
            while currentX>-1 and currentY>-1:
                if board[currentX][currentY]:
                    return False
                else:
                    currentX-=1
                    currentY-=1
                    
            currentX,currentY = position[0],position[1]
            
            while currentX>-1 and currentY<n:
                if board[currentX][currentY]:
                    return False
                else:
                    currentX-=1
                    currentY+=1
            
            return True
            
        
        def placeQueen(board,col):
            
            for line in range(n):
                
                coords=(col,line)
                
                if validPosition(board,coords):
                    if col==n-1:
                        global numSolutions
                        numSolutions+=1
                        return
                    board[col][line]=1
                    placeQueen(board,col+1)
                    board[col][line]=0
            return
        
        placeQueen(board,0)
        return(numSolutions)
                
