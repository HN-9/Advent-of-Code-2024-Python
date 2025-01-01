from collections import deque
with open("Day-18-Challenge/input.txt", "r") as file:
    lines = file.readlines()

final_grid = [['.' for _ in range(70 + 1)] for _ in range(70 + 1)]


for i in range(1024):
    coords = lines[i].strip().split(',')
    x = int(coords[0])
    y = int(coords[1])
    final_grid[y][x] = '#'


start = (0, 0) 
end = (70, 70)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
dist = [[-1] * (70 + 1) for _ in range(70 + 1)]
dist[start[0]][start[1]] = 0
queue = deque([start])

while queue:
    row, col = queue.popleft()
    if (row, col) == end:
        print(dist[row][col])
        break
    for dir_row, dir_col in directions:
        new_row, new_col = row + dir_row, col + dir_col
        if 0 <= new_row < 71 and 0 <= new_col < 71 and \
            final_grid[new_row][new_col] != '#' and dist[new_row][new_col] == -1: 
            dist[new_row][new_col] = dist[row][col] + 1
            queue.append((new_row, new_col))

