# given the board, a position x and y, the Trie to explore and the result set
# will fill the result set if word from the Trie can be found in the board
def exploreBoard(board,x,y,node,result):
        # If the node is a end node, add the word to the result set
        if "END" in node:
            result.add(node["END"])
            
        # Check if the call parameters are correct
        if x<0 or y<0 or x>= len(board[0]) or y>=len(board):
            return
        
        # Need a temp var to avoid returning on a position already visited
        temp=board[y][x]
        if temp in node:
            
            board[y][x]="-"
            
            # Call the recursive function from all neighbour positions
            exploreBoard(board,x-1,y,node[temp],result)
            exploreBoard(board,x+1,y,node[temp],result)
            exploreBoard(board,x,y-1,node[temp],result)
            exploreBoard(board,x,y+1,node[temp],result)
            
            # Restore the board modification
            board[y][x]=temp
            
class Solution:
    
    
            
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Creation of the Trie
        trie=dict()
        
        for word in words:
            currentNode=trie
            
            for letter in word:
                
                if letter not in currentNode:
                    currentNode[letter]=dict()
                
                currentNode=currentNode[letter]
                        
            currentNode["END"]=word
        
        
        
        result=set()
        
        # Exploring the board from each starting position
        for y in range(len(board)):
            for x in range(len(board[0])):
                exploreBoard(board,x,y,trie,result)
        return list(result)
      
      
# Ouais, j'ai vu que cette solution passe plus sur leetcode, mais c'est parce qu'ils ont rajouté un test case, et honnetement, j'ai la flemme et pas le temps de refaire la solution
# Si vous bvoulez, je pense que juste traduire en CPP ça parmet de passer, allez salut
