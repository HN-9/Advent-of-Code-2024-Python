def read_map(file_path):
    with open(file_path, "r") as file:
        raw_lines = file.readlines()
    map_grid = []
    for line in raw_lines:
        map_grid.append(list(line.strip()))
    return map_grid


def simulate_guard(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in "^>v<":
                guard_position = (row, col)
                current_direction = "^>v<".index(grid[row][col])
                break

    visited_positions = set([guard_position])
    rows, cols = len(grid), len(grid[0])

    while True:
        row, col = guard_position
        dy, dx = directions[current_direction]
        next_position = (row + dy, col + dx)

        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            break

        if grid[next_position[0]][next_position[1]] == "#":
            current_direction = (current_direction + 1) % 4 
        else:
            guard_position = next_position  
            visited_positions.add(guard_position)

    return len(visited_positions)


file_path = "Day-6-Challenge/input.txt"
grid = read_map(file_path)
result = simulate_guard(grid)

print(result)
