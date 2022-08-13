class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ = sum(arr[:k])
        out = 1 if summ//k >= threshold else 0
        for i in range(1, len(arr)-k+1):
            summ -= arr[i-1]
            summ += arr[i+k-1]
            if summ//k >= threshold: out += 1
            
        return out