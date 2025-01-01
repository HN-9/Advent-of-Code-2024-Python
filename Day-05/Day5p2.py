from collections import defaultdict, deque 
def parse(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()
    
    rules_part, updates_part = content.split("\n\n")
    
    rules = []
    for line in rules_part.splitlines():
        x, y = line.split("|")
        rules.append((int(x), int(y))) 
    updates = []
    update_lines = updates_part.splitlines()
    for line in update_lines:
        pages = line.split(",")
        updates.append([int(page) for page in pages])

    return rules, updates


def solve_part_two(rules, updates):
    def reorder_update(update, rules):
        
        graph = defaultdict(list)  
        in_degree = defaultdict(int)  
        pages_in_update = set(update) 
        for x, y in rules:
            if x in pages_in_update and y in pages_in_update:
                graph[x].append(y)
                in_degree[y] += 1
                in_degree[x] += 0  
        queue = deque()
        for node in update:
            if in_degree[node] == 0:
                queue.append(node)
        sorted_order = []

        while queue:
            current = queue.popleft() 
            sorted_order.append(current)
            for neighbor in graph[current]:  
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0: 
                  queue.append(neighbor)

        return sorted_order 
    incorrect_updates_middle_sum = 0

    for update in updates:
        is_valid = True

        for x, y in rules:
            if x in update and y in update and update.index(x) > update.index(y):
                is_valid = False
                break

        if not is_valid:
            reordered_update = reorder_update(update, rules)
            middle_index = len(reordered_update) // 2
            incorrect_updates_middle_sum += reordered_update[middle_index]

    return incorrect_updates_middle_sum



file_path = "Day-5-Challenge\input.txt"
rules, updates = parse(file_path)
result = solve_part_two(rules, updates)
print(result)

