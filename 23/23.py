import os
from helper import *

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

R,C = len(input), len(input[0])
grid = defaultdict(lambda: '#')
for r,line in enumerate(input):
    for c,ch in enumerate(line):
        grid[(r,c)] = ch

start = (0, 1)
goal = (R-1, C-2)

# figure out the graph
adj = defaultdict(list)

q = deque([(start, None, 0, None)])
seen = set([start])
nodes = [start]
adj = defaultdict(list)
cnt = 0
while q:
    (r, c), parent, cnt, prev = q.pop()
    neighs = []
    for (dr, dc) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r+dr, c+dc
        if grid[(nr, nc)] == '#':
            continue
        neighs.append((nr, nc))
    
    if len(neighs) >= 3 or (r, c) == goal:
        adj[parent].append(((r,c), cnt))
        nodes.append((r, c))
    
    for (nr, nc) in neighs:
        if (nr, nc) == prev or ((nr < r or nc < c) and grid[(nr, nc)] in ['v', '>']):
            continue
        seen.add((nr, nc))
        q.appendleft(((nr, nc), parent if len(neighs) < 3 and (r,c) != start else (r, c), cnt + 1 if len(neighs) < 3 else 1, (r,c)))


# nodes is already in topological order
dist = defaultdict(lambda: -int(1e9))
dist[start] = 0
for v in nodes:
    for (w, weight) in adj[v]:
        alt = dist[v] + weight
        if dist[w] < alt:
            dist[w] = alt
print('Part 1:', dist[goal])