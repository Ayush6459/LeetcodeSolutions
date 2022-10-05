'''
 delete the node with only the pointer given to it 
 you can assume that the node to be deleted is not the last node in the list
 example:
 Input: 1->2->3->4->5-> , node = 4
 Output: 1->2->3->5
'''

# solution
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
    return node


