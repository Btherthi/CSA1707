from collections import deque

# Goal state for the 8-puzzle
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Possible moves for the blank space (0)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def print_board(state):
    """Prints the board in a 3x3 grid format."""
    for i in range(0, 9, 3):
        print(state[i:i+3])

def get_neighbors(state):
    """Generates all possible states from the current state."""
    neighbors = []
    zero_pos = state.index(0)
    zero_row, zero_col = divmod(zero_pos, 3)

    for dr, dc in MOVES:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))
    return neighbors

def bfs(start_state):
    """Solves the 8-puzzle using BFS."""
    if start_state == GOAL_STATE:
        return []

    queue = deque([(start_state, [])])
    visited = set([start_state])

    while queue:
        current_state, path = queue.popleft()

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                if neighbor == GOAL_STATE:
                    return new_path
                queue.append((neighbor, new_path))
    return None

if __name__ == "__main__":
    # Input: Start state as a tuple
    start_state = tuple(map(int, input("Enter the start state (9 numbers, space-separated): ").split()))

    # Solve the puzzle
    solution = bfs(start_state)

    if solution:
        print("\nSolution found:")
        for step in solution:
            print_board(step)
            print()
    else:
        print("No solution found.")
