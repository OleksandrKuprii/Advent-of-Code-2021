data = {}
result = 0


def find_path(path):
    global result
    node: str
    for node in data[path[-1]]:
        if len([x for x in [path.count(n) for n in path if n.islower()] if x > 1]) > 2:
            continue
        elif node.islower() and path.count(node) == 2:
            continue
        elif node == 'end':
            result += 1
            print(','.join(['start'] + path + ['end']))
            continue
        else:
            find_path(path + [node])


with open('input.txt') as f:
    for x, y in map(lambda i: i.strip().split('-'), f.readlines()):
        if x not in data:
            data[x] = []
        if y not in data:
            data[y] = []

        if x == 'start':
            data[x].append(y)
        elif x == 'end':
            data[y].append(x)
        elif y == 'start':
            data[y].append(x)
        elif y == 'end':
            data[x].append(y)
        else:
            data[x].append(y)
            data[y].append(x)
    # print(data)


for start in data['start']:
    find_path([start])


print(result)
