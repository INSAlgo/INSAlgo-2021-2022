
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def DFS(node,pathSum):
            
            if node is None:
                return False
            
            if node.left is None and node.right is None:
                if pathSum+node.val==targetSum:
                    return True
                else:
                    return False
            
            return DFS(node.left,pathSum+node.val) or DFS(node.right,pathSum+node.val)
            
            
        return DFS(root,0)
