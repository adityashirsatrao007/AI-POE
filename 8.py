import heapq

def a_star(graph, start, goal, heuristic_fn):
    open_list = [(0 + heuristic_fn(start), 0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current_g, current_node = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from.get(current_node)
            return path[::-1]
        for neighbor, weight in graph[current_node].items():
            tentative_g = current_g + weight
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g
                heapq.heappush(open_list, (tentative_g + heuristic_fn(neighbor), tentative_g, neighbor))

# Example Usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
heuristic_fn = lambda x: {'A': 7, 'B': 6, 'C': 2, 'D': 0}[x]
print(a_star(graph, 'A', 'D', heuristic_fn))
