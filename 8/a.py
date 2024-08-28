from itertools import groupby
from functools import reduce
import operator


with open('input.txt') as f:
    lines = f.readlines()

count = 0
total = 0
for line in lines:
    parts = [part.strip() for part in line.split("|")]
    patterns = [set(p) for p in parts[0].split()]
    output = [p for p in parts[1].split()]
    count += sum(1 for digit in output if len(digit) in [2, 3, 4, 7])

    lookup = {0x24: '1', 0x5d: '2', 0x6d: '3', 0x2e: '4', 0x6b: '5', 0x7b: '6', 0x25: '7', 0x7f: '8', 0x6f: '9',
              0x77: '0'}
    grouped = {length: list(g) for length, g in groupby(sorted(patterns, key=len), len)}
    seven = grouped[3][0]
    eight = grouped[7][0]
    four = grouped[4][0]
    one = grouped[2][0]

    #   -- 0 --                  --- 01 ---
    #   1     2                  02      04
    #   |- 3 -|  ==> (hex) ==>   --- 08 ---
    #   4     5                  10      20
    #   |- 6 -|                  --- 40 ---

    segments = dict()
    segments[0] = seven - four
    segments[1] = segments[3] = four - one
    segments[6] = reduce(set.intersection, grouped[5]) - four - seven - one
    segments[4] = eight - four - seven - one - segments[6]

    two = next(nr for nr in grouped[5] if nr.intersection(segments[4]))

    segments[3] = (four - one).intersection(two)
    segments[1] = four - one - segments[3]
    segments[2] = one.intersection(two)
    segments[5] = one - two

    segments = {next(iter(char)): 1 << index for index, char in segments.items()}

    number = int(''.join(lookup[reduce(operator.or_, (segments[char] for char in digit))] for digit in output))
    total = total + number

print("Day 8 part 1: {}".format(count))
print("Day 8 part 8: {}".format(total))