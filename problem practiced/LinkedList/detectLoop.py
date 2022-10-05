'''
    Given a singly linked list find if there is a cycle in it. 
    if cycle presennt return the starting node of the cycle else return None.
    example:
    Input: 1->2->3->4->2
    Output: 2

'''
# Definition for singly-linked list. 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# iterative solution using hash table
def detectCycle(head) :
    d = set()
    if head== None or head.next == None :
        return None
    curr = head
    
    while curr!=None:
        if curr in d:
            return curr
        d.add(curr)
        curr = curr.next
    return None

# Implementation of Floyd’s Cycle-Finding Algorithm:
# https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/

def detectCycle1(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

# implementation using dummy node cocept
def detectCycle2(head):
    tmp = ListNode()
    curr = head
    while curr != None:
        if curr.next == None :
            return None
        if curr.next == tmp:
            return tmp
        curr_next = curr.next
        curr.next = tmp
        curr = curr_next
    return None

# above solution is not correct yet 
