data = open("data", "r")

# part 1
depth = 0

# part 2
aim_depth = 0
aim = 0

horizontal = 0

while True:
    next = data.readline()
    if next == '':
        break
    instruction = next.split()
    if instruction[0] == 'up':
        aim -= int(instruction[1])
        depth -= int(instruction[1])
    if instruction[0] == 'down':
        aim += int(instruction[1])
        depth += int(instruction[1])
    if instruction[0] == 'forward':
        horizontal += int(instruction[1])
        aim_depth += aim * int(instruction[1])

print(horizontal*depth)
print(horizontal*aim_depth)