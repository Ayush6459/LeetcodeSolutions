'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

example:
Input: 1->2->3->4->5->6->7->8->9->10
output: 6
Input: 1->2->3->4->5
Output: 3
'''
def middleNode(head):
    # Code here
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow