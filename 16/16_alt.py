# DISCLAIMER: This solution does not work yet.

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
def solve(pos, dir, depth=100):
    #print(pos, dir)
    #print(DP)
    # Return set of energized cells
    # pos is expected to NOT point at an empty cell
    if grid[pos] == '+' or depth == 0:
        return set()
    state = (pos, dir, depth)
    if state in DP:
        return DP[state]
    
    ans = None
    dirs = []
    if grid[pos] == '.':
        pos, cells = move_batch(pos, dir)
        ans = cells | solve(pos, dir, depth-1)
        DP[(pos, dir, depth)] = ans
        return ans
    elif grid[pos] == '\\': # right or down, or up
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
        ans |= (cells | solve(nextpos, nextdir, depth-1))
    
    DP[state] = ans
    return ans

energized = solve((0, 0), (0, 1))

print('Part 1:', len(energized))

exit()
ans = 0
for r,dir in [(-1, DOWN), (R, UP)]:
    for c in range(C):
        ans = max(ans, solve((r,c), dir))
for c,dir in [(-1, RIGHT), (C, LEFT)]:
    for r in range(R):
        ans = max(ans, solve((r,c), dir))

print('Part 2:', ans)