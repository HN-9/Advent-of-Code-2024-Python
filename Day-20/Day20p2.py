from collections import deque
with open("input.txt", "r") as file:  
    lines = file.readlines()

grid = []
for line in lines:
    grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "S":
            start = (row, col)
            break
    else:
        continue
    break

dist = [[-1] * cols for _ in range(rows)]
dist[start[0]][start[1]] = 0
queue = deque([start])

while queue:
    row, col = queue.popleft()
    if grid[row][col] == "E":
        break
    for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]: 
        if 0 <= new_row < rows and 0 <= new_col < cols \
        and grid[new_row][new_col] != "#" \
        and dist[new_row][new_col] == -1: 
            dist[new_row][new_col] = dist[row][col] + 1
            queue.append((new_row, new_col))


def count_cheats_part2(grid, dist):
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#": 
                continue
            for radius in range(2, 21): 
                for dir_row in range(radius + 1): 
                    dir_col = radius - dir_row 
                    for new_row, new_col in {
                        (row + dir_row, col + dir_col), # I
                        (row + dir_row, col - dir_col),
                        (row - dir_row, col + dir_col),
                        (row - dir_row, col - dir_col),
                    }:  
                        if 0 <= new_row < rows and 0 <= new_col < cols \
                        and grid[new_row][new_col] != "#":  
                            if dist[row][col] - dist[new_row][new_col] >= 100 + radius:  
                                count += 1
    return count

possible_cheats = count_cheats_part2(grid, dist)
print(possible_cheats)

