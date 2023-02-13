# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    head = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def revPreOrder(node: TreeNode) -> None:
            if node.right: revPreOrder(node.right)
            if node.left: revPreOrder(node.left)
            node.left, node.right, self.head = None, self.head, node
        if root: revPreOrder(root)
            
        