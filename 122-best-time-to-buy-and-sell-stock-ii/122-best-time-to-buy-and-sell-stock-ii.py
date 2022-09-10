class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        i =0 
        l = len(prices)
        while i<l:
            if (i+1<l ) and (prices[i]>prices[i+1]):
                while i<l:
                    if (i+1<l ) and (prices[i]>prices[i+1]):
                        i+=1
                    else:
                        break
            j = i+1
            while j<l:
                if (j+1<l ) and (prices[j]<prices[j+1]):
                    j+=1
                else:
                    break
            if j<l:
                profit = profit+prices[j]-prices[i]
            #print(profit)
            i = j+1
        return profit