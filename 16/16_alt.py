# DISCLAIMER: This solution does not work yet.

# analyze (0, 19); should be crazy long, but this algorithm just says 60

import os
from helper import *
import sys
sys.setrecursionlimit(100000)

inpath = '16.in'
input = open(inpath).read().split('\n')

grid = defaultdict(lambda: '+')

R,C = len(input), len(input[0])
for r,line in enumerate(input):
    for c,ch in enumerate(line):
        grid[(r,c)] = ch

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

def move(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

def move_batch(pos, dir):
    cells = [pos]
    pos = move(pos, dir)
    while grid[pos] == '.':
        cells.append(pos)
        pos = move(pos, dir)
    return pos, set(cells)

def reverse(dir):
    return (-dir[0], -dir[1])

DP = {}
def solve(pos, dir, hist=[]):
    # Return set of energized cells
    if grid[pos] == '+':
        return set()
    state = (pos, dir)
    if state in DP:
        return DP[state]
    
    ans = None
    dirs = []
    if grid[pos] == '\\': # right or down, or up
        if dir == RIGHT:
            dirs.append(DOWN)
        elif dir == UP:
            dirs.append(LEFT)
        elif dir == DOWN:
            dirs.append(RIGHT)
        elif dir == LEFT:
            dirs.append(UP)
    elif grid[pos] == '/':
        if dir == RIGHT:
            dirs.append(UP)
        elif dir == UP:
            dirs.append(RIGHT)
        elif dir == DOWN:
            dirs.append(LEFT)
        elif dir == LEFT:
            dirs.append(DOWN)
    elif grid[pos] == '|':
        if dir == RIGHT:
            dirs += [UP, DOWN]
        elif dir == UP:
            pass
        elif dir == DOWN:
            pass
        elif dir == LEFT:
            dirs += [UP, DOWN]
    elif grid[pos] == '-':
        if dir == RIGHT:
            pass
        elif dir == UP:
            dirs += [LEFT, RIGHT]
        elif dir == DOWN:
            dirs += [LEFT, RIGHT]
        elif dir == LEFT:
            pass
    
    if dirs == []:
        dirs.append(dir) # no change in direction
    
    ans = set()
    for nextdir in dirs:
        nextpos, cells = move_batch(pos, nextdir)
        if (nextpos,nextdir) in hist:
            # find the loop
            idx = hist.index((nextpos, nextdir))
            loop = hist[idx:] + [(pos,dir)]
            #print([len(DP[x]) if x in DP else -1 for x in loop])
            #print(loop)
            return cells
        ans |= (cells | solve(nextpos, nextdir, hist + [(pos, dir)]))
    
    DP[state] = ans
    return ans

energized = solve((0, 0), (0, 1))

print('Part 1:', len(energized))

ans = 0
for r,dir in [(0, DOWN), (R-1, UP)]:
    for c in range(C):
        new_ans = len(solve((r,c), dir))
        print(r, c, new_ans)
        ans = max(ans, new_ans)
for c,dir in [(0, RIGHT), (C-1, LEFT)]:
    for r in range(R):
        new_ans = len(solve((r,c), dir))
        print(r, c, new_ans)
        ans = max(ans, new_ans)

print('Part 2:', ans)