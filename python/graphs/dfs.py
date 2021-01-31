from collections import defaultdict

# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, node, visited = set(), path = []):
        if node in visited:
            return

        # Do something with node as you traverse
        path.append(node)

        visited.add(node)
        
        for neighbor in self.graph[node]:
            self.dfs(neighbor, visited, path)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

path = []
g.dfs(0, set(), path)
assert(path == [0, 1, 2, 3])