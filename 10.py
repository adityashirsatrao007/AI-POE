def map_coloring(graph, colors):
    def is_valid(node, color):
        for neighbor in graph[node]:
            if color_assignment[neighbor] == color:
                return False
        return True

    def solve(node):
        if node == len(graph):
            return True
        for color in colors:
            if is_valid(nodes[node], color):
                color_assignment[nodes[node]] = color
                if solve(node + 1):
                    return True
                color_assignment[nodes[node]] = None
        return False

    nodes = list(graph.keys())
    color_assignment = {node: None for node in nodes}
    if solve(0):
        return color_assignment
    return None

# Example Usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
print(map_coloring(graph, colors))
