class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        V= len(rooms)
        visited = [0]*V
        count = 0
        for i in range(V):
            if visited[i]==0:
                if count >=1:
                    return False
                else:
                    count+=1
                    q = []
                    visited[i]=1 
                    q.append(i)
                    while q:
                        u = q.pop(0)
                        #print(u)
                        for v in rooms[u]:
                            if visited[v]==0:
                                visited[v]=1
                                q.append(v)
        return True 