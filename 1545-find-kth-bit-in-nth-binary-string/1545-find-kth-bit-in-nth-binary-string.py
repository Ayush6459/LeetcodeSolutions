class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n ==1 and k == 1:
            return "0"
        mid = pow(2,n)//2
        if k == mid :
            return "1"
        if k<mid:
            return self.findKthBit(n-1,k)
        if k>mid:
            x = self.findKthBit(n-1,mid-(k%mid))
            return "0" if x == "1" else "1"
        