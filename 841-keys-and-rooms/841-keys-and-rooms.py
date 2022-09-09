class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        q = [0]
        while q:
            u = q.pop(0)
            for v in rooms[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return len(visited)==len(rooms)