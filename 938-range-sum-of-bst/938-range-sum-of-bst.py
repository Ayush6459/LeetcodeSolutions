# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.r = 0
        def InOrder(root,low,high):
            if not root:
                return
            if root.val>=low and root.val<=high:
                self.r+=root.val
            InOrder(root.left,low,high)
            InOrder(root.right,low,high)
        InOrder(root,low,high)
        return self.r
    
        
        
        