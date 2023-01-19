class Solution:
    def getRow(self, numRows: int) -> List[int]:
        res = [1]
        for i in range(numRows):
            temp = [0] + res +[0]
            row = []
            for j in range(len(res)+1):
                row.append(temp[j]+temp[j+1])
              
            res= row
        
        return res