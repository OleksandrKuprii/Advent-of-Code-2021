with open('input.txt') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

result1 = 0
result2 = 0
r = []

score = {')': 3, ']': 57, '}': 1197, '>': 25137}
replace = {')': '(', ']': '[', '}': '{', '>': '<'}

for line in lines:
    stack = []

    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            if stack[-1] == replace[c]:
                stack.pop()
            else:
                result1 += score[c]
                break
    else:
        local_res = 0
        for c in stack[::-1]:
            local_res *= 5
            local_res += list(replace.values()).index(c) + 1
        r.append(local_res)

result2 = sorted(r)[(len(r) - 1) // 2]

print('Part 1: ', result1)
print('Part 2: ', result2)


