class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        rem = [0]*60
        for i in time:
            rem[i%60]+=1
        count = 0
        count+=((rem[0]-1)*rem[0])//2
        count+=((rem[30]-1)*rem[30])//2
        for i in range(1,30):
            count+=rem[i]*rem[60-i]
        return count