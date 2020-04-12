
// graph: each node has array of children
export const breadthFirstSearch = (graph, source) => {
  if (Object.keys(graph).length === 0) {
    return [];
  }
  let queue = [];
  queue.push(source);
  let visited = new Set(queue);

  while (queue.length) {
    const node = queue.shift();
    visited.add(node);
    graph[node].forEach(neighbor => {
      if (visited.has(neighbor)) {
        return;
      }
      queue.push(neighbor);
    });
  }
  return Array.from(visited);
};