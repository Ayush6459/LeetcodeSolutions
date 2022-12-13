class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = set(nums1)
        ans = {i for i in nums2 if i in nums1}
        return ans