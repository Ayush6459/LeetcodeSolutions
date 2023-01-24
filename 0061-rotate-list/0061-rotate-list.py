# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head : return head
        n = self.lengthofList(head)
        k = k%n
        print(n,k)
        if k==0:return head
        count = 1
        pivot = head
        dummy = ListNode()
        while count<n-k:
            pivot = pivot.next
            count+=1
        right = pivot.next
        pivot.next = None
        dummy.next = right
        while  right.next:
            right = right.next
        
        right.next = head
        
        return dummy.next
        
    def lengthofList(self,head):
        count = 0
        while head:
            head= head.next
            count+=1
        return count