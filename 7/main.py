with open('input.txt') as f:
    data = list(map(int, f.read().split(',')))

m = 999999999999

for pos in range(min(data), max(data)):
    fuel = 0
    for x in data:
        for i in range(1, abs(x - pos) + 1):
            fuel += i

    if fuel < m:
        m = fuel

print(m)
