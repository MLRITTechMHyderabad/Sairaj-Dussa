from collections import deque

def maze_path_finder(maze):
    if not maze or maze[0][0] == 1 or maze[-1][-1] == 1:
        return False, -1  # No path if start or end is blocked

    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(0, 0, 1)])  # (row, col, path length starting at 1)
    visited = set()
    visited.add((0, 0))  # Mark starting cell as visited

    while queue:
        r, c, path_length = queue.popleft()
        
        # Check if we reached the bottom-right corner
        if (r, c) == (rows - 1, cols - 1):
            return True, path_length  # Return success and shortest path length

        # Explore all valid neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, path_length + 1))
                visited.add((nr, nc))  # Mark cell as visited

    return False, -1  # If no path is found, return failure

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

path_exists, shortest_length = maze_path_finder(maze)
print("Is there a valid path?", path_exists)
print("Length of the shortest path:", shortest_length)
