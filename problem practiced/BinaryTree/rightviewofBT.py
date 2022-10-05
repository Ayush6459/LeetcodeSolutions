
# this solution is using level order traversal concept
def rightSideView(root):
    if not root:
        return
    q = []
    q.append(root)
    ans = []
    while q :
        ans.append(q[-1].val)
        temp = []
        for i in q:
            temp.extend([i.left,i.right])
        q = [i for i in temp if i]

    return ans


# solution using dfs 

def dfsRightSideView(root):
    # The plan here is to dfs the tree, right-first
    # (opposite of  the usual left-first method), and
    # keeping track of the tree levels as we proceed. The
    # first node we visit on each level is the right-side view
    # node. We know it's the first because the level will be
    # one greater than the length of the current answer list.
    ans = []
    def dfs(node=root,level=1):
        if not node : return 
        if len(ans)<level:
            ans.append(node.val)
        dfs(node.right,level+1)
        dfs(node.left,level+1)
        return 
    dfs(root)
    return ans 
    
