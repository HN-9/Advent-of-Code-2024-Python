from collections import deque
with open("Day-18-Challenge/input.txt", "r") as file:
    lines = file.readlines()

def is_path_possible(grid, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        row, col = queue.popleft()
        if (row, col) == end:
            return True
        for dir_row, dir_col in directions:
            new_row, new_col = row + dir_row, col + dir_col
            if 0 <= new_row < 71 and 0 <= new_col < 71 and \
                grid[new_row][new_col] != '#' and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
    return False



bytes_to_fall = []
for line in lines:
    coords = line.strip().split(',')
    x = int(coords[0])
    y = int(coords[1])
    bytes_to_fall.append((x, y))

final_grid = [['.' for _ in range(70 + 1)] for _ in range(70 + 1)]
start = (0, 0) 
end = (70, 70)

low = 0
high = len(bytes_to_fall) - 1
blocking_index = -1

while low <= high:
    mid = (low + high) // 2

    final_grid = [['.' for _ in range(70 + 1)] for _ in range(70 + 1)]


    for i in range(mid + 1):
        x, y = bytes_to_fall[i]
        final_grid[y][x] = '#'

    if is_path_possible(final_grid, start, end):
        low = mid + 1  
    else:
        blocking_index = mid
        high = mid - 1  

if blocking_index != -1:
    x, y = bytes_to_fall[blocking_index]
    print(f"{x},{y}")

