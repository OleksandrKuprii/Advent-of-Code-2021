def print_data(array):
    for t in array:
        for r in t:
            print(' '.join(map(str, r)))
        print()


def count_sum(t):
    s = 0
    for l in t:
        s += sum(l)
    # print(s)
    return s


def count_1(t):
    c = 0
    for rr in t:
        c += rr.count(-1)
    return c


def check(array):
    rr = []
    for ind, t in enumerate(array):
        for r in t:
            if r[0] == r[1] == r[2] == r[3] == r[4] == -1:
                # print([t])
                # print('a')
                # print(ind)

                if ind not in ready:
                    rr.append(ind)
                else:
                    break
        for l in range(5):
            if t[0][l] == t[1][l] == t[2][l] == t[3][l] == t[4][l] == -1:
                # print('b')
                # print(ind)
                if ind not in ready:
                    rr.append(ind)
                else:
                    break
    return rr


data = []

with open('input.txt') as f:
    numbers = list(map(int, f.readline().split(',')))
    f.readline()

    file = f.read()

    for x in file.split('\n\n'):
        table = []
        for row in x.split('\n'):
            table.append(list(map(int, row.split())))
        data.append(table)


ready = set()


ll = len(numbers)

for index, num in enumerate(numbers):
    for i in range(100):
        for j in range(5):
            for k in range(5):
                if data[i][j][k] == num:
                    data[i][j][k] = -1

    res = check(data)

    if res is not None:
        # print(res)
        print(res)
        for _res in res:
            ready.add(_res)

    if len(ready) == 100:
        print(res[-1])
        print(count_sum(data[res[-1]]) + count_1(data[res[-1]]))
        print(num)
        print((count_sum(data[res[-1]]) + count_1(data[res[-1]])) * num)

        # print(res, num, index)
        #
        # print(res * num)

        # print_data(data)

        # exit()
