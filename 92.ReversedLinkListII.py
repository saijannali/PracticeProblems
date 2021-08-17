# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        #corner case
        if left == right:
            return head
        
        #skip left -1 node
        curr, prev = head, None
        i = 0
        while curr != None and i < left-1:
            prev, curr = curr, curr.next
            i += 1
        
        before_left = prev
        left_node = curr
        
        #reverse right-left+1
        i=0
        while curr != None and i < right-left+1:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1
        
        #attach
        
        if before_left != None: #left != 1
            before_left.next = prev
        else:
            head = prev
            
        left_node.next = curr
        return head
            
            
