from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def adjacency_matrix(self):
        vertices = sorted(self.graph.keys())
        n = len(vertices)
        matrix = [[0] * n for _ in range(n)]
        vertex_to_index = {v: i for i, v in enumerate(vertices)}

        for u in vertices:
            for v in self.graph[u]:
                i, j = vertex_to_index[u], vertex_to_index[v]
                matrix[i][j] = 1

        return matrix, vertices


    # BFS
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    # DFS
    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(node):
            visited.add(node)
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    def shortest_path(self, start, end):
        if start == end:
            return [start]

        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)

        while queue:
            node, path = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []  


if __name__ == "__main__":
    g = Graph(directed=False)
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    for u, v in edges:
        g.add_edge(u, v)

    print("Список смежности:")
    for node in sorted(g.graph.keys()):
        print(f"{node}: {g.graph[node]}")

    matrix, vertices = g.adjacency_matrix()
    print("\nМатрица смежности:")
    print("   ", "  ".join(map(str, vertices)))
    for i, row in enumerate(matrix):
        print(f"{vertices[i]}: {'  '.join(map(str, row))}")

    print("\nBFS из 0:", g.bfs(0))
    print("DFS из 0:", g.dfs(0))
    print("Кратчайший путь от 0 до 4:", g.shortest_path(0, 4))