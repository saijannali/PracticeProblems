# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #fast and slow pointer, slow represents last unique node, fast is the next unique node
        
        #corner case
        if head is None:
            return head
        
        slow, fast = head, head
        
        while fast != None and fast.next != None:
            if fast.next.val != fast.val:
                slow.next.val = fast.next.val
                slow = slow.next
            fast = fast.next
        
        slow.next = None
        
        return head
        
        
