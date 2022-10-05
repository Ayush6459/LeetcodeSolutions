''' 
given an array find the index of next smaller element to the right of each element 
if no such element exists, return len(nums) 

example:
I/p : [6,2,5,4,5,1,6]
o/p : [1,5,3,5,5,7,7]
'''



# solution

'''
        traverse the array from right to left
        let psuedo index = len(nums)
        conditions to check for:
        1. if the stack is empty : 
            add psuedo index to the result array
            push a pair of (element, index) to the stack
        2. if the top of the stack is smaller than the current element :
            push the index value of the top of the stack to the result array
            push current value , index to the stack
        3. if the top of the stack is greater than the current element :
            pop the top value of the stack from the stack till the value is smaller than the current element 
            or the stack is empty
            if the stack is empty :
                add pusedo index to result
                push the current value , index to stack
            else:
                push the top index of the top of the stack to the result array
                push current value,index to the stack
'''

from collections import deque

def nextSmallerRight(nums):
    stack = []
    res = []
    psuedoIndex = len(nums)
    
    for i in range(len(nums)-1,-1,-1):
        if not stack :
            res.append(psuedoIndex)
        elif stack[-1][0]<nums[i]:
            res.append(stack[-1][1])
        else:
            while stack and stack[-1][0]>=nums[i]:
                stack.pop()
            if not stack:
                res.append(psuedoIndex)
            else:
                res.append(stack[-1][1])
        stack.append([nums[i],i])

    return res[::-1]


arr = [2, 1, 5, 6, 2, 3]
print(nextSmallerRight(arr))    



# program to find next smaller to left
'''
I/p : [6,2,5,4,5,1,6]
o/p : [-1,-1,1,1,3,-1,5]
'''

# solution 

def nextSmallerLeft(nums):
    stack =[]
    res  = []
    psuedoIndex = -1
    for i in range(len(nums)):
        if not stack :
            res.append(psuedoIndex)
        elif stack[-1][0] <nums[i]:
            res.append(stack[-1][1])
        else:
            while stack and stack[-1][0]>=nums[i]:
                stack.pop()
            if not stack:
                res.append(psuedoIndex)
            else:
                res.append(stack[-1][1])
        stack.append([nums[i],i])
    
    return res

print(nextSmallerLeft(arr))