class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        ans=maxi = 0
        for a,d in properties:
            if d<maxi:
                ans+=1
            maxi = max(maxi,d)
        return ans