# Imports
# problem link: "https://leetcode.com/problems/maximum-subarray/"
# Topic = "Kaden's Algo"
# Difficulty = "Easy"
# Is_Able_To_Solve_It = "Yes"
# Is_Important = "Yes"
# Date_Solved = ""
# Need_Revision = "Yes"
# Editorial = "https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1#"

'''Solution:
    Brute Forece Approach : 


    Best Approach :
        Initialize:
            max_so_far = INT_MIN
            max_ending_here = 0

        Loop for each element of the array
            (a) max_ending_here = max_ending_here + a[i]
            (b) if(max_so_far < max_ending_here)
                    max_so_far = max_ending_here
            (c) if(max_ending_here < 0)
                    max_ending_here = 0
        return max_so_far
    ''' 

def MaxSubArray(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1,len(arr)):
        max_ending_here = max(max_ending_here+arr[i],arr[i])
        max_so_far = max(max_ending_here,max_so_far)
    return max_so_far

if __name__ == "__main__":
    print(MaxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(MaxSubArray([1,2,3,-2,5]))