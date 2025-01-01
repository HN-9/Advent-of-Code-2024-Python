def gcd(a, b): 
    while b != 0:
        a, b = b, a % b
    return a

def solve_machine(Ax, Ay, Bx, By, Px, Py):
    g1 = gcd(Ax, Bx)
    g2 = gcd(Ay, By)
    if Px % g1 != 0 or Py % g2 != 0:
        return None  


    B_max = min(100, Px // Bx) if Bx > 0 else 0
    for B in range(B_max, -1, -1):
        remaining_x = Px - Bx * B
        if Ax != 0 and remaining_x % Ax == 0:
            A = remaining_x // Ax
            if 0 <= A <= 100:
                if Ay * A + By * B == Py:
                    cost = 3 * A + 1 * B
                    return cost

    return None


machines = []
with open("input.txt", "r") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    if lines[i].startswith("Button A:"):
        part = lines[i].split(",")
        Ax_str = part[0].split("X+")[-1].strip()
        Ay_str = part[1].split("Y+")[-1].strip()
        Ax = int(Ax_str)
        Ay = int(Ay_str)

        i += 1
        part = lines[i].split(",")
        Bx_str = part[0].split("X+")[-1].strip()
        By_str = part[1].split("Y+")[-1].strip()
        Bx = int(Bx_str)
        By = int(By_str)

        i += 1
        part = lines[i].split(",")
        Px_str = part[0].split("X=")[-1].strip()
        Py_str = part[1].split("Y=")[-1].strip()
        Px = int(Px_str)
        Py = int(Py_str)

        machines.append((Ax, Ay, Bx, By, Px, Py))
    
    i += 1

counter = 0
total_cost = 0
for (Ax, Ay, Bx, By, Px, Py) in machines:
    cost = solve_machine(Ax, Ay, Bx, By, Px, Py)
    print("Trying machine: ", counter, " amount ", cost)
    counter += 1
    if cost is not None:
        total_cost += cost

print(total_cost)
