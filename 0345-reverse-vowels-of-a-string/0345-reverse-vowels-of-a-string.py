class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s)-1
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        while i<j:
            if s[i] in vowel and s[j] in vowel:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
            elif s[i] in vowel and s[j] not in vowel:
                j-=1
            elif s[j] in vowel and s[i] not in vowel:
                i+=1
            else:
                i+=1
                j-=1
        return ''.join(s)