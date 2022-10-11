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

if __name__ == '__main__':   
    arr = [30,10,60,10,60,50]
    print(frogJumpMin(arr))

