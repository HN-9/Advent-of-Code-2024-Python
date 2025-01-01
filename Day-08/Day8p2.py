from collections import defaultdict

with open("Day-8-Challenge/input.txt", "r") as file:
    lines = []
    for line in file:
        lines.append(line.strip())

valid_antenna_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

antennas = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in valid_antenna_chars:
            antennas.append((x, y, char))

frequency_map = defaultdict(list)
for x, y, freq in antennas:
    frequency_map[freq].append((x, y))

unique_antinodes = set() 
for freq, positions in frequency_map.items():
  
    if len(positions) < 2:
        continue

    n = len(positions)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            step_x = x2 - x1
            step_y = y2 - y1

            for direction in [-1, 1]:
                k = 1  
                while True:
                    new_x = x1 + direction * k * step_x
                    new_y = y1 + direction * k * step_y

                    if 0 <= new_x < len(lines[0]) and 0 <= new_y < len(lines):
                        unique_antinodes.add((new_x, new_y))
                        k += 1
                    else:
                        break  
for freq, positions in frequency_map.items():
    if len(positions) > 1:
        for x, y in positions:
            unique_antinodes.add((x, y))

print(len(unique_antinodes))

