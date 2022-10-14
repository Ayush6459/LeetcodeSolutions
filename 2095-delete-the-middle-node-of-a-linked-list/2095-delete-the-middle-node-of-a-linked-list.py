# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None or head.next == None:
            return None
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev= slow
            slow = slow.next
            fast = fast.next.next
        if prev!=None:
            if prev.next!=None:
                if prev.next.next!=None:
                    prev.next = prev.next.next
                else:
                    prev.next=None
            else:
                prev = None
        
        return head