import os
from helper import *

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

grid = defaultdict(lambda: '.')
R,C = len(input), len(input[0])

ans = 0
for r,line in enumerate(input):
    for c,ch in enumerate(line):
        rr = 0
        if ch == 'O':
            rr = 1
            while grid[(r-rr,c)] == '.' and rr <= r:
                rr += 1
            rr -= 1
            ans += R - (r - rr)
        grid[(r - rr,c)] = ch
print('Part 1:', ans)

def tilt_up_down(grid, dir):
    assert dir in [-1, 1]
    if dir == -1:
        rowrange = range(R)
        def rlim(r): return r
    else:
        rowrange = range(R-1,-1,-1)
        def rlim(r): return R - r - 1
    for r in rowrange:
        for c in range(C):
            ch = grid[(r,c)]
            if ch != 'O':
                continue
            rr = 1
            while grid[(r + dir*rr,c)] == '.' and rr <= rlim(r):
                rr += 1
            rr -= 1
            grid[(r,c)] = '.'
            grid[(r + dir*rr,c)] = ch

def tilt_left_right(grid, dir):
    assert dir in [-1, 1]
    if dir == -1:
        colrange = range(C)
        def clim(c): return c
    else:
        colrange = range(C-1,-1,-1)
        def clim(c): return C - c - 1
    for c in colrange:
        for r in range(R):
            ch = grid[(r,c)]
            if ch != 'O':
                continue
            cc = 1
            while grid[(r, c + dir*cc)] == '.' and cc <= clim(c):
                cc += 1
            cc -= 1
            grid[(r,c)] = '.'
            grid[(r,c + dir*cc)] = ch

from copy import deepcopy

# already tilted north
tilt_left_right(grid, -1)
tilt_up_down(grid, 1)
tilt_left_right(grid, 1)
history = [deepcopy(grid)]

double_at, double_from = None, None

for i in range(1000000000):
    tilt_up_down(grid, -1)
    tilt_left_right(grid, -1)
    tilt_up_down(grid, 1)
    tilt_left_right(grid, 1)

    if grid in history:
        double_at = i+1
        double_from = history.index(grid)
        break
    history.append(deepcopy(grid))

until = (1000000000 - double_at - 1) % (double_at - double_from)
grid = history[double_from + until]

def compute_ans(grid):
    mul = R
    ans = 0
    for r in range(R):
        for c in range(C):
            if grid[(r,c)] == 'O':
                ans += mul
        mul -= 1
    return ans

print('Part 2:', compute_ans(grid))