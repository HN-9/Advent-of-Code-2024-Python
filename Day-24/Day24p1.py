with open("Day-24-Challenge\input.txt", "r") as file:
    lines = file.readlines()

first_data = []
second_data = []
switch = False
for line in lines:
    if line == "\n":
        switch = True
        continue
    if switch == False: 
        first_data.append(line.strip())
    else:
        second_data.append(line.strip())

first_clean = {}
second_clean = {}
for first in first_data:
    left, right = first.split(":")
    first_clean[left] = int(right)
for second in second_data:
    data1, operator, data2, arrow, data3 = second.split(" ")
    second_clean[data3] = (data1, data2, operator)


def operate(data3, wire_values, gates):

    if data3 in wire_values:
        return wire_values[data3]

    data1, data2, operator = gates[data3]

    if data1 not in wire_values:
        wire_values[data1] = operate(data1, wire_values, gates)
    if data2 not in wire_values:
        wire_values[data2] = operate(data2, wire_values, gates)

    if operator == "AND":
        wire_values[data3] = wire_values[data1] & wire_values[data2]
    elif operator == "OR":
        wire_values[data3] = wire_values[data1] | wire_values[data2]
    elif operator == "XOR":
        wire_values[data3] = wire_values[data1] ^ wire_values[data2]

    return wire_values[data3]


wire_values = first_clean.copy()

for wire in second_clean.keys():
    operate(wire, wire_values, second_clean)

z_wires = sorted([key for key in wire_values.keys() if key.startswith("z")])

binary_result = "".join(str(wire_values[z]) for z in z_wires[::-1])
decimal_result = int(binary_result, 2)

sorted_results = sorted(wire_values.items())

print(f"Binary Result from z wires: {binary_result}")
print(f"Decimal result: {decimal_result}")

