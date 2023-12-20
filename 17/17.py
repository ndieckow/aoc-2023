import os
from helper import *
import heapq

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

grid, R, C = read_grid(input)

# Dijkstra
# nodes are of the form (r, c, vert) --> R*C*2 nodes in total
# each node has up to 6 neighbors: {left/up, right/down} x {1, 2, 3}
for part in [1, 2]:
    DIRS = [(1,0), (0,1), (-1,0), (0, -1)]
    dist = defaultdict(lambda: 2**31)
    dist[(0, 0, True)] = 0
    dist[(0, 0, False)] = 0
    q = [(0, 0, 0, False), (0, 0, 0, True)]
    prev = dict()

    while q:
        v = heapq.heappop(q)
        v_dist, r, c, vert = v

        if part == 1:
            rang = range(-3, 4)
        else:
            rang = list(range(4, 11))
            rang = [-n for n in rang] + rang
        
        for steps in rang:
            sgn = -1 if steps < 0 else 1
            if steps == 0:
                continue
            w = (r + steps, c, False) if vert else (r, c + steps, True)
            if tuple(w[:-1]) not in grid:
                continue
            alt = v_dist + sum(grid[(r + sgn * s, c)] if vert else grid[(r, c + sgn * s)] for s in range(1, abs(steps) + 1))
            if alt < dist[w]:
                dist[w] = alt
                heapq.heappush(q, (alt, *w))
                prev[w] = (r, c, vert)

    print(f'Part {part}:', min(dist[(R-1, C-1, False)], dist[(R-1, C-1, True)]))