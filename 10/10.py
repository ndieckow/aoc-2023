import os
from helper import *
from collections import defaultdict, deque

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

grid = defaultdict(lambda: '.')
start = None

for r,line in enumerate(input):
    for c,ch in enumerate(line):
        grid[(r,c)] = ch
        if ch == 'S':
            start = (r,c)

def neighbors(cell):
    r, c = cell
    ch = grid[(r,c)]
    neighs = []
    if ch in '|':
        if grid[(r-1,c)] in ['|', '7', 'F']:
            neighs.append((r-1,c))
        if grid[(r+1, c)] in ['|', 'J', 'L']:
            neighs.append((r+1,c))
    elif ch == '-':
        if grid[(r, c-1)] in ['-', 'L', 'F']:
            neighs.append((r,c-1))
        if grid[(r, c+1)] in ['-', '7', 'J']:
            neighs.append((r,c+1))
    elif ch == 'L':
        if grid[(r-1,c)] in ['|', '7', 'F']:
            neighs.append((r-1,c))
        if grid[(r, c+1)] in ['-', '7', 'J']:
            neighs.append((r,c+1))
    elif ch == 'J':
        if grid[(r-1,c)] in ['|', '7', 'F']:
            neighs.append((r-1,c))
        if grid[(r, c-1)] in ['-', 'L', 'F']:
            neighs.append((r,c-1))
    elif ch == '7':
        if grid[(r, c-1)] in ['-', 'L', 'F']:
            neighs.append((r,c-1))
        if grid[(r+1, c)] in ['|', 'J', 'L']:
            neighs.append((r+1,c))
    elif ch == 'F':
        if grid[(r, c+1)] in ['-', '7', 'J']:
            neighs.append((r,c+1))
        if grid[(r+1, c)] in ['|', 'J', 'L']:
            neighs.append((r+1,c))
    return neighs

# Find the right pipe at starting position.
sr, sc = start
for sym in ['|', '-', 'L', 'J', '7', 'F']:
    grid[start] = sym
    if len(neighbors(start)) == 2:
        break

dist, _, seen = bfs(start, None, neighbors)
loop = seen
print('Part 1:', max(dist.values()))

# ============ Part 2: Left check implemenation (thanks, reddit)

inside = 0
for r in range(len(input)):
    left = 0
    for c in range(len(input[0])):
        if (r,c) not in loop and left % 2 == 1:
            inside += 1
        if grid[(r,c)] in ['|', 'L', 'J'] and (r,c) in loop:
            left += 1
print('Part 2:', inside)