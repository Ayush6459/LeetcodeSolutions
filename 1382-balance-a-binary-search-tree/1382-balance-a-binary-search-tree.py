# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # this is the solution using O(N) extrat space and O(n) time complexity 
        # The idea is to first store the value of BST in an array using Inorder traversal
        # since inorder Traversal gives the sorted list so we can use this array to form a BST
        def Inorder(root, arr):
            if root:
                Inorder(root.left, arr)
                arr.append(root.val)
                Inorder(root.right, arr)
            return arr
        
        def arrayToBST(arr, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(arr[mid])
            root.left = arrayToBST(arr, start, mid - 1)
            root.right = arrayToBST(arr, mid + 1, end)
            return root
        
        if root is None:
            return None
        arr = Inorder(root, [])
        return arrayToBST(arr, 0, len(arr) - 1)