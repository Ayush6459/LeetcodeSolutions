class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        '''
        Idea:
First, we store in a map the frequencies of the strings, so that we can find easily which strings we have and how many.
Now, we iterate through the freq map.
For every string:

We check if it's a prefix of our target.
If yes, first case is that the target is exactly twice the prefix. If so, we add frq*(frq-1) to res.
The reason is that the number of combinations for a pattern with frequency n is n * (n-1).
Otherwise we look in the map if we have the suffix, if so - we add the product of their frequencies to res.
Time Complexity: O(n)
Space Complexity: O(n)

        '''
        ans = 0 
        freq = collections.Counter(nums)
        for k,v in freq.items():
            if target.startswith(k): 
                suffix = target[len(k):]
                ans += v * freq[suffix]
                if k == suffix: ans -= freq[suffix]
        
        return ans
            