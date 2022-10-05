from collections import deque


# A class to represent a graph object
class Graph:

    # Constructor
    def __init__(self, edges=None, n=0):

        # Total number of nodes in the graph
        self.n = n

        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the undirected graph
        for (src, dest) in edges:

            # add an edge from source to destination
            self.adjList[src].append(dest)

            # add an edge from destination to source
            self.adjList[dest].append(src)


# Perform BFS on a graph starting from vertex `v`
def isBipartite(graph):

    # start from any node as the graph is connected and undirected
    v = 0

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * graph.n

    # stores the level of each vertex in BFS
    level = [None] * graph.n

    # mark the source vertex as discovered and set its level to 0
    discovered[v] = True
    level[v] = 0

    # create a queue to do BFS and enqueue source vertex
    q = deque()
    q.append(v)

    # loop till queue is empty
    while q:

        # dequeue front node and print it
        v = q.popleft()

        # do for every edge (v, u)
        for u in graph.adjList[v]:
            # if vertex `u` is explored for the first time
            if not discovered[u]:
                # mark it as discovered
                discovered[u] = True

                # set level one more than the level of the parent node
                level[u] = level[v] + 1

                # enqueue vertex
                q.append(u)

            # if the vertex has already been discovered and the
            # level of vertex `u` and `v` are the same, then the
            # graph contains an odd-cycle and is not bipartite
            elif level[v] == level[u]:
                return False

    return True


if __name__ == '__main__':

    # List of graph edges
    # Note that if we add edge (1, 3), the graph becomes non-bipartite
    edges = [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]

    # total number of nodes in the graph (0 to 8)
    n = 9

    # build a graph from the given edges
    graph = Graph(edges, n)

    if isBipartite(graph):
        print('Graph is bipartite')
    else:
        print('Graph is not bipartite')
