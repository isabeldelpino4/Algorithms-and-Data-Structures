class Graph:
    def __init__(self):
        # store edges as list of tuples (u, v, w)
        self.edges = []
        self.nodes = set()

    def add_edge(self, u, v, w):
        """Add a directed weighted edge u -> v with weight w."""
        self.edges.append((u, v, w))
        self.nodes.add(u)
        self.nodes.add(v)

    def bellman_ford(self, start):
        """Compute shortest paths from start node.
        Returns (dist, negative_cycle) where:
        - dist is a dict of shortest distances
        - negative_cycle is True if one was detected
        """
        # Step 1: initialize distances
        dist = {node: float("inf") for node in self.nodes}
        dist[start] = 0

        # Step 2: relax edges repeatedly (|V|-1 times)
        for _ in range(len(self.nodes) - 1):
            updated = False
            for u, v, w in self.edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break  # early exit if no updates

        # Step 3: check for negative-weight cycles
        for u, v, w in self.edges:
            if dist[u] + w < dist[v]:
                return dist, True  # negative cycle found

        return dist, False


# DEMO
g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("B", "C", -1)
g.add_edge("B", "D", 2)
g.add_edge("C", "D", 3)
g.add_edge("D", "B", 1)  

distances, has_neg_cycle = g.bellman_ford("A")

print("Shortest distances from A:", distances)
print("Negative cycle detected?", has_neg_cycle)
