from functools import cache
with open("Day-19-Challenge/input.txt", "r") as file: 
    lines = file.readlines()

towel_patterns = []
designs = []

split_index = lines.index("\n")
raw_patterns = lines[:split_index][0]
raw_pattern_list = raw_patterns.split(",")
towel_patterns = []
for pattern in raw_pattern_list:
    towel_patterns.append(pattern.strip())

raw_designs = lines[split_index+1:]
designs = []
for design in raw_designs:
    designs.append(design.strip())

@cache
def count_ways_to_construct_design(design):
    if not design:
        return 1

    total_ways = 0

    for pattern in towel_patterns:
        if design[:len(pattern)] == pattern:  
          total_ways += count_ways_to_construct_design(design[len(pattern):])
    
    return total_ways

total_ways_for_all_designs = 0
for design in designs:
    total_ways_for_all_designs += count_ways_to_construct_design(design)

print(total_ways_for_all_designs)
