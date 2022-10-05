'''
# problem link: "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
# Topic = "Kaden's Algo varient"
# Difficulty = "Easy"
# Is_Able_To_Solve_It = ""
# Is_Important = "Yes"
# Date_Solved = ""
# Need_Revision = "Yes"
# Editorial = "https://www.youtube.com/watch?v=XIWykOHE1SE"

'''
'''
Solution :- 
    Brute Force Approach :-

'''




def MaxProfit1(arr):
    # Brute Force Approach
    # Time Complexity : O(n^2)
    maxProfit=0
    for i in range(len(arr)-1):
        currMax = 0
        for j in range(i,len(arr)):
            currMax = max(currMax,arr[j]-arr[i])
        maxProfit = max(maxProfit,currMax)   

    return maxProfit

def MaxProfit2(arr):
    # Best Approach :
    '''
        Let's say arr = [7,1,5,3,6,4] 
        to find the max profit in one transaction we have to focus on selling of that stock which have 
        minimum value in the stocks seen previously and have max profit between all the possible transactions
        So  first we have to keep track of the minimum stock value seen till i'th index 
        second we have to keep a variable which store the max transaction value till i'th index
    '''
    maxprofit = 0 
    minPrice = arr[0]
    for i in range(1, len(arr)):
        minPrice = min(minPrice,arr[i])
        maxprofit = max(maxprofit, arr[i]-minPrice)

    return maxprofit

if __name__ == "__main__":
    arr = [7,6,4,3,1]

    print(MaxProfit1(arr))
    print(MaxProfit1([7,1,5,3,6,4]))
    print(MaxProfit2(arr))
    print(MaxProfit1([7,1,5,3,6,4]))