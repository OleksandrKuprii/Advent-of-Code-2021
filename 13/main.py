from functools import reduce
from pprint import pprint
from itertools import chain


data = []
fold = []

for _ in range(1400):
    data.append([False] * 1400)

with open('input.txt') as f:
    for line in f.readlines():
        if line.startswith('fold'):
            if 'x' in line:
                fold.append(('x', int(line.strip().split('=')[1])))
            else:
                fold.append(('y', int(line.strip().split('=')[1])))
        elif line != '\n':
            x, y = map(int, line.strip().split(','))
            data[y][x] = True


for axes, number in fold:
    if axes == 'y':
        for y in range(len(data)):
            if y < number:
                for x in range(len(data[y])):
                    data[y][x] = data[y][x] or data[2 * number - y][x]
            else:
                data[y] = [False] * 1400
    else:
        for y in range(len(data)):
            for x in range(len(data[y])):
                if x < number:
                    data[y][x] = data[y][x] or data[y][2 * number - x]
                else:
                    data[y][x] = False
    print(sum(chain(*data)))
    # print(data)

# print(data)

for x in data[:8]:
    print(' '.join(['#' if y else '.' for y in x]))
