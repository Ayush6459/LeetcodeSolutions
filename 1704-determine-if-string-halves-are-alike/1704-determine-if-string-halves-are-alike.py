class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)//2
        a = 0
        b = 0
        for i in range(n):
            if s[i] in vowels:
                a += 1
            if s[-i - 1] in vowels:
                b += 1
        if a == b:
            return True
        else:
            return False