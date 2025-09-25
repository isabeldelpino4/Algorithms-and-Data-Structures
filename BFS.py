from collections import deque

class Graph:
    def __init__(self):
        # adjacency list stored as dict: {node: [neighbors]}
        self.graph = {}

    def add_edge(self, u, v):
        """Add an edge from u to v (directed graph)"""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def add_undirected_edge(self, u, v):
        """Add an undirected edge (both directions)"""
        self.add_edge(u, v)
        self.add_edge(v, u)

    def bfs(self, start):
        """Perform BFS traversal from a starting node"""
        visited = set()
        queue = deque([start])
        visited.add(start)

        order = []  # to store traversal order

        while queue:
            node = queue.popleft()
            order.append(node)

            # Visit all neighbors
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order


# DEMO
g = Graph()
g.add_undirected_edge(0, 1)
g.add_undirected_edge(0, 2)
g.add_undirected_edge(1, 3)
g.add_undirected_edge(1, 4)
g.add_undirected_edge(2, 5)
g.add_undire_
