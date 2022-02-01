# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
   
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        queue = deque()
        
        queue.append((root,1))

        maxDepth = 0
        
        while queue:
            currentNode,currentLevel = queue.popleft()
            if currentNode is None:
                continue
            else:
                maxDepth = max(maxDepth,currentLevel)
                queue.append((currentNode.left,currentLevel+1))
                queue.append((currentNode.right,currentLevel+1))
        return(maxDepth)
        
