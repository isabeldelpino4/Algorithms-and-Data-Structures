from collections import deque

# Graph definition
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Add a directed edge from u to v."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def add_undirected_edge(self, u, v):
        """Add an undirected edge (both directions)."""
        self.add_edge(u, v)
        self.add_edge(v, u)

    def bfs(self, start):
        """Breadth-First Search traversal."""
        visited = set()
        queue = deque([start])
        visited.add(start)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

  # algorithm Definion
  
    def dfs_recursive(self, start):
        """Recursive Depth-First Search."""
        visited = set()
        order = []

        def dfs(node):
            visited.add(node)
            order.append(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return order

    def dfs_iterative(self, start):
        """Iterative Depth-First Search using a stack."""
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                # add neighbors in reverse to mimic recursive order
                for neighbor in reversed(self.graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order


# DEMO
g = Graph()
g.add_undirected_edge(0, 1)
g.add_undirected_edge(0, 2)
g.add_undirected_edge(1, 3)
g.add_undirected_edge(1, 4)
g.add_undirected_edge(2, 5)
g.add_undirected_edge(2, 6)

print("BFS from node 0:", g.bfs(0))
print("DFS (recursive) from node 0:", g.dfs_recursive(0))
print("DFS (iterative) from node 0:", g.dfs_iterative(0))
