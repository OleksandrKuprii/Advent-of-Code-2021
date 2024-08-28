from time import time

start = time()


with open('input.txt') as f:
    line = list(map(int, f.readline().strip().split(',')))

data = [0] * 10

for x in line:
    data[x] += 1


for day in range(256):

    data[9] = data[0]
    data[7] += data[0]

    del data[0]
    data.append(0)

    print(day)

print(sum(data))

print(time() - start)
