d = {}

with open('input.txt') as f:
    formula = list(f.readline().strip())

    f.readline()

    data = {}
    for x in f.readlines():
        a, b = x.strip().split('->')
        data[a.strip()] = b.strip()
        d[a.strip()] = 0

for i in range(len(formula) - 1):
    d[formula[i] + formula[i+1]] += 1

for _ in range(10):
    d_c = dict(d)
    for k, v in d.items():
        if v:
            d_c[k[0] + data[k]] += v
            d_c[data[k] + k[1]] += v
            d[k] = 0

    d = dict(d_c)
    print(d)
    # break

# print(d)


