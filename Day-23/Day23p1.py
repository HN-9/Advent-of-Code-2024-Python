with open("input.txt", "r") as file: 
    lines = file.readlines()

connections = []
for line in lines:
    connection = line.strip().split("-")
    connections.append(connection)


graph = {}
for a, b in connections:
    if a not in graph: graph[a] = set()
    if b not in graph: graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

three_nodes = set()
for node in graph:
    neighbors = graph[node]
    for n1 in neighbors:
        for n2 in neighbors:
            if n1 != n2 and n2 in graph[n1]:
                three_nodes.add(tuple(sorted([node, n1, n2])))

filtered_three_nodes = []
for triad in three_nodes:
    for computer in triad:
        if computer.startswith('t'):
            filtered_three_nodes.append(triad)
            break 
print(len(filtered_three_nodes))

