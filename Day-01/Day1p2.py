left_list = [] 
right_list = []

with open("input.txt", "r") as file: 
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

right_count = {} 
for num in right_list: 
    if num in right_count:
        right_count[num] += 1
    else:
        right_count[num] = 1
similarity_score = 0

for num in left_list:
    if num in right_count:
        similarity_score += num * right_count[num]

print(similarity_score)
