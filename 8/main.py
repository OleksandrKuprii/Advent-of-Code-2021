inp = []
out = []

with open('input.txt') as f:
    for x in f.readlines():
        inp.append(x.split('|')[0].split())
        out.append(x.split('|')[1].split())

res = 0
for x, _out in zip(inp, out):
    data = [''] * 7

    zero = ''
    one = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    nine = ''
    five_ = []
    six_ = []

    for i in x:
        if len(i) == 2:
            one = i

    for i in x:
        if len(i) == 3:
            seven = i

    for i in x:
        if len(i) == 4:
            four = i

    for i in x:
        if len(i) == 5:
            five_.append(i)

    for i in x:
        if len(i) == 6:
            six_.append(i)

    data[0] = str(next(iter(set(seven) - set(one))))

    for _six in six_:
        diff = set(one) - set(_six)

        if diff:
            six = _six
            data[1] = str(next(iter(diff)))
            data[2] = str(next(iter(set(one) - diff)))

        diff = set(four) - set(_six) - set(one)
        if diff:
            zero = _six
            data[6] = str(next(iter(diff)))

    nine = str(next(iter(set(six_) - {zero} - {six})))
    data[4] = str(next(iter(set('abcdefg') - set(nine))))

    for _five in five_:
        diff = set(six) - set(_five)
        if len(diff) == 1:
            data[4] = str(next(iter(diff)))
            five = _five
            continue

        diff = set(nine) - set(_five)
        if len(diff) == 1:
            data[5] = str(next(iter(diff)))
            three = _five

    data[3] = str(next(iter(set('abcdefg') - set(data))))
    # print(data)

    r = 0
    for i, o in enumerate(_out):
        if len(o) == 7:
            r += 8 * 10 ** (3 - i)
        elif set(o) == set(one):
            r += 1 * 10 ** (3 - i)
        elif set(o) == set(five):
            r += 5 * 10 ** (3 - i)
        elif set(o) == set(three):
            r += 3 * 10 ** (3 - i)
        elif set(o) == set(four):
            r += 4 * 10 ** (3 - i)
        elif set(o) == set(six):
            r += 6 * 10 ** (3 - i)
        elif set(o) == set(seven):
            r += 7 * 10 ** (3 - i)
        elif set(o) == set(nine):
            r += 9 * 10 ** (3 - i)
        else:
            r += 2 * 10 ** (3 - i)
    print(r)
    res += r

print(res)


