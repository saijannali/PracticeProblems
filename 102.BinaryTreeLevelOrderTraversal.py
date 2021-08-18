# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #O(n)
        #O(n) + O(n/2) --> O(n)
        if root is None:
            return []
        
        result = []
        q = []
        q.append(root)
        while q:
            lvl_size = len(q)
            temp = []
            for _ in range(lvl_size):
                curr_node = q.pop(0)
                temp.append(curr_node.val)
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                
            result.append(temp)
            
        print(result)
        return result
                
