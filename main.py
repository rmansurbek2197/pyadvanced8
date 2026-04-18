import heapq

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w):
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, []).append((u, w))

    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                for n, _ in self.adj.get(node, []):
                    queue.append(n)
        return order

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for n, _ in self.adj.get(node, []):
                    stack.append(n)
        return order

    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.adj}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neigh, w in self.adj[node]:
                nd = d + w
                if nd < dist[neigh]:
                    dist[neigh] = nd
                    heapq.heappush(pq, (nd, neigh))
        return dist

g = Graph()
g.add_edge("A","B",1)
g.add_edge("A","C",4)
g.add_edge("B","C",2)
g.add_edge("C","D",1)

print(g.bfs("A"))
print(g.dfs("A"))
print(g.dijkstra("A"))
