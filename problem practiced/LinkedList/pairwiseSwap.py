'''
given a singly  linked list swap the pair of nodes in list
example:
Input : 1->2->3->4->5->6->7->8->9->10
Output : 2->1->4->3->6->5->8->7->10->9
'''

# using data swaping technique
def swapPair(head):

    curr = head 
    while curr !=None and curr.next!=None:
        curr.data,curr.next.data = curr.next.data,curr.data
        curr = curr.next.next
    return head

# using pointer swaping technique
def swapPair(head):
    if head == None or head.next == None:
        return head
    curr = head.next.next
    prev = head
    head = head.next
    head.next = prev
    while curr != None and curr.next != None:
        prev.next=curr.next
        prev = curr
        next = curr.next.next
        curr.next.next = curr
        curr = next

    prev.next = curr
    return head
