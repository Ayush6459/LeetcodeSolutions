# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # count the left level and right level for root
        # if both the levels are equal then return the total node = 2^h -1
        # else call again for left node of root and roght node of root
        
        left_level = 1
        left_node = root.left
        while left_node:
            left_node = left_node.left
            left_level +=1
        right_level = 1
        right_node = root.right
        while right_node:
            right_node = right_node.right
            right_level +=1
        if left_level == right_level:
            return pow(2,left_level)-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)