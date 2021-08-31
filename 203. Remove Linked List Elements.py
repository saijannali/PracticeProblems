# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #fast and slow pointer approach
        #fast after slow and fast will check for vals
        #if vals found, set slow.next.val = fast.val and move slow pointer 
        #move fast pointer regardless
        
        new_head = ListNode(0)
        new_head.next = head
        
        slow, fast = new_head, head
        
        while fast:
            if fast.val != val:
                slow.next.val = fast.val
                slow = slow.next
            fast = fast.next
        slow.next = None
        return new_head.next
            
        
