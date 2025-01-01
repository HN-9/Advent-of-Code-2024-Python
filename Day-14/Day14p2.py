with open("input.txt", "r") as file:
    lines = file.readlines()

WIDE = 101
TALL = 103

robots = []
for robot in lines: 
    sides = robot.split(" ")
    left_side = sides[0]
    right_side = sides[1]
    left_sides = left_side.split(",")
    Px = left_sides[0].split("=")[-1]
    Py = left_sides[1]
    right_sides = right_side.split(",")
    Vx = right_sides[0].split("=")[-1]
    Vy = right_sides[1].strip()
    Px = int(Px)
    Py = int(Py)
    Vx = int(Vx)
    Vy = int(Vy)
    robots.append([Px,Py,Vx,Vy])

smallest_answer = 999999999999
found_at_second = 0
for second in range(WIDE * TALL): 
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    final_grid = [[0]*WIDE for _ in range(TALL)]
    for i in range(len(robots)):
        Px,Py,Vx,Vy = robots[i]
        new_Py, new_Px = (Px + Vx * second),(Py + Vy * second) 
        new_Px, new_Py = (new_Px % TALL), (new_Py % WIDE)
        final_grid[new_Px][new_Py] += 1 
        vertical_middle = WIDE // 2
        horizontal_middle = TALL // 2


        if new_Px < vertical_middle and new_Py < horizontal_middle:
            q1 += 1
        if new_Px > vertical_middle and new_Py < horizontal_middle:
            q2 += 1
        if new_Px < vertical_middle and new_Py > horizontal_middle:
            q3 += 1
        if new_Px > vertical_middle and new_Py > horizontal_middle:
            q4 += 1

    answer = q1 * q2 * q3 * q4 
    if(answer < smallest_answer): 
        smallest_answer = answer
        found_at_second = second

    
print("Found smallest safety factor: ", smallest_answer)
print("at second: ", found_at_second)
