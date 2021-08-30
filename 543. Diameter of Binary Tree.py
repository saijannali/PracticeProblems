class Solution:
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.max
    
    def helper(self, root):
        if root is None: 
            return 0
        
        l_height = self.helper(root.left)
        r_height = self.helper(root.right)
        
        if l_height + r_height > self.max:
            self.max = l_height + r_height
            
        return max(l_height,r_height) + 1
    
        
