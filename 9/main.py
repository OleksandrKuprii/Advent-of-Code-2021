data = []

with open('input.txt') as f:
    for x in f.readlines():
        data.append(list(map(int, ['10'] + list(x.strip()) + ['10'])))

data.insert(0, [10] * len(data[0]))
data.append([10] * len(data[0]))

res = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        x = data[i][j]
        if x < data[i-1][j] and x < data[i][j-1] and x < data[i+1][j] and x < data[i][j+1]:
            res += x + 1

print(res)
