def iddfs(graph, start, goal, max_depth):
    def dls(node, depth):
        if depth == 0:
            return node == goal
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if dls(neighbor, depth - 1):
                    return True
        return False

    for depth in range(max_depth + 1):
        visited = set()
        if dls(start, depth):
            print(f"Found {goal} at depth {depth}")
            return True
    print(f"{goal} not found within depth {max_depth}")
    return False

# Example Usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
iddfs(graph, 'A', 'F', 3)
