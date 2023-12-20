from collections import defaultdict, Counter, deque

def memoize(f):
    mem = {}
    def F(*x):
        if x in mem:
            return mem[x]
        val = f(*x)
        mem[x] = val
        return val
    return F

def read_grid(input):
    grid = dict()
    R,C = len(input),len(input[0])
    for r,line in enumerate(input):
        for c,ch in enumerate(line):
            grid[(r,c)] = int(ch)
    return grid, R, C

# does it work with defaultdict?
def grid_bounds(grid, pred=lambda x: True):
    min_r = min(r for (r,c) in grid if pred(grid[(r,c)]))
    max_r = max(r for (r,c) in grid if pred(grid[(r,c)]))
    min_c = min(c for (r,c) in grid if pred(grid[(r,c)]))
    max_c = max(c for (r,c) in grid if pred(grid[(r,c)]))
    return min_r,max_r,min_c,max_c

def print_grid(grid):
    bds = grid_bounds(grid)
    for r in range(bds[0],bds[1]+1):
        line = ''
        for c in range(bds[2],bds[3]+1):
            line += grid[(r,c)]
        print(line)
    print('\n')

# Returns ints in a string that are either surrounded by spaces or at the start or end of the string.
def ints(line):
    ans = []
    words = line.split(' ')
    for w in words:
        try:
            ans.append(int(w))
        except Exception:
            continue
    return ans

# Returns any integers in a string.
def ints2(line):
    ans = []
    cur = []
    for c in line:
        if ord('0') <= ord(c) <= ord('9'):
            cur.append(c)
        elif cur:
            ans.append(int(''.join(cur)))
            cur = []
    return ans

def bfs(start, goal, neighbors):
    q = deque()
    q.append(start)
    dist = dict() # distances
    par = dict() # parents
    dist[start] = 0
    seen = set([start])
    while q:
        v = q.pop()
        if goal is not None and v == goal:
            break
        for w in neighbors(v):
            if w not in seen:
                seen.add(w)
                par[w] = v
                dist[w] = dist[v] + 1
                q.appendleft(w)
    return dist, par, seen

def shortest_path(start, end, par):
    path = [end]
    cur = end
    while cur != start:
        cur = par[cur]
        path.append(cur)
    return reversed(path)