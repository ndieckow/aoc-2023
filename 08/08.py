import os
from helper import *
import math

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

ins = input[0] # instructions
nbs = dict() # neighbors

for line in input[2:]:
    lhs, rhs = line.split(' = ')
    left, right = rhs[1:-1].split(', ')
    nbs[lhs] = (left, right)

t = {'L': 0, 'R': 1}

def solve1():
    cur = 'AAA'
    steps = 0
    while cur != 'ZZZ':
        cur = nbs[cur][t[ins[steps % len(ins)]]]
        steps += 1
    return steps

def solve2():
    starts = [x for x in nbs.keys() if x[-1] == 'A']
    nums = []
    for cur in starts:
        steps = 0
        while cur[-1] != 'Z':
            cur = nbs[cur][t[ins[steps % len(ins)]]]
            steps += 1
        nums.append(steps)
    return math.lcm(*nums)

print('Part 1:', solve1())
print('Part 2:', solve2())