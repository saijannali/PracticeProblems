"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        root.next = None
        q = [root]
        while q:
            lvl_size = len(q)
            for _ in range(lvl_size):
                curr_node = q.pop(0)
                
                #set next pointers
                if _ == lvl_size-1:
                    curr_node.next = None
                else:
                    curr_node.next = q[0]
                #add children to q
                if curr_node.left:
                    q.append(curr_node.left)
                    
                if curr_node.right:
                    q.append(curr_node.right)
        return root
                    
        
