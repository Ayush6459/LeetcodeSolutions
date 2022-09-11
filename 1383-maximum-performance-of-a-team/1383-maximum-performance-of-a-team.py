class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        # build tuples ( efficiency, speed ) so that we can sort it later
        candidates = zip(efficiency, speed)
        # default sort mode is ascending. use `reverse = True` to sort in descending
        candidates = sorted(candidates, key=lambda x: x[0], reverse=True)
        # Using Example 1: 
        # speed: [2, 10, 3, 1 ,5, 8] and efficiency: [5, 4, 3, 9, 7, 2]
        # after sort, it becomes
        # candidates: [(9, 1), (7 ,5), (5, 2), (4, 10), (3, 3), (2, 8)]
        speedSum, ans = 0, 0
        # in python, it usually refers to heap 
        heap = []
        # iterate each tuple
        for e, s in candidates:
            # put the speed to heap
            heapq.heappush(heap, s)
            # add to speedSum
            speedSum += s
            # we only need to choose at most k engineers
            # hence if the queue size is greater than k
            # we need to remove a candidate
            if len(heap) > k:
                # who to remove? of course the one with smallest speed
                speedSum -= heapq.heappop(heap)
            # calculate the performance
            ans = max(ans, speedSum * e)
        return ans % MOD