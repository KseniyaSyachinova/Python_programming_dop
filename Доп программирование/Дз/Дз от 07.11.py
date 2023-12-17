# Алгоритм Дейкстры

import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 7, 'E': 2},
    'C': {'A': 3, 'F': 4},
    'D': {'B': 7},
    'E': {'B': 2, 'F': 1},
    'F': {'C': 4, 'E': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print(shortest_distances)

# Алгоритм Флойда-Уоршелла
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = {
    0: {1: 3, 2: 6},
    1: {0: 3, 2: 2},
    2: {0: 6, 1: 2}
}

shortest_paths = floyd_warshall(graph)
for row in shortest_paths:
    print(row)

# Алгоритм Тарьяна
class TarjanSCC:
    def __init__(self, graph):
        self.graph = graph
        self.index = 0
        self.stack = []
        self.ids = [-1] * len(graph)
        self.low = [float('inf')] * len(graph)
        self.on_stack = [False] * len(graph)
        self.scc_count = 0

    def find_scc(self):
        for i in range(len(self.graph)):
            if self.ids[i] == -1:
                self.dfs(i)

    def dfs(self, at):
        self.stack.append(at)
        self.on_stack[at] = True
        self.ids[at] = self.index
        self.low[at] = self.index
        self.index += 1

        for to in self.graph[at]:
            if self.ids[to] == -1:
                self.dfs(to)
            if self.on_stack[to]:
                self.low[at] = min(self.low[at], self.low[to])

        if self.low[at] == self.ids[at]:
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False
                self.low[node] = self.ids[at]
                if node == at:
                    break
            self.scc_count += 1

graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [3, 5],
    5: [5]
}

tarjan = TarjanSCC(graph)
tarjan.find_scc()
print(tarjan.scc_count)  # Количество компонент сильной связности