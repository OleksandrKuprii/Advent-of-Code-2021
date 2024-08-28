with open('input.txt') as f:
    data = f.read().split()

position = 0
while len(data) != 1:
    common = 0

    for x in data:
        common += int(x[position])

    if (len(data) - common) > common:
        common = '0'
    else:
        common = '1'

    new_data = []
    for i in range(len(data)):
        if data[i][position] == common:
            new_data.append(data[i])

    position += 1

    data = list(new_data)
    new_data = []

    print(len(data), data)

o2 = int(data[0], 2)

with open('input.txt') as f:
    data = f.read().split()

position = 0
while len(data) != 1:
    common = 0

    for x in data:
        common += int(x[position])

    if (len(data) - common) > common:
        common = '0'
    else:
        common = '1'

    new_data = []
    for i in range(len(data)):
        if data[i][position] != common:
            new_data.append(data[i])

    position += 1

    data = list(new_data)
    new_data = []

    print(len(data), data)

co2 = int(data[0], 2)

print(o2, co2)
print(o2 * co2)
