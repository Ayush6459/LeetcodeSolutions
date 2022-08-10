# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        
        if root == None:
            return False
        
        return self.isSameTree(root, subRoot) | self.isSubtree(root.left, subRoot) |                                self.isSubtree(root.right, subRoot) 
        
    def isSameTree(self, p, q):
        
        if p == None and q == None:
            return True
        
        if p == None  or q == None:
            return False
        
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        