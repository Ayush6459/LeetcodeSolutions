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
        res = []
        def InOrder(root,low,high):
            if not root:
                return
            if root.val>=low and root.val<=high:
                res.append(root.val)
            InOrder(root.left,low,high)
            InOrder(root.right,low,high)
        InOrder(root,low,high)
        return sum(res)
    
        
        
        