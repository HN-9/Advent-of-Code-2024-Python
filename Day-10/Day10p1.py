def read_map(file_path):
    with open(file_path, "r") as file:
        height_map = []
        for line in file:
            height_map.append(list(map(int, line.strip())))
    return height_map

def find_trailheads(height_map):
    trailheads = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if height_map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(height_map, x, y, current_height, visited):
    rows, cols = len(height_map), len(height_map[0])
    return (0 <= x < rows and 0 <= y < cols and
            (x, y) not in visited and
            height_map[x][y] == current_height + 1)

def dfs(height_map, x, y, visited): 
    stack = [(x, y, 0)]  
    reachable_nines = set()
    
    while stack:
        cx, cy, current_height = stack.pop()
        
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        
        if height_map[cx][cy] == 9:
            reachable_nines.add((cx, cy))
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            new_x, new_y = cx + dx, cy + dy
            if is_valid_move(height_map, new_x, new_y, current_height, visited):
                new_height = height_map[new_x][new_y]
                stack.append((new_x, new_y, new_height))
    
    return len(reachable_nines)

def calculate_trailhead_scores(height_map):
    trailheads = find_trailheads(height_map) 
    total_score = 0
    
    for trailhead in trailheads:
        visited = set()
        total_score += dfs(height_map, trailhead[0], trailhead[1], visited)
    
    return total_score

file_path = "Day-10-Challenge/input.txt"
height_map = read_map(file_path)
total_score = calculate_trailhead_scores(height_map)
print(total_score)


