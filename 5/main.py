import re


data = []
for i in range(1000):
    data.append([0] * 1000)

with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()

        match = re.search(r'(\d*),(\d*) -> (\d*),(\d*)', line)
        x1 = int(match.group(1))
        y1 = int(match.group(2))
        x2 = int(match.group(3))
        y2 = int(match.group(4))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                data[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                data[y1][x] += 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            for x in range(x1, x2 + 1):
                data[y1][x] += 1
                y1 += (1 if y1 < y2 else -1)

res = 0

for x in data:
    for y in x:
        if y >= 2:
            res += 1

print(res)


