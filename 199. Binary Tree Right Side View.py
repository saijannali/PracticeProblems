# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        
        q = [root]
        result = []
        while q:
            lvl_size = len(q)
            for _ in range(lvl_size):
                node = q.pop(0)
                
                if _ == lvl_size-1:
                    result.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
