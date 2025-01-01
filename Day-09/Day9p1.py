with open("input.txt", "r") as file:
    disk_map = file.read().strip()

disk_segments = []
for i in range(0, len(disk_map), 2):
    file_length = int(disk_map[i])
    free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
    disk_segments.append(("file", file_length))
    if free_length > 0:
        disk_segments.append(("free", free_length))

blocks = []
file_id = 0
for segment, length in disk_segments:
    if segment == "file":
        blocks.extend([file_id] * length)
        file_id += 1
    else:
        blocks.extend(["."] * length)

left_walker, right_walker = 0, len(blocks) - 1
while left_walker < right_walker:
    while left_walker < len(blocks) and blocks[left_walker] != ".":
        left_walker += 1
    while right_walker >= 0 and blocks[right_walker] == ".":
        right_walker -= 1
    if left_walker < right_walker:
        blocks[left_walker], blocks[right_walker] = blocks[right_walker], blocks[left_walker]

checksum = 0
for i in range(len(blocks)):
    if blocks[i] != ".":
        checksum += i * blocks[i]

print(checksum)
