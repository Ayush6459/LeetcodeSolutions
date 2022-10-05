def pathSum(root,target,res,currPath):
    if root is None:
        if sum(currPath)==target:
            res.append(currPath)
        return 
    pathSum(root.left,target,res,currPath+[root.val])
    pathSum(root.right,target,res,currPath+[root.val])
    return res 

