# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        if root.left==None and root.right==None:
            return True
        s=0
        if root.left:
            s+=root.left.val
        if root.right:
            s+=root.right.val
        return root.val==s and self.checkTree(root.left) and self.checkTree(root.right)
        