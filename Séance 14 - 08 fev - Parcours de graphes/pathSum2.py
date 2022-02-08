class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def DFS(node,pathSum,currentPath):
            
            if node is None:
                return
            
            if node.left is None and node.right is None:
                if pathSum+node.val==targetSum:
                    solution.append(currentPath+[node.val])
                return
            
            DFS(node.left,pathSum+node.val,currentPath+[node.val])
            DFS(node.right,pathSum+node.val,currentPath+[node.val])
            
        
        solution = []
        DFS(root,0,[])
        return solution
