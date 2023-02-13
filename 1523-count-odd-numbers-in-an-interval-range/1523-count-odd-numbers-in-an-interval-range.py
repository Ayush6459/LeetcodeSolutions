class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not (low & 1):
            low+=1
        return 0 if low>high else (high-low)//2+1