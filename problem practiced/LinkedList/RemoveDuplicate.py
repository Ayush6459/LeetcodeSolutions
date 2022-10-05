# Remove Duplicate Element from a Sorted Linked List

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
example :
Input: 1->2->3->3->4->4->5
Output: 1->2->3->4->5
'''
def removeDuplicates(head):
    if head is None:
        return head
    curr = head
    while curr.next and curr.next!=None: 
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head 


