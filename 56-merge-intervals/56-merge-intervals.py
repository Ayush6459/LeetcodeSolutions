class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        sort the array on the basis of the end interval
        then merge those whose intervals are overlapping
        '''
        intervals.sort(key=lambda x:x[0])
        i = 0
        j =1
        res = []
        while j<len(intervals):
            if intervals[i][1]>=intervals[j][0]:
                intervals[i][1]=max(intervals[i][1],intervals[j][1])
                intervals.pop(j)
            else:
                i+=1
                j+=1
        
        return intervals