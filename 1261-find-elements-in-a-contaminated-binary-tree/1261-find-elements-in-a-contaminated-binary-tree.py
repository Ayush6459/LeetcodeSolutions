# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.values = set()
        self.recover()
    def find(self, target: int) -> bool:
        if target in self.values : return True
        else:
            return False
        
    def recover(self):
        if self.root:
            self.root.val = 0 # make the root value as zero
            self.values.add(self.root.val) # add the root value in the set
            q = [self.root] # put the root node in queue
            # iterate throgh the root in level order and transform the values
            while q:
                node = q.pop(0)
                if node.left is not None:
                    node.left.val = 2*node.val + 1
                    self.values.add(node.left.val)
                    q.append(node.left)
                    
                if node.right is not None:
                    node.right.val = 2*node.val +2
                    self.values.add(node.right.val)
                    q.append(node.right)
                    
                
                
                
                

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)