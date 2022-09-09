class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        count = 0
        for i in range(len(rooms)):
            if i not in visited:
                
                if count >=1:
                    return False
                else:
                    count+=1
                    q = []
                    visited.add(i) 
                    q.append(i)
                    while q:
                        u = q.pop(0)
                        #print(u)
                        for v in rooms[u]:
                            if v not in visited:
                                visited.add(v)
                                q.append(v)
        return True 