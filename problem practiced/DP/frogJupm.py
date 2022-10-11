
# mamoization method
def frogJumpMin(arr):
    n = len(arr)
    dp = [-1]*n
    def MinCostTillIthIndex(i):
        if dp[i] != -1:
            return dp[i]
        if i <= 0 : 
            dp[i] = 0
            return 0
        elif i == 1:
            dp[i] = MinCostTillIthIndex(i-1) + abs(arr[i]-arr[i-1])
            return dp[i]
        else:
            
            leftCall = MinCostTillIthIndex(i-1) + abs(arr[i]-arr[i-1])
            rightcall = MinCostTillIthIndex(i-2) + abs(arr[i]-arr[i-2])
            
            dp[i] = min(leftCall,rightcall)
            return dp[i]

    return MinCostTillIthIndex(n-1)

# tabulation Method 
'''
you can make a dp array and store the value of zero index as 0
proceed up in bottom up manner till last index 
return the last element value of dp array 
'''
def frogJumpTabulation(arr):
    n = len(arr)
    dp = [-1]*n
    dp[0] = 0
    dp[1] = abs(arr[1]-arr[0])
    for i in range(2,n):
        dp[i] = min((dp[i-1]+abs(arr[i]-arr[i-1])), (dp[i-2]+abs(arr[i]-arr[i-2])))
    return dp[-1]

def frogJumpSpaceOptimised(arr):
    n = len(arr)
    secondPrev = 0
    prev = 0
    for i in range(1,n):
        fs = prev + abs(arr[i]-arr[i-1])
        ss = float('inf')
        if i>1:
            ss = secondPrev+abs(arr[i]-arr[i-2])

        curr = min(fs,ss)
        secondPrev = prev
        prev = curr 

    return prev

    

if __name__ == '__main__':   
    arr = [30,10,60,10,60,50]
    #print(frogJumpMin(arr))
    #print(frogJumpTabulation(arr))
    print(frogJumpSpaceOptimised(arr))
