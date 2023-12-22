import os
from helper import *

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

def brick_size(brick):
    return sum(abs(brick[0][i] - brick[1][i]) for i in range(3))

bricks = []
bs = 0
for line in input:
    end1, end2 = line.split('~')
    brick = tuple(tuple(int(x) for x in end.split(',')) for end in [end1, end2])
    bricks.append(brick)

bricks.sort(key = lambda x: x[0][2])

brick_layer = [set() for _ in range(bricks[-1][1][2]+1)]
brick_map = []
id = 0
supports = defaultdict(set)
supported_by = defaultdict(set)
for brick in bricks:
    newbrick = list(list(x) for x in brick)
    while newbrick[0][2] > 1:
        valid = True
        for ob_id in brick_layer[newbrick[0][2] - 1]:
            ob = brick_map[ob_id]
            # check for intersection in x and y coords
            if all(newbrick[1][i] >= ob[1][i] and newbrick[0][i] <= ob[1][i] or ob[1][i] >= newbrick[1][i] and ob[0][i] <= newbrick[1][i] for i in [0, 1]):
                valid = False
                supports[ob_id].add(id)
                supported_by[id].add(ob_id)
        if not valid:
            break
        newbrick[0][2] -= 1
        newbrick[1][2] -= 1
    brick_map.append(tuple(tuple(x) for x in newbrick))
    brick_layer[newbrick[0][2]].add(id)
    brick_layer[newbrick[1][2]].add(id)
    id += 1

ans = 0
for bid in range(len(brick_map)):
    ans += int(all(len(supported_by[obid]) > 1 for obid in supports[bid]))
print('Part 1:', ans)

ans2 = 0
for bid in range(len(brick_map)):
    falling = set([bid])
    q = deque([bid])
    while q:
        v = q.pop()
        for obid in supports[v]:
            # 1. is it supported by others, or is it already falling?
            if len(supported_by[obid].difference(falling)) > 0 or obid in falling:
                continue
            falling.add(obid)
            q.appendleft(obid)
    ans2 += len(falling) - 1
print('Part 2:', ans2)