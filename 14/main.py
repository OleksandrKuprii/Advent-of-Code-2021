with open('input.txt') as f:
    formula = list(f.readline().strip())

    f.readline()

    data = {}
    for x in f.readlines():
        a, b = x.strip().split('->')
        data[a.strip()] = b.strip()

for _ in range(40):
    formula_copy = [formula[0]]
    for i in range(len(formula) - 1):
        formula_copy.append(data[formula[i] + formula[i + 1]])
        formula_copy.append(formula[i + 1])
    formula = list(formula_copy)
    print(_)

print(max([formula.count(x) for x in formula]) - min([formula.count(x) for x in formula]))
