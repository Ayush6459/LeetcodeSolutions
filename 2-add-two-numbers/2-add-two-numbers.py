# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        
        h3 = ListNode(0)
        dummy = h3
        carry =0
        while h1 and h2:
            
            if h1.val+h2.val+carry<=9:
                dummy.next =ListNode(h1.val+h2.val+carry)
                carry =0
                dummy = dummy.next
            else:
                dummy.next =ListNode((h1.val+h2.val+carry)%10)
                carry = 1
                dummy = dummy.next
            h1 = h1.next
            h2 = h2.next
            
        if h1:
            while h1:
                if h1.val+carry<=9:
                    dummy.next =ListNode(h1.val+carry)
                    carry =0
                    dummy = dummy.next
                else:
                    dummy.next =ListNode((h1.val+carry)%10)
                    carry =1
                    dummy = dummy.next
                h1 = h1.next
        elif h2:
            while h2:
                if h2.val+carry<=9:
                    dummy.next =ListNode(h2.val+carry)
                    carry =0
                    dummy = dummy.next
                else:
                    dummy.next =ListNode((h2.val+carry)%10)
                    carry =1
                    dummy = dummy.next
                h2 = h2.next
        if carry ==1:
            dummy.next = ListNode(carry)
            carry = 0
            dummy = dummy.next
                
        return h3.next