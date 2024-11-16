G = [list(x) for x in open('10.in').read().strip().split('\n')]

R = len(G)
C = len(G[0])

dmap = {
    '7': [(0, 1), (1, 0)],
    'F':  [(0, -1), (1, 0)],
    'J': [(1, 0), (0, -1)],
    'L': [(1, 0), (0, 1)],
    '|': [(1, 0), (1, 0)],
    '-': [(0, 1), (0, 1)]
}

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr,sc = r,c
            G[r][c] = '|'  # HARDCODED!!!!!!!!!!!!
            #G[r][c] = 'F'

def follow(pr, pc, r, c):
    ch = G[r][c]
    d = dmap[ch]
    diff = (r-pr, c-pc)
    if diff == d[0]:
        dr,dc = d[1]
    elif diff == (-d[1][0],-d[1][1]):
        dr,dc = -d[0][0], -d[0][1]
    else:
        print('err', pr, pc, r, c)
    return r+dr,c+dc

i = 0
r,c = sr,sc
dr,dc = dmap[G[r][c]][1]
pr,pc = r+dr,c+dc
loopmap = [[0 for _ in range(C)] for _ in range(R)]
while r != sr or c != sc or i == 0:
    loopmap[r][c] = 1
    ch = G[r][c]
    nr,nc = follow(pr,pc,r,c)
    pr,pc = r,c
    r,c = nr,nc
    i += 1
print(i // 2)

# Counting empty space

# Observation: 7 and J can ONLY occur, if one of L or F occurs somewhere before
# Observation 2: There cannot be a | between a {L,F} and the next {7,J}
space = 0
inside = False
last_lf = None
for r in range(R):
    for c in range(C):
        ch = G[r][c]
        if loopmap[r][c]:
            if ch in '7J':
                if last_lf == 'L':
                    if ch == '7':
                        inside = not inside
                elif last_lf == 'F':
                    if ch == 'J':
                        inside = not inside
            
            if ch == '|':
                inside = not inside
            elif ch in 'LF':
                last_lf = ch
        else:
            if inside:
                print(r,c)
                space += 1
print(space)