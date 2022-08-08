# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
         
        dummy = ListNode(0)
        prev = dummy
        dummy.next =head
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val==head.next.val:
                    head = head.next
                prev.next = head.next
            else :
                prev = prev.next
            head=head.next
        return dummy.next