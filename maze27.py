import timeit   # library to calculate the time

# Generate maze (0: empty, 1: wall)
maze_map = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],    
    [0, 0, 0, 0, 0]
]

# 'Print maze' function
def print_maze(maze_map):
    for row in maze_map:
        print(row)

def dfs(maze_map, cur_r, cur_c, R, C):
    if cur_r == R - 1 and cur_c == C - 1:
        return True  # Can find the target

    for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr, nc = cur_r + dr, cur_c + dc
        if 0 <= nr < R and 0 <= nc < C and maze_map[nr][nc] == 0:
            maze_map[nr][nc] = 9  # check visit
            if dfs(maze_map, nr, nc, R, C):
                return True

    return False  # Can't find the target


R = len(maze_map)
C = len(maze_map[0])

if dfs(maze_map, 0, 0, R, C):
    print("Success.")
else:
    print("failure.")

# Disply maze checked visit with 9
print("Maze:")
print_maze(maze_map)

# Calculate time
exec_time = timeit.timeit(lambda: dfs(maze_map, 0, 0, R, C), number=1) * 1e6

# display
print(f"Time: {exec_time:.2f} microsec")