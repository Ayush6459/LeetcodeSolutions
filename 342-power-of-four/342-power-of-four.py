class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        n = f'{n:b}'
        x = n.count('1')
        y = n.count('0')
        if x>1:
            return False
        if x == 1 and y%2!=0:
            return False
        return True