# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
    
    def helper(self, root, pathSum):
        if root is None:
            return 0
        
        pathSum = 10 * pathSum + root.val
        print(pathSum)
        
        #if leaf
        if not root.right and not root.left:
            return pathSum
        
        return self.helper(root.left, pathSum) + self.helper(root.right, pathSum)
        
    
        
        
