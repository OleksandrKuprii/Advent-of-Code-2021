from functools import reduce
import operator


with open('input.txt') as f:
    data = {(row, col): int(val) for row, line in enumerate(f.readlines()) for col, val in enumerate(line.strip())}


def adjacent(x, y):
    return (x+1, y), (x, y+1), (x-1, y), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)


explosions = 0

for step in range(1000):
    prev_exp = explosions
    data = {k: v + 1 for k, v in data.items()}

    while reduce(operator.or_, map(lambda x: x > 9, data.values())):
        for k, v in data.items():
            if v > 9:
                data[k] = 0
                explosions += 1
                for x, y in adjacent(*k):
                    try:
                        if data[(x, y)] != 0:
                            data[(x, y)] += 1
                    except KeyError:
                        pass

    if step == 99:
        print('Part 1: ', explosions)

    if (explosions - prev_exp) == 100:
        print('Part 2: ', step+1)
        break
