class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        length = len(s)
        count = 0
        while j<length:
            if j-i+1<3:
                j+=1
            elif j-i+1 == 3:
                s1 = set(s[i:j+1])
                if len(s1)==3:
                    count+=1
                i+=1
                j+=1
                    
        return count
                