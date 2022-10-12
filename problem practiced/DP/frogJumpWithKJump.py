def FrogJumpWithKJump(arr,k):
    dp = [-1]*len(arr)
    def MinSteps(index):
        if index == 0: 
            dp[0] = 0
            return 0
        if dp[index]!=-1:return dp[index]
        minSteps = float('inf')
        for j in range(1,k+1):
            if index-j >=0:
                jumps = MinSteps(index-j) + abs(arr[index]-arr[index-j])
                minSteps = min(minSteps,jumps)

        dp[index] = minSteps
        return minSteps

    return MinSteps(len(arr)-1)

if __name__ == '__main__':
    arr = [30,10,60,10,60,50]
    print(FrogJumpWithKJump(arr,5))


