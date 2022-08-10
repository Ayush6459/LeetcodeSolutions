# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        if root and root.left==None and root.right==None:
            return True
        
        return self.compare(root.left,root.right)
        
        
    def compare(self,r1,r2):
        if not r1 and not r2:
            return True
        if r1 and not r2 or r2 and not r1:
            return False
        return r1.val == r2.val and self.compare(r1.left,r2.right) and self.compare(r1.right,r2.left)