from itertools import permutations

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')

    for perm in permutations(vertices):
        current_path = 0
        k = start
        for node in perm:
            current_path += graph[k][node]
            k = node
        current_path += graph[k][start]
        min_path = min(min_path, current_path)
    return min_path

# Example Usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
print(tsp(graph, 'A'))
