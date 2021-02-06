from collections import defaultdict

# 4.1
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # 4.1 Check if a path exists from node to target
    def findPathToNode(self, node, target, visited = set()):
        if node in visited:
            return False
        
        if node == target:
            return True
        
        visited.add(node)

        found = False
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                found = self.findPathToNode(neighbor, target, visited)

        return found

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4, 5)

assert(g.findPathToNode(0, 3) == True)
assert(g.findPathToNode(0, 5) == False)