import os
from helper import *

inpath = '23.in'
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
        if grid[(nr, nc)] != '#':
            neighs.append((nr, nc))
    if len(neighs) > 2 or (r, c) == goal:
        adj[parent].append(((r,c), cnt))
        adj[(r,c)].append((parent, cnt))
        if (r,c) not in nodes:
            nodes.append((r, c))
        else:
            continue
    for (nr, nc) in neighs:
        if (nr, nc) == prev:
            continue
        seen.add((nr, nc))
        q.appendleft(((nr, nc), parent if len(neighs) < 3 and (r,c) != start else (r, c), cnt + 1 if len(neighs) < 3 else 1, (r,c)))


DP = dict()
def solve(v, hist = []):
    if v == goal:
        return 0
    state = (v, frozenset(hist))

    if state in DP:
        return DP[state]

    ans = -100000000000
    for w, weight in adj[v]:
        if w in hist:
            continue
        alt = weight + solve(w, hist = hist + [w])
        if alt > ans:
            ans = alt
    DP[state] = ans
    return ans

print('Part 2:', solve(start, hist=[start]))