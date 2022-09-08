# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or ( root.val == p.val) or (root.val == q.val):
            #print(root.val)
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        
        right =  self.lowestCommonAncestor(root.right,p,q)
        if left is None:
            return right
        elif right is None :
            return left
        else:
            return root