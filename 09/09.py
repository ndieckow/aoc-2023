import os
from helper import *
import math

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

def differences(x):
    out = []
    for i in range(len(x)-1):
        out.append(x[i+1] - x[i])
    return out

def solve1():
    ans = 0
    max_deg = 0
    for line in input:
        cnt = 0
        vals = ints(line)
        tmp = [vals[-1]]
        while not all(x == 0 for x in vals):
            cnt += 1
            vals = differences(vals)
            tmp.append(vals[-1])
        ans += sum(tmp)
        max_deg = max(max_deg, cnt)
    return ans

def solve2():
    ans = 0
    for line in input:
        vals = ints(line)
        tmp = [vals[0]]
        sgn = -1
        while not all(x == 0 for x in vals):
            vals = differences(vals)
            tmp.append(sgn * vals[0])
            sgn *= -1
        ans += sum(tmp)
    return ans

print('Part 1:', solve1())
print('Part 2:', solve2())