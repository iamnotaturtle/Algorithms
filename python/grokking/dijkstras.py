# 3 hash tables: graph, costs, and parents
graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'fin': 1},
    'b': {'a': 3, 'b': 5},
    'fin': {}
}

infinity = float('inf')
costs = {
    'a': 6,
    'b': 2,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

processed = []

def findLowestCostNode(costs, processed):
    lowestCost = float('inf')
    lowestCostNode = None
    for node in costs:
        cost = costs[node]
        if cost < lowestCost and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

node = findLowestCostNode(costs, processed)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        newCost = cost + neighbors[n]
        if costs[n] > newCost:
            costs[n] = newCost
            parents[n] = node
    processed.append(node)
    node = findLowestCostNode(costs, processed)

def getShortestPath(parents):
    path = []
    cur = 'fin'
    while cur != 'start':
        path.append(cur)
        cur = parents[cur]
    path.append('start')

    return path

print('Found shortest path', list(reversed(getShortestPath(parents))))