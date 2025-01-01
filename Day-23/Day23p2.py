with open("Day-23-Challenge/input.txt", "r") as file: 
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
visited_networks = set()

def search(node, network):
    key = tuple(sorted(network))
    if key in visited_networks:
        return
    visited_networks.add(key)

    for neighbor in graph[node]:
        if neighbor in network:
            continue
        if not all(neighbor in graph[other] for other in network):
            continue
        search(neighbor, network | {neighbor}) 

for node in graph:
    search(node, {node})

largest_network = max(visited_networks, key=len)

password = ",".join(sorted(largest_network))
print(password)

