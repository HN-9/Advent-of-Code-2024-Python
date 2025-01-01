def read_map(file_path):
    with open(file_path, "r") as file:
        raw_lines = file.readlines()
    map_grid = []
    for line in raw_lines:
        map_grid.append(list(line.strip()))
    return map_grid


def simulate_guard_with_tracking(grid):
    
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

    return visited_positions


def causes_loop_with_obstruction(grid, obstruction_pos, start_pos, start_direction):
    """Simulates the guard"s movement with a new obstruction and checks if it causes a loop."""
  
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_now = start_direction
    guard_position = start_pos

    visited_with_direction = set() 
    visited_with_direction.add((guard_position, direction_now))

    rows, cols = len(grid), len(grid[0])

    
    if(grid[obstruction_pos[0]][obstruction_pos[1]] == "#"):
        return False

    
    grid[obstruction_pos[0]][obstruction_pos[1]] = "#"

    while True:
        y, x = guard_position
        dy, dx = directions[direction_now]
        next_position = (y + dy, x + dx)

        
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            grid[obstruction_pos[0]][obstruction_pos[1]] = "."  
            return False 

      
        if grid[next_position[0]][next_position[1]] == "#":
            direction_now = (direction_now + 1) % 4 
        else:
            guard_position = next_position  

        
        state = (guard_position, direction_now)
        if state in visited_with_direction:
            grid[obstruction_pos[0]][obstruction_pos[1]] = "."  
            return True

        visited_with_direction.add(state)


def find_all_loop_positions(grid, visited_positions):
    """Finds all positions where adding an obstruction causes the guard to get stuck in a loop."""


    
    guard_position = None
    guard_direction = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
          
            if cell in "^>v<":
                guard_position = (y, x)
                guard_direction = "^>v<".index(cell)  
                print(f"Guard found at ({y}, {x}) facing {"^>v<"[guard_direction]}")
                break
        if guard_position:
            break

   
    loop_positions = []

    
    for y, x in visited_positions:
    
        if (y, x) == guard_position:
            continue


        if causes_loop_with_obstruction(grid, (y, x), guard_position, guard_direction):
            loop_positions.append((y, x))

    return loop_positions


file_path = "Day-6-Challenge/input.txt"
grid = read_map(file_path)
visited_positions = simulate_guard_with_tracking(grid)
loop_positions = find_all_loop_positions(grid, visited_positions)

print(len(loop_positions))

