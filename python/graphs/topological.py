from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add
    
    def topological(self, node, visited = set(), path = []):
        if node in visited:
            return
        
        visited.add(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.topological(neighbor, visited, path)
        
        path.append(node)
    def top(self):
        visited = set()
        path = []

        vertices = len(self.graph.keys())
        print(vertices)
        for i in range(vertices + 1):
            self.topological(i, visited, path)
        
        path.reverse()
        return path
        
g = Graph() 
g.addEdge(0, 2) 
g.addEdge(0, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(5, 3)
g.addEdge(5, 6)
g.addEdge(4, 6)


path = g.top()

print(path)