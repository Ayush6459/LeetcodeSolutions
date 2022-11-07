class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        try :
            x = num.index('6')
            num[x] = '9'
            num = int(''.join(num))
            return num
        except:
            return int(''.join(num))
            
        