from collections import Counter 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = Counter(stones)
        res = 0
        for i in jewels:
            if i in freq:
                res+=freq[i]
        return res