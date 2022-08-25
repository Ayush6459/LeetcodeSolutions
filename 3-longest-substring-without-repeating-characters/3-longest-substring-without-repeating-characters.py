class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        length = len(s)
        s1 = set()
        res = 0
    
        while j<length:
            if s[j] in s1:
                s1.remove(s[i])
                i+=1
            else:
                s1.add(s[j])
                j+=1
                res = max(res,j-i)
        return res