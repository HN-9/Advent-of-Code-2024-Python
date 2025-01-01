import time
with open("input.txt", "r") as file:
    lines = file.readlines()

def secretStep(secret):
 
    temp = secret * 64

    secret = temp ^ secret

    secret = secret % 16777216
    temp = secret // 32 
    secret = temp ^ secret
    secret = secret % 16777216
    temp = secret * 2048
    secret = temp ^ secret
    secret = secret % 16777216
    return secret

def shiftStep(secret): 
    secret = (secret << 6) ^ secret
    secret &= 0xFFFFFF 
    secret = (secret >> 5) ^ secret

    secret &= 0xFFFFFF

    secret = (secret << 11) ^ secret
    secret &= 0xFFFFFF
    return secret

start_secret = time.time()
totalSecret = 0
for line in lines:
    secret = int(line)
    for _ in range(2000):
        secret = secretStep(secret)
    totalSecret += secret
end_secret = time.time()

start_shift = time.time()
totalShift = 0
for line in lines:
    shift = int(line)
    for _ in range(2000):
        shift = shiftStep(shift)
    totalShift += shift
end_shift = time.time()

print("Total Secret:", totalSecret)
print("Total Shift:", totalShift)
print(f"Time for secretStep: {end_secret - start_secret:.6f} seconds")
print(f"Time for shiftStep: {end_shift - start_shift:.6f} seconds")

