# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head=head.next
        return self.sortedArrayToBST(arr)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        n = len(nums)
        mid = n // 2

        node = TreeNode(nums[mid])

        node.left = self.sortedArrayToBST(nums[:mid].copy())
        node.right = self.sortedArrayToBST(nums[mid+1:].copy())

        return node