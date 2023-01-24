# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        # iterate the right pointer ahead by n
        for i in range(n):
            right=right.next
            
        # here we want to remove the first node
        # note that if linked list is length 3 and we want to remove the third node from end:
        # right will iterate starting at head 3 times and be past the end
        # thus here we can just return the first node removed aka head is head.next
        if not right:
            return head.next
        
        # iterate right&left pointer till it is at end
        # why "while right.next"? stopping point is when right is at the last node (so that left is at node before one to remove)
        while right.next:
            right = right.next
            left = left.next
        
        # at this point left is at the prev of node to remove
        left.next= left.next.next
        return head