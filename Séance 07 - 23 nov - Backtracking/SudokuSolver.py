class Solution:
    
        
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isCorrect(board, x,y,value):
        
            line = board[x]
            col = [board[i][y] for i in range(9)]

            square = [board[x-x%3+i][y-y%3+j] for i in range(3) for j in range(3)]
            
            if value in line or value in col or value in square:
                return False
            else:
                return True
            
            
        
        def tryValue(board, x,y):
            if x==9:
                return True
            nextX = x+1 if y==8 else x
            nextY = (y+1)%9
            if board[x][y] == ".":
                for value in range(1,10):
                    if isCorrect(board,x,y,str(value)):
                        board[x][y]=str(value)
                        if tryValue(board,nextX,nextY):
                            return True
                        board[x][y]="."
                else:
                    return False
                
            else:
                return tryValue(board,nextX,nextY)
                
        tryValue(board,0,0)
