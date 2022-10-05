
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2) :

    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next



def Merge(l1,l2):
    # check for empty list if any one is empty return the other
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    # if both are not empty return null
    if l1 == None and l2 == None:
        return None
    head,tail = None,None 
    # check for the first value of both list if l.val > l2.val then add l2 to the head else add l1
    if l1.val > l2.val:
        head = l2
        tail = l2
        l2 = l2.next
    else:
        head = l1
        tail = l1
        l1 = l1.next
    # now loop through both list and check for each value and update the list accordingly
    while l1 and l2:
        if l1.val > l2.val:
            tail.next = l2
            tail = l2
            l2 = l2.next
        else:
            tail.next = l1
            tail = l1
            l1 = l1.next
    # if any one of the list is empty then add the remaining list to the tail
    if l1 is None:
        tail.next = l2
    if l2 is None:
        tail.next = l1
    return head
