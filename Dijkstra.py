import heapq

# Define Graph Class first
class Graph:
    def __init__(self):
        # adjacency list: {node: [(neighbor, weight), ...]}
        self.graph = {}

    def add_edge(self, u, v, w, undirected=False):
        """Add a weighted edge u -> v with weight w.
           If undirected=True, also add v -> u."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, w))
        if undirected:
            self.graph[v].append((u, w))

  # Definition of Dijkstra's algorithm

    def dijkstra(self, start):
        """Return shortest distances from start to all other nodes."""
        # Initialize distances
        dist = {node: float("inf") for node in self.graph}
        dist[start] = 0

        # Min-heap priority queue
        pq = [(0, start)]  # (distance, node)

        while pq:
            current_dist, u = heapq.heappop(pq)

            # Skip if we already found a better path
            if current_dist > dist[u]:
                continue

            for v, weight in self.graph[u]:
                distance = current_dist + weight
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))

        return dist


# DEMO USE
g = Graph()
g.add_edge("A", "B", 4, undirected=True)
g.add_edge("A", "C", 2, undirected=True)
g.add_edge("B", "C", 5, undirected=True)
g.add_edge("B", "D", 10, undirected=True)
g.add_edge("C", "E", 3, undirected=True)
g.add_edge("E", "D", 4, undirected=True)
g.add_edge("D", "F", 11, undirected=True)

distances = g.dijkstra("A")
print("Shortest distances from A:", distances)
