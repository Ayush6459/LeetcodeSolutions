class Solution:
    def minimumSum(self, num: int) -> int:
        l = []
        while num>0:
            l.append(num%10)
            num = num//10
        l.sort()
        
        x,y,z,a = l
        return z + a + 10*x + 10*y