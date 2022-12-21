class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
            Idea : 
            If every element in the sorted array were to appear exactly twice, they would occur in pairs at indices i, i+1 for all even i.

Equivalently, nums[i] = nums[i+1] and nums[i+1] != nums[i+2] for all even i.

When we insert the unique element into this list, the indices of all the pairs following it will be shifted by one, negating the above relationship.

So, for any even index i, we can compare nums[i] to nums[i+1].

If they are equal, the unique element must occur somewhere after index i+1
If they aren't equal, the unique element must occur somewhere before index i+1
Using this knowledge, we can use binary search to find the unique element.
        
        '''
        
        l=0
        h=len(nums)-1
        while l<h:
            m=(l+h)//2
            n = m+1 if m%2 == 0 else m-1 # here we are deciding if our mid index is odd or even if it is even then we will compare with next element after mid otherwise we will compair with elment before it  
            if nums[m]==nums[n]:
                l=m+1
            else:
                h=m
        return nums[l] 