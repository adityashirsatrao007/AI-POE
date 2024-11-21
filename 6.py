import heapq

def best_first_search(initial_state, goal_state, heuristic_fn):
    open_list = [(heuristic_fn(initial_state), initial_state)]
    visited = set()

    while open_list:
        _, current_state = heapq.heappop(open_list)
        if current_state == goal_state:
            print("Goal reached:", current_state)
            return
        visited.add(tuple(current_state))
        for neighbor in generate_neighbors(current_state):
            if tuple(neighbor) not in visited:
                heapq.heappush(open_list, (heuristic_fn(neighbor), neighbor))

def generate_neighbors(state):
    # Define logic for neighbor generation
    pass

def heuristic_fn(state):
    # Define logic for heuristic calculation
    return 0

# Example Usage
initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
best_first_search(initial_state, goal_state, heuristic_fn)
