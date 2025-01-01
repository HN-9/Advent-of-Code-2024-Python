with open("input.txt", "r") as file:
    lines = file.read()

def parse_schematics(data):
    sections = data.split("\n\n")
    locks = []
    keys = []

    for section in sections:
        schematic = []
        for line in section.splitlines():
            schematic.append(line)
        if all(char == "#" for char in schematic[0]): 
            locks.append(schematic)
        elif all(char == "#" for char in schematic[-1]): 
            keys.append(schematic)

    return locks, keys

def schematic_to_heights(schematic, reverse=False):
    heights = []
    width = len(schematic[0])
    height = len(schematic)

    for col in range(width):
        count = 0
        for row in range(height):
            if not reverse:
                char = schematic[row][col]
            else:
                char = schematic[height - 1 - row][col]
            if char == "#":
                count += 1
            else:
                break
        heights.append(count)

    return heights

def count_fitting_pairs(lock_heights, key_heights, max_height):
    count = 0
    for lock in lock_heights:
        for key in key_heights:
            fit = True
            for i in range(len(lock)): 
                if lock[i] + key[i] > max_height:
                    fit = False
                    break

            if fit:
                count += 1

    return count


locks, keys = parse_schematics(lines)

lock_heights = []
for lock in locks:
    lock_heights.append(schematic_to_heights(lock))

key_heights = []
for key in keys:
    key_heights.append(schematic_to_heights(key, reverse=True)) 
max_height = len(locks[0])

result = count_fitting_pairs(lock_heights, key_heights, max_height)

print(result)
