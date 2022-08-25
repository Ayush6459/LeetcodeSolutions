class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        s1 = set()
        res = 0
        
        for j in range(len(s)):
            while s[j] in s1:
                s1.remove(s[i])
                i+=1
            s1.add(s[j])
            res = max(res,j-i+1)
        return res