class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
            approach one : By counting the the number and returining the number which came once.
        '''
        '''
        approach two :  by duing XOR of every element of the nums 
        since all the element which came twice will cancle out the for themselves and only the element which came once will reflect in our result.
        '''
        res = 0 # Sicnce (a XOR 0 = a ) 
        for i in nums:
            res = i^res
            
        return res
        