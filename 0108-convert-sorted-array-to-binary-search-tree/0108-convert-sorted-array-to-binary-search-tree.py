# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        parent = set()
        n = len(nums)
        def helper(start,end):
            # base case 
            if start<0 or end >= n:return None
            mid = (start+end)//2
            temp = TreeNode(nums[mid])
            parent.add(mid)
            if mid-1>=0 and mid-1 not in parent :#check if the index is covered or not 
                temp.left = helper(start,mid-1)
            if mid+1<n and mid+1 not in parent :
                temp.right = helper(mid+1,end)
            return temp 
        return helper(0,n-1)