from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, node):
        path = []
        q = [node]
        visited = {node}

        while q:
            cur = q.pop(0)
            path.append(cur)
            for neighbor in self.graph[cur]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)

        return path

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.bfs(2))
assert(g.bfs(2) == [2, 0, 3, 1])