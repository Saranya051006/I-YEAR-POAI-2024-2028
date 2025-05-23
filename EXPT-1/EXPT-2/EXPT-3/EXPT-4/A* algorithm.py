import heapq

class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(start, goal, heuristic, get_neighbors):
    open_list = []
    heapq.heappush(open_list, Node(start, None, 0, heuristic(start, goal)))
    closed_set = set()
    state_g_cost = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)

        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]

        closed_set.add(current.state)

        for neighbor, cost in get_neighbors(current.state):
            if neighbor in closed_set:
                continue

            tentative_g = current.g + cost

            if neighbor not in state_g_cost or tentative_g < state_g_cost[neighbor]:
                state_g_cost[neighbor] = tentative_g
                h = heuristic(neighbor, goal)
                heapq.heappush(open_list, Node(neighbor, current, tentative_g, h))

    return None

# Heuristic: Manhattan distance
def heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

# Neighbors: 4-directional movement
def get_neighbors(state):
    x, y = state
    return [((x + dx, y + dy), 1) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

# Example usage
start = (0, 0)
goal = (3, 3)

path = a_star_search(start, goal, heuristic, get_neighbors)
print("Path from start to goal:", path)
