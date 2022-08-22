# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p1 = head
        middle = self.middleNode(p1)
        p2 = middle.next
        middle.next = None
        # reverse the next half part
        p2 = self.reverseList(p2)
        
        while p1 and p1.next and p2:
            temp = p2
            p2= p2.next
            temp.next = p1.next
            p1.next = temp
            p1 = p1.next.next
        return head
        
        
    def middleNode(self,head):
        # Code here
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self,head):
        # Code here
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev