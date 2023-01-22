class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0: return 0 if nums1 == nums2 else -1
        positive_diff  = 0
        negative_diff = 0
        
        for x,y in zip(nums1,nums2):
            if (x-y) % k != 0:
                return -1
            else:
                if x-y<0:
                    negative_diff+=(x-y)
                else:
                    positive_diff+=(x-y)
        print(positive_diff)
        print(negative_diff)
        return positive_diff//k if positive_diff+negative_diff==0 else -1
         