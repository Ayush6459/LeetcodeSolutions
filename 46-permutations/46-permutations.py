class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''# method 1 
        res = list()
        map = dict.fromkeys(range(len(nums)),0)
        self.generate(nums,[],res,map)
        
        return res
    def generate(self,nums,temp,res,map):
        if len(temp) == len(nums):
            print(temp)
            res+=[temp]
        for i in range(len(nums)):
            if not map[i]:
                map[i] = 1
                temp.append(nums[i])
                self.generate(nums,temp,res,map)
                temp.pop()
                map[i]=0
        return res'''
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)