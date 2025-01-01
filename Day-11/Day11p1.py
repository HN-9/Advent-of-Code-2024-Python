with open("input.txt", "r") as file:
    line = file.readline().strip()
stones = []
for number in line.split():
    stones.append(int(number))

blinks = 75
for i in range(blinks):
    print(i)
    new_stones = []
    for stone in stones:
        if stone == 0: 
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0: 
            half_len = len(str(stone)) // 2
            left_half = int(str(stone)[:half_len])
            right_half = int(str(stone)[half_len:])
            new_stones.extend([left_half, right_half])
        else: 
            new_stones.append(stone * 2024) 
    stones = new_stones

print(len(stones))

