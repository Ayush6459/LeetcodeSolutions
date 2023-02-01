class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x = math.gcd(len(str1),len(str2))
        
        return str1[:x] if str1[:x]*(len(str1)//x) == str1 and str1[:x]*(len(str2)//x) == str2 else ""
            
                
            
            