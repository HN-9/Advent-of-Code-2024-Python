with open("Day-15-Challenge/input.txt", "r") as file:
    lines = file.readlines()
final_grid = [["."]*(50) for _ in range(len(lines[0]) - 1)]



def find_soulmate(final_grid, check_row,check_col):
    check = final_grid[check_row][check_col]
    if check == "[":
        return check_row,check_col+1
    if check == "]":
        return check_row,check_col-1

def collect_boxes_and_validate(final_grid, start_row, start_col, go_row, go_col):
    """ Collect all connected boxes and validate movement. """
    boxes_to_move = []  
  queue = [(start_row, start_col)]

    while queue:
        current_row, current_col = queue.pop(0)

        if (current_row, current_col) not in boxes_to_move:
            boxes_to_move.append((current_row, current_col))
            soulmate = find_soulmate(final_grid, current_row, current_col)
            queue.append(soulmate) 
            if soulmate and soulmate not in boxes_to_move:
                boxes_to_move.append(soulmate)

        next_row = current_row + go_row
        next_col = current_col + go_col
        if 0 <= next_row < len(final_grid) and 0 <= next_col < len(final_grid[0]):
            if final_grid[next_row][next_col] in ["[", "]"] and (next_row, next_col) not in boxes_to_move:
                queue.append((next_row, next_col))
            elif final_grid[next_row][next_col] == "#":  
                return None

    

    return boxes_to_move


def move_from_to(from_row, from_col, go_row, go_col, final_grid):
    """ Move the robot and boxes in the specified direction. """
    next_row = from_row + go_row
    next_col = from_col + go_col

      if final_grid[next_row][next_col] == ".":
        final_grid[from_row][from_col] = "."
        final_grid[next_row][next_col] = "@"
        return True

    if go_row == 0 and go_col == -1: 
        if final_grid[from_row+go_row][from_col+go_col] == "]": 
            Box_riginal = [[go_row,go_col]]
            while True:
                go_col -= 1
                Box_riginal.append([go_row,go_col])
                
                if final_grid[from_row+go_row][from_col+go_col] == "#":
                    return False 
                if final_grid[from_row+go_row][from_col+go_col] == ".":
                    final_grid[from_row][from_col] = "." 
                  for i in range(len(Box_riginal)-1,0,-1): 
                        final_grid[from_row+Box_riginal[i][0]][from_col+Box_riginal[i][1]] = final_grid[from_row+Box_riginal[i-1][0]][from_col+Box_riginal[i-1][1]]
                    final_grid[from_row+Box_riginal[0][0]][from_col+Box_riginal[0][1]] = "@"
                    
                    return True

    if go_row == 0 and go_col == 1:  
        if final_grid[from_row + go_row][from_col + go_col] == "[":  
            Box_riginal = [[go_row, go_col]]  
            while True:
                go_col += 1  
                Box_riginal.append([go_row, go_col])  
                if final_grid[from_row + go_row][from_col + go_col] == "#":
                    return False  
                if final_grid[from_row + go_row][from_col + go_col] == ".":
                    final_grid[from_row][from_col] = "."  
                    for i in range(len(Box_riginal) - 1, 0, -1):
                        final_grid[from_row + Box_riginal[i][0]][from_col + Box_riginal[i][1]] = \
                            final_grid[from_row + Box_riginal[i - 1][0]][from_col + Box_riginal[i - 1][1]]

                    final_grid[from_row + Box_riginal[0][0]][from_col + Box_riginal[0][1]] = "@"
                    return True

    if final_grid[next_row][next_col] in ["[", "]"]:
        
        boxes = collect_boxes_and_validate(final_grid, next_row, next_col, go_row, go_col)
        if not boxes:  
            return False
        boxes = sorted(boxes, reverse=(go_row == 1)) 
        for row, col in boxes:
            next_row = row + go_row
            next_col = col + go_col
            final_grid[next_row][next_col] = final_grid[row][col]  
            final_grid[row][col] = "."  
          final_grid[from_row][from_col] = "."
        final_grid[from_row + go_row][from_col + go_col] = "@"

        return True

    return False


moves = []
row = 0
for line in lines: 
    if "#" in line:
        line = line.split("\n")[0]
        col = 0
        for i in line:
            final_grid[row][col] = i
            col += 1
        row += 1
    else:
        line = line.split("\n")[0]
        for i in line:
            moves.append(i)

temp_grid = [["."]*(100) for _ in range(len(lines[0]) - 1)]
for row in range(len(final_grid)):
    for col in range(len(final_grid[0])):
        if final_grid[row][col] == "#":
            temp_grid[row][2 * col - 1] = "#"
            temp_grid[row][2 * col    ] = "#"
        if final_grid[row][col] == "O":
            temp_grid[row][2 * col - 1] = "["
            temp_grid[row][2 * col    ] = "]"
        if final_grid[row][col] == ".":
            temp_grid[row][2 * col - 1] = "."
            temp_grid[row][2 * col    ] = "."
        if final_grid[row][col] == "@":
            temp_grid[row][2 * col - 1] = "@"
            temp_grid[row][2 * col    ] = "."
final_grid = temp_grid

def findRobotCoords(final_grid):
    for row in range(len(final_grid)):
        for col in range(len(final_grid[0])):
            if final_grid[row][col] == "@":
                return row,col

def boxPoints(final_grid):
    total = 0
    for row in range(len(final_grid)):
        for col in range(len(final_grid[0])):
            if final_grid[row][col] == "]":
                total += row * 100 + col
    return total
    
                


for move in moves:
    robot_row,robot_col = findRobotCoords(final_grid)
    if move == "<":
        move_from_to(robot_row,robot_col,0,-1,final_grid)
        continue
    if move == ">":
        move_from_to(robot_row,robot_col,0,1,final_grid)
        continue

    if move == "^":
        move_from_to(robot_row,robot_col,-1,0,final_grid)
        continue

    if move == "v":
        move_from_to(robot_row,robot_col,1,0,final_grid)
        continue
    
print("Box points", boxPoints(final_grid))

