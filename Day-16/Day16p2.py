with open("Day-16-Challenge/input.txt", "r") as file:
    lines = file.readlines()
final_grid = [[""]*(len(lines)) for _ in range(len(lines[0]) - 1)]

moves = []
row = 0
for line in lines: 
    if "#" in line[0]:
        line = line.split("\n")[0]
        col = 0
        for i in line:
            final_grid[row][col] = i
            col += 1
        row += 1
    
start = None
end = None
for row in range(len(final_grid)):
    for col in range(len(final_grid[0])):
        if final_grid[row][col] == 'S':
            start = (row, col)
        elif final_grid[row][col] == 'E':
            end = (row, col)

import heapq 
directions = [(-1,0),(0,1),(1,0),(0,-1)]
start_state = (start[0], start[1], 1)  
previous_states = {}

distances = {}
distances[start_state] = 0
priority_queue = [(0, start_state)]
previous_states[start_state] = [] 

while priority_queue:
    current_cost, (row, col, dir) = heapq.heappop(priority_queue)
    if distances[(row, col, dir)] < current_cost:
        continue
    new_row, new_col = row + directions[dir][0], col + directions[dir][1]
    if 0 <= new_row < len(final_grid) and 0 <= new_col < len(final_grid[0]) and final_grid[new_row][new_col] != '#':
        new_cost = current_cost + 1
        new_state = (new_row, new_col, dir)
        if new_state not in distances or new_cost < distances[new_state]:
            distances[new_state] = new_cost
            heapq.heappush(priority_queue, (new_cost, new_state))
            previous_states[new_state] = [(row, col, dir)]
        elif new_cost == distances[new_state]:
            previous_states[new_state].append((row, col, dir))
    new_dir = (dir - 1) % 4
    new_cost = current_cost + 1000
    new_state = (row, col, new_dir)
    if new_state not in distances or new_cost < distances[new_state]:
        distances[new_state] = new_cost
        heapq.heappush(priority_queue, (new_cost, new_state))
        previous_states[new_state] = [(row, col, dir)]
    elif new_cost == distances[new_state]:
        previous_states[new_state].append((row, col, dir)
    new_dir = (dir + 1) % 4
    new_cost = current_cost + 1000
    new_state = (row, col, new_dir)
    if new_state not in distances or new_cost < distances[new_state]:
        distances[new_state] = new_cost
        heapq.heappush(priority_queue, (new_cost, new_state))
        previous_states[new_state] = [(row, col, dir)]
    elif new_cost == distances[new_state]:
        previous_states[new_state].append((row, col, dir))

end_states = []
for state in distances:
    row, col, _ = state
    if (row, col) == end:
        end_states.append(state)
tiles_in_best_paths = set()

def backtrack(state):
    row, col, _ = state
    tiles_in_best_paths.add((row, col))
    for parent in previous_states.get(state, []): 
        backtrack(parent)

for end_state in end_states:
    backtrack(end_state)

best_path_count = len(tiles_in_best_paths)

print(best_path_count)
