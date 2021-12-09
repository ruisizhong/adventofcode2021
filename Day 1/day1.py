data = open("data", "r")

increases = 0
sum_increases = 0
str_list = data.read().split()

# convert to int
depths = [int(i) for i in str_list]

# part 1
for x in range(len(depths)-1):
    prevNum = int(depths[x])
    nextNum = int(depths[x + 1])
    if nextNum > prevNum:
        increases += 1

# part 2
for x in range(len(depths)-3):
    sum1 = depths[x] + depths[x+1] + depths[x+2]
    sum2 = depths[x+1] + depths[x+2] + depths[x+3]
    if sum2 > sum1:
        sum_increases += 1

print(increases)
print(sum_increases)
