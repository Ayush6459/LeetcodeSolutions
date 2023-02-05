# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        '''
        # using hashset
        s = set()
        curr = headA
        while curr:
            s.add(curr)
            curr= curr.next
        curr = headB
        while curr:
            if curr in s:
                return curr
            curr = curr.next
        return None
        '''
        # using two pointers 
        currA = headA
        currB = headB
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        return currA
        