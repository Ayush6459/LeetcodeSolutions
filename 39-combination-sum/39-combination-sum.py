class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.generateCombination(candidates,target,0,[],[])
    def generateCombination(self,arr,target,index,temp,res):
        if index==len(arr):
            if target == 0:
                res.append(temp)
            return 
        
        if arr[index]<=target:
            self.generateCombination(arr,target-arr[index],index,temp+[arr[index]],res)
            
        self.generateCombination(arr,target,index+1,temp,res)
        
        return res