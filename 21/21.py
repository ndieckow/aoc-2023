import os
from helper import *
import numpy as np

# Observation:
# Tiles after 2k steps <= Tiles after 2l steps, for l > k
# Tiles after 2k+1 steps <= Tiles after 2l+1 steps, for l > k
# Hence, we just need to "store" the new ones

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

grid = defaultdict(lambda: '.')
start = None
R,C = len(input), len(input[0])
for r,line in enumerate(input):
    for c,ch in enumerate(line):
        if ch == 'S':
            start = (r,c)
            grid[(r,c)] = '.'
        else:
            grid[(r,c)] = ch

def solve(start, N):
    start = (start, N)
    q = deque([start])
    seen = set([start])
    final = set()

    st = N

    while q:
        v, steps = q.pop()
        if steps < st:
            st = steps
        if steps % 2 == 0:
            final.add(v)
        if steps == 0:
            continue
        for (dr, dc) in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr, nc = v[0]+dr, v[1]+dc
            if grid[(nr % R, nc % C)] == '#' or (nr,nc) in seen:
                continue
            q.appendleft(((nr, nc), steps - 1))
            seen.add((nr, nc))
    return len(final)

print('Part 1:', solve(start, 64))

quo, rem = divmod(26501365, R)

c = solve(start, rem)
rhs = [solve(start, rem + R) - c, solve(start, rem + 2*R) - c]
A = np.array([
    [1, 1],
    [4, 2]
])
a, b = [int(x) for x in np.linalg.solve(A, np.array(rhs))]

print('Part 2:', a * quo**2 + b * quo + c)