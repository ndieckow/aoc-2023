import os
from helper import *

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

grid = defaultdict(lambda: '+')

R,C = len(input), len(input[0])
for r,line in enumerate(input):
    for c,ch in enumerate(line):
        grid[(r,c)] = ch

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

def move(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

def reverse(dir):
    return (-dir[0], -dir[1])

def solve(start, dir):
    poss = [start]
    dirs = [dir]

    energized = set()
    history = set()
    while True:
        new_energized = energized | set(poss)
        if poss == [] and dirs == []:
            break
        #if len(new_energized) == len(energized):
        #    break
        energized = new_energized
        newposs = []
        newdirs = []
        for i in range(len(poss)):
            pos, dir = poss[i], dirs[i]
            #print(pos, dir)
            if (pos, dir) in history:
                continue
            history.add((pos, dir))
            pos = move(pos, dir)
            if grid[pos] == '+':
                continue
            newposs.append(pos)
            if grid[pos] == '\\': # right or down, or up 
                if dir == RIGHT:
                    dir = DOWN
                elif dir == UP:
                    dir = LEFT
                elif dir == DOWN:
                    dir = RIGHT
                elif dir == LEFT:
                    dir = UP
            elif grid[pos] == '/':
                if dir == RIGHT:
                    dir = UP
                elif dir == UP:
                    dir = RIGHT
                elif dir == DOWN:
                    dir = LEFT
                elif dir == LEFT:
                    dir = DOWN
            elif grid[pos] == '|':
                if dir == RIGHT:
                    newposs.append(pos)
                    newdirs += [UP, DOWN]
                elif dir == UP:
                    pass
                elif dir == DOWN:
                    pass
                elif dir == LEFT:
                    newposs.append(pos)
                    newdirs += [UP, DOWN]
            elif grid[pos] == '-':
                if dir == RIGHT:
                    pass
                elif dir == UP:
                    newposs.append(pos)
                    newdirs += [LEFT, RIGHT]
                elif dir == DOWN:
                    newposs.append(pos)
                    newdirs += [LEFT, RIGHT]
                elif dir == LEFT:
                    pass
            if len(newdirs) < len(newposs):
                newdirs.append(dir)
        poss = newposs.copy()
        dirs = newdirs.copy()


    return len(energized) - 1

print('Part 1:', solve((0, -1), (0, 1)))

ans = 0
for r,dir in [(-1, DOWN), (R, UP)]:
    for c in range(C):
        ans = max(ans, solve((r,c), dir))
for c,dir in [(-1, RIGHT), (C, LEFT)]:
    for r in range(R):
        ans = max(ans, solve((r,c), dir))

print('Part 2:', ans)