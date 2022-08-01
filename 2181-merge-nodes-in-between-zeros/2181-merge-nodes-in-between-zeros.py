# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        d=ListNode(0)
        t=0
        r=ListNode(0,d)
        while head:
            if head.val!=0:
                t+=head.val
            else:
                if t!=0:
                    d.next=ListNode(t)
                    d=d.next
                    t=0
            head=head.next
        return r.next.next
    
        
        
        
        
        
        