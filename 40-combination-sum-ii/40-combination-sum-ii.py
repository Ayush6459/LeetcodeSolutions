class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(curr,index,target):
            if target == 0:
                res.append(curr.copy())
            if target<=0:
                return
            prev = -1
            for i in range(index,len(candidates)):
                if candidates[i]==prev:
                    continue
                curr.append(candidates[i])
                backtrack(curr,i+1,target-candidates[i])
                curr.pop()
                prev = candidates[i]
                
        backtrack([],0,target)
        return res