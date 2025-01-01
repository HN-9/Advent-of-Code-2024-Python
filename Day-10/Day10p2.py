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

def dfs_count_trails(height_map, x, y, visited): 
    rows, cols = len(height_map), len(height_map[0])
    
    if height_map[x][y] == 9:
        return 1
    
    visited.add((x, y))
    total_trails = 0
    current_height = height_map[x][y]
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < rows and 0 <= new_y < cols and
                (new_x, new_y) not in visited and
                height_map[new_x][new_y] == current_height + 1):
            total_trails += dfs_count_trails(height_map, new_x, new_y, visited.copy())
    
    return total_trails

def calculate_trailhead_ratings(height_map):
    trailheads = find_trailheads(height_map) 
    total_rating = 0
    
    for trailhead in trailheads:
        visited = set()
        total_rating += dfs_count_trails(height_map, trailhead[0], trailhead[1], visited)
    
    return total_rating

file_path = "Day-10-Challenge/input.txt"
height_map = read_map(file_path)
total_rating = calculate_trailhead_ratings(height_map)
print(total_rating)

