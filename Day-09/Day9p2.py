with open("Day-9-Challenge/input.txt", "r") as file:
    disk_map = file.read().strip()

disk_segments = []
for i in range(0, len(disk_map), 2):
    file_length = int(disk_map[i])
    free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
    disk_segments.append(("file", file_length))
    if free_length > 0:
        disk_segments.append(("free", free_length))

blocks = []
file_positions = [] 
file_id = 0
pos = 0
for segment, length in disk_segments:
    if segment == "file":
        blocks.extend([file_id] * length)
        file_positions.append((pos, length, file_id))
        pos += length
        file_id += 1
    else:
        blocks.extend([None] * length)
        pos += length

free_spaces = []
current_pos = 0
while current_pos < len(blocks):
    if blocks[current_pos] is None:
        start = current_pos
        while current_pos < len(blocks) and blocks[current_pos] is None:
            current_pos += 1
        free_spaces.append((start, current_pos - start))
    current_pos += 1

file_count = len(file_positions)
space_count = len(free_spaces)
for file_index in range((file_count - 1), -1, -1):  
    start_pos, file_size, file_id = file_positions[file_index]
    for space_index in range(space_count):  
        space_pos, space_size = free_spaces[space_index]
        if space_pos < start_pos and file_size <= space_size:
            for j in range(file_size):
                blocks[start_pos + j] = None
                blocks[space_pos + j] = file_id
            free_spaces[space_index] = (space_pos + file_size, space_size - file_size)
            break


checksum = 0
for i, block in enumerate(blocks):
    if block is not None:
        checksum += i * block

print(checksum)
