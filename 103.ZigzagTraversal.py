# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #O(n)
        #O(n) + O(n/2) --> O(n)
        if root is None:
            return []
        
        zigzag = True
        q = []
        result = []
        q.append(root)
        
        while q:
            lvl_size = len(q)
            temp = deque()
            for _ in range(lvl_size):
                curr_node = q.pop(0)
                if zigzag:
                    temp.append(curr_node.val)
                else:
                    temp.appendleft(curr_node.val)
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                    
            zigzag = not zigzag
            result.append(temp)
            
        return result
