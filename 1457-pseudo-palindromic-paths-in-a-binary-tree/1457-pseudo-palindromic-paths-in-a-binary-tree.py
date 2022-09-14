# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, node: Optional[TreeNode],mask  = 0) -> int:
        # mask has 9 spaces corresponding to 1 to 9 (0b xxxxxxxxx)
		
        mask ^= 1 << node.val - 1
		# e.g. val = 4 and current mask is 0b011000011
		# the space 4 of mask is 0 -> change it to 1 (which means the current numbers of 4 is even)
		# -> mask now is 0b011001011
		# if that space is 1 then change it to 0 (the numbers of 4 is odd)
		
        if node.left is None and node.right is None: return int((mask & -mask) == mask)
		# a trick to check if mask is a power of 2 (which means mask contains 0 or 1 ones)
	    # if it does return 1 else 0
		
        return (
			self.pseudoPalindromicPaths(node.left, mask) if node.left else 0
		) + (
			self.pseudoPalindromicPaths(node.right, mask) if node.right else 0
		)