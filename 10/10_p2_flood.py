import os
from helper import *
from collections import defaultdict, deque

inpath = '10.in'
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

# ============ Part 1: just a BFS

dist, _, seen = bfs(start, None, neighbors)
loop = seen
print('Part 1:', max(dist.values()))

# ============ Part 2: Floodfill implementation (not working)

def right_of(orientation):
    a,b = orientation
    return (b, -a)

def fill(cell):
    q = deque()
    q.append(cell)
    seen = set([cell])
    while q:
        v = q.pop()
        r,c = v
        for dr,dc in [(-1,0), (0, 1), (1, 0), (0, -1)]:
            w = (r+dr, c+dc)
            if w in loop:
                continue
            if w not in grid:
                return False
            if w not in seen:
                seen.add(w)
                q.appendleft(w)
    return seen

for dir in [0, 1]: # which direction to move in at the beginning?
    prev = None
    cur = start
    orientation = None
    contained = set()
    hist = set([start])
    round = 0
    while round == 0 or cur != start:
        neighs = neighbors(cur)
        if len(neighs) == 1:
            print(cur)
            exit()
            next = neighs[0]
        else:
            a, b = neighs
            if prev is not None:
                next = a if (a not in hist or (round > 2 and a == start)) else b
            else:
                next = neighs[dir]
        orientation = (next[0] - cur[0], next[1] - cur[1])
        
        dr,dc = right_of(orientation)
        right_cell = (cur[0] + dr, cur[1] + dc)
        if right_cell not in loop: # not in the loop
            fi = fill(right_cell)
            if fi == False: # we are computing outside, need to switch direction
                break
            contained |= fi
        prev = cur
        cur = next
        hist.add(cur)
        round += 1
    if round > 2 and cur == start: # we made it, don't care about other direction
        break

print('Part 2 (wrong):', len(contained))

#for r in range(len(input)):
#    ln = ''
#    for c in range(len(input[0])):
#        ln += ((grid[(r,c)]) if (r,c) not in contained else 'I') if (r,c) not in loop else '*'
#    print(ln)