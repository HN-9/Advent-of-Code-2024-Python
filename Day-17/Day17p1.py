
with open("Day-17-Challenge/input.txt", "r") as file:
    lines = file.readlines()

registers = {
    "A": int(lines[0].split(":")[1].strip()),
    "B": int(lines[1].split(":")[1].strip()),
    "C": int(lines[2].split(":")[1].strip())
}
program = []
program_line = lines[4].split(":")[1].strip()
for value in program_line.split(","):
    program.append(int(value))


def get_combo_value(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    else:
        raise ValueError("Invalid operand combo: 7 or more can not be used")

output = []
pointer = 0
while pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer + 1]

    if opcode == 0:  
        registers["A"] //= 2 ** get_combo_value(operand)

    elif opcode == 1:  
        registers["B"] ^= operand

    elif opcode == 2:  
        registers["B"] = get_combo_value(operand) % 8

    elif opcode == 3:  
        if registers["A"] != 0:
            pointer = operand
            continue 

    elif opcode == 4:  
        registers["B"] ^= registers["C"]

    elif opcode == 5: 
        output.append(get_combo_value(operand) % 8)

    elif opcode == 6:  
        registers["B"] = registers["A"] // 2 ** get_combo_value(operand)

    elif opcode == 7:  
        registers["C"] = registers["A"] // 2 ** get_combo_value(operand)

    else:
        raise ValueError(f"Unknown opcode: {opcode}")

    pointer += 2 



string_output = []
for value in output:
    string_output.append(str(value))

print(",".join(string_output))
