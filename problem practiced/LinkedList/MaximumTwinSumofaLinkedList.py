def pairSum( head) :
    middle, prev = middleNode(head)
    prev.next = None
    last = reverseList(middle)
    curr = head
    maxSum = 0
    while curr and last:
        maxSum = max(maxSum, curr.val+last.val)
        curr = curr.next
        last = last.next
    return maxSum


def middleNode(head):
    # Code here
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    return slow,prev

def reverseList(head):
    # Code here
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev