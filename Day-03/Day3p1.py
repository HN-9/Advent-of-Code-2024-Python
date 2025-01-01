import re

with open("input.txt", "r") as file:
    corrupted_memory = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)" 

matches = re.findall(pattern,corrupted_memory)

result_sum = 0
for x,y in matches:
    result_sum += int(x) * int(y)
print(result_sum)
