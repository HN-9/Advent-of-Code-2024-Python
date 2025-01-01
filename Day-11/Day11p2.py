from functools import cache

with open("input.txt", "r") as file:
    line = file.readline().strip()
stones = []
for number in line.split():
    stones.append(int(number))

@cache
def process_stone(value, remaining_blinks):
    if remaining_blinks == 0:  
        return 1
    if value == 0:
        return process_stone(1, remaining_blinks - 1)
    
    value_str = str(value)
    length = len(value_str)
    
    if length % 2 == 0: 
        midpoint = length // 2
        left_half = int(value_str[:midpoint])
        right_half = int(value_str[midpoint:])
        return process_stone(left_half, remaining_blinks - 1) + process_stone(right_half, remaining_blinks - 1)
    else: 
        new_value = value * 2024
        return process_stone(new_value, remaining_blinks - 1)


total_stones = 0
for stone in stones: 
    total_stones += process_stone(stone, 75)

print(total_stones)
