import math

data = open("data", "r")

arr = [0] * 12
gamma_arr = [0] * 12
epsilon_arr = [0] * 12

data_dict = {}

while True:
    next = data.readline()
    if next == '':
        break
    for x in range(0, len(next)-1):
        if int(next[x]) == 1:
            arr[x] += 1
        if int(next[x]) == 0:
            arr[x] -= 1

    cur = data_dict
    for i, x in enumerate(next):
        if cur.get(x):
            cur[x]['count'] += 1
        else:
            cur[x] = {'0': {}, '1': {}, 'count': 1}
        cur = cur[x]

cur = data_dict
more_common = ''
while True:
    count0 = cur['0'].get('count', 0)
    count1 = cur['1'].get('count', 0)

    if count1 == 0 and count0 == 0:
        break

    if count1 >= count0:
        more_common += '1'
        cur = cur['1']
    else:
        more_common += '0'
        cur = cur['0']

cur = data_dict
less_common = ''
while True:
    count0 = cur['0'].get('count', 0)
    count1 = cur['1'].get('count', 0)

    if count1 == 0 and count0 == 0:
        break

    if not count1:
        less_common += '0'
        cur = cur['0']
    elif not count0:
        less_common += '1'
        cur = cur['1']
    elif count1 < count0:
        less_common += '1'
        cur = cur['1']
    else:
        less_common += '0'
        cur = cur['0']

power = len(arr)-1
gamma = 0
epsilon = 0
oxygenRating = int(more_common, base=2)
CO2Rating = int(less_common, base=2)

for x in range(0, len(arr)):
    if arr[x] > 0:
        gamma_arr[x] = 1
        gamma += math.pow(2, power)
        epsilon_arr[x] = 0
    if arr[x] < 0:
        gamma_arr[x] = 0
        epsilon_arr[x] = 1
        epsilon += math.pow(2, power)
    power -= 1

print(gamma * epsilon)
print(oxygenRating * CO2Rating)
