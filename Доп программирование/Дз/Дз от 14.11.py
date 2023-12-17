# Алгоритм Флёри
class FleuryGraph:
    def __init__(self, graph):
        self.graph = graph

    def find_eulerian_path(self):
        edges_count = sum(len(edges) for edges in self.graph.values())
        if edges_count % 2 != 0:
            return "Граф не содержит эйлерова пути или цикла"

        current_vertex = next(iter(self.graph))
        path = []
        stack = [current_vertex]

        while stack:
            if self.graph[current_vertex]:
                stack.append(current_vertex)
                next_vertex = self.graph[current_vertex].pop()
                del self.graph[next_vertex][self.graph[next_vertex].index(current_vertex)]
                current_vertex = next_vertex
            else:
                path.append(current_vertex)
                current_vertex = stack.pop()

        return path


graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

fleury = FleuryGraph(graph)
eulerian_path = fleury.find_eulerian_path()
print(eulerian_path)  # Эйлеров путь или цикл в графе

# Алгоритм поиска Эйлерова цикла на основе объединения простых циклов

def find_eulerian_cycle(graph):
    def dfs(v, cycle):
        while graph[v]:
            dfs(graph[v].pop(), cycle)
        cycle.append(v)

    cycle = []
    start_vertex = list(graph.keys())[0]
    dfs(start_vertex, cycle)
    return cycle[::-1]


graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]
}

eulerian_cycle = find_eulerian_cycle(graph)
print(eulerian_cycle)

# Алгортим Косарайю
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):
        stack = []
        visited = [False] * (self.V)

        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        gr = self.transpose()

        visited = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.dfs(i, visited, [])
                print(visited)


g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Сильно связные компоненты:")
g.print_scc()
