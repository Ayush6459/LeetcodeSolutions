'''
Given a linked list of N nodes. The task is to reverse this list.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.
'''

#Function to reverse a linked list.
def reverseList(head):
    # Code here
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

# recursive function to reverse a linked list
def reverseList(head,prev):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverseList(next,head)
