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


def solve(rules, updates):
    total = 0

    for update in updates:
        page_indices = {}
        index = 0
        for page in update:
            page_indices[page] = index
            index += 1

        
        is_valid = True

        for x, y in rules:
            if x in page_indices and y in page_indices: 
                if page_indices[x] > page_indices[y]: 
                    is_valid = False
                    break

        if is_valid:
            middle_page = len(update) // 2 
            total += update[middle_page]

    return total



file_path = "input.txt"
rules, updates = parse(file_path)
result = solve(rules, updates)
print(result)
