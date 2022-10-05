'''
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. If the two linked lists have no intersection at all, 
return null.


'''


def getIntersectionNode(headA, headB) :
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

    '''
    # using count difference 
        c1 =0
        c2 =0
        curr=headA
        while curr:
            c1+=1
            curr=curr.next
        curr = headB
        while curr:
            c2+=1
            curr=curr.next
        diff=0
        if c1>c2:
            diff =0
            currA = headA
            while diff<c1-c2:
                currA = currA.next
            currB = headB
            while currA!=None and currB!=None:
                if currA==currB:
                    return currA
                currA=currA.next
                currB = currB.next
        elif c1<=c2:
            diff =0
            currB = headB
            while diff<c2-c1:
                currB = currB.next
            currA = headA
            while currA!=None and currB!=None:
                if currA==currB:
                    return currA
                currA=currA.next
                currB = currB.next
        else:
            return None
    '''

    
