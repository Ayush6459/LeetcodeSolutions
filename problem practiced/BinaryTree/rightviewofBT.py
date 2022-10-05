
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
    pass