def Inorder(root, arr):
    if root:
        Inorder(root.left, arr)
        arr.append(root.data)
        Inorder(root.right, arr)
    return arr

# function to put element from array to BST inorder

def arrayToBST(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = arrayToBST(arr, start, mid - 1)
    root.right = arrayToBST(arr, mid + 1, end)
    return root

# TreeNode Class

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to balance a given BST

def balanceBST(root):
    if root is None:
        return None
    arr = Inorder(root, [])
    return arrayToBST(arr, 0, len(arr) - 1)






# Driver code

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)
    root = balanceBST(root)
    