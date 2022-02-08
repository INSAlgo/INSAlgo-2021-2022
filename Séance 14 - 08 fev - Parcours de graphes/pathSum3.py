class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        nbOfSolution = [0]
        
        def DFS(node):

            if node is None:
                return []
            
            currentPaths = [node.val]
            if node.val==targetSum:
                nbOfSolution[0]+=1
            

            for childPath in DFS(node.left)+DFS(node.right):
                if node.val+childPath==targetSum:
                    nbOfSolution[0]+=1
                currentPaths.append(node.val+childPath)
            
            return currentPaths

        DFS(root)
        return nbOfSolution[0]
