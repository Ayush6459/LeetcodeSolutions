class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        i = 0 
        j =0
        count =0
        x = str(num)
        while j<len(x):
            if j-i+1<k:
                j+=1
            elif j-i+1 == k:
                if int(x[i:j+1])!=0 and num%int(x[i:j+1])==0 :
                    count+=1
                    
                i+=1
                j+=1
        return count
        