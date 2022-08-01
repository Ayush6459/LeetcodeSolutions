# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        middle ,prev= self.middleNode(head)
        prev.next = None
        last = self.reverseList(middle)
        curr = head
        maxSum = 0
        while curr and last:
            maxSum = max(maxSum,curr.val+last.val)
            curr = curr.next
            last = last.next
        return maxSum
    
    
    def middleNode(self,head):
        # Code here
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return slow,prev
    
    def reverseList(self,head):
        # Code here
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    