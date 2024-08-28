from functools import reduce
import operator


with open('input.txt') as f:
    data = list(map(lambda x: x.strip(), f.readlines()))


def day9(lines):
    def adjacent(x, y):
        return (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)

    map = {(int(row), int(col)): int(value) for row, values in enumerate(lines) for col, value in enumerate(values)}
    risk = sum(height + 1 for (x, y), height in map.items() if all(map.get((ax, ay), 10) > height for ax, ay in adjacent(x, y)))
    print("Day 9 part 1: {}".format(risk))

    basins = {(row, col) for (row, col), height in map.items() if height < 9}
    print(basins)

    def basin_size(x, y):
        basins.remove((x, y))
        return sum(basin_size(x2, y2) for x2, y2 in adjacent(x, y) if (x2, y2) in basins) + 1

    sizes = list()
    while basins:
        sx, sy = next(iter(basins))
        sizes.append(basin_size(sx, sy))

    print("Day 9 part 2: {}".format(reduce(operator.mul, sorted(sizes)[-3:])))



day9(data)
