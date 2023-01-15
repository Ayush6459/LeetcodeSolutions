class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        reqired = collections.Counter('balloon')
        freq = collections.Counter(text)
        instance = float('inf')
        for i in reqired:
            if i not in freq:
                return 0
            else:
                instance = min(instance,freq[i]//reqired[i])
        
        return instance