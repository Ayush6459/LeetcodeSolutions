from itertools import combinations
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        curr = 0
        ans = 0
        for x in range(1, n + 1):
            if x in banned: continue
            if curr + x > maxSum: break
            curr += x
            ans += 1
        
        return ans