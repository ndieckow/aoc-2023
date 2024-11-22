from collections import defaultdict

G = open('16.in').read().strip().split('\n')

def solve(G, start):
    seen = defaultdict(list)
    beams = [start] # (r,c,dr,dc)

    while beams:
        r,c,dr,dc = beams.pop()
        if not (0 <= r < len(G)) or not (0 <= c < len(G[0])):
            continue
        if (dr,dc) in seen[(r,c)]:
            continue
        seen[(r,c)].append((dr,dc))
        
        ch = G[r][c]
        if ch == '/':
            if (dr,dc) == (0,1): # right -> up
                beams.append((r-1, c, -1, 0))
            elif (dr,dc) == (1,0): # down -> left
                beams.append((r, c-1, 0, -1))
            elif (dr,dc) == (0,-1): # left -> down
                beams.append((r+1, c, 1, 0))
            elif (dr,dc) == (-1,0): # up -> right
                beams.append((r, c+1, 0, 1))
        elif ch == '\\':
            if (dr,dc) == (0,1): # right -> down
                beams.append((r+1, c, 1, 0))
            elif (dr,dc) == (1,0): # down -> right
                beams.append((r, c+1, 0, 1))
            elif (dr,dc) == (0,-1): # left -> up
                beams.append((r-1, c, -1, 0))
            elif (dr,dc) == (-1,0): # up -> left
                beams.append((r, c-1, 0, -1))
        elif ch == '|':
            if abs(dr) == 1: # up or down
                beams.append((r+dr, c, dr, dc))
            elif abs(dc) == 1: # left or right
                beams.append((r+1, c, 1, 0))
                beams.append((r-1, c, -1, 0))
        elif ch == '-':
            if abs(dr) == 1: # up or down
                beams.append((r, c+1, 0, 1))
                beams.append((r, c-1, 0, -1))
            elif abs(dc) == 1: # left or right
                beams.append((r, c+dc, dr, dc))
        else:
            beams.append((r+dr,c+dc,dr,dc))
    return len([k for k in seen.keys() if seen[k]])

print(solve(G, (0,0,0,1)))

#print(solve(G, (0,3,1,0)))

# Part 2
best = 0
R,C = len(G), len(G[0])
for r in range(R):
    best = max(best, solve(G, (r, 0, 0, 1)), solve(G, (r, C-1, 0, -1)))
for c in range(C):
    best = max(best, solve(G, (0, c, 1, 0)), solve(G, (R-1, c, -1, 0)))
print(best)