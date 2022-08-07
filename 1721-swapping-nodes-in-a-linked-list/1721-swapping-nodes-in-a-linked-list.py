# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 1
        curr = head
        while count<k:
            curr = curr.next
            count+=1
            
        start = curr
        end = curr
        curr = head
        while end.next :
            end = end.next
            curr = curr.next
        start.val , curr.val = curr.val,start.val
        
        return head
        
            
        