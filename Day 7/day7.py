data = open("data", "r")
nums = data.read().split(',')

arr = [0] * 9
arr_temp = [0] * 9

for x in nums:
    arr[int(x)] += 1

# days = 80
days = 256

for x in range(0, days):
    print(arr)
    num_new = arr[0]
    for y in range(1, len(arr)):
        arr_temp[y - 1] = arr[y]
    arr = arr_temp
    arr[6] += num_new
    arr[8] = num_new

sum = 0
for x in arr:
    sum += x

print(sum)
