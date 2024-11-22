input = open("14.in").read().strip().split('\n')
N = len(input)
G = [list(line) for line in input]

def render(G):
    print('\n'.join([''.join(x) for x in G]) + '\n')

def score(G):
    ans = 0
    for i,row in enumerate(G):
        for ch in row:
            if ch == 'O':
                ans += N-i
    return ans

def rotate(G): # rotates clockwise by 90°
    newG = [[None for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            newG[r][c] = G[N-c-1][r]
    return newG

def tilt(G):
    newG = [[None for _ in range(N)] for _ in range(N)]
    pivots = [-1 for _ in range(N)]
    for r,row in enumerate(G):
        for c,ch in enumerate(row):
            newG[r][c] = ch
            if ch == '#':
                pivots[c] = r
            elif ch == 'O':
                newG[r][c] = '.'
                piv = pivots[c]
                newG[piv+1][c] = 'O'
                pivots[c] = piv+1
    return newG

def cycle(G):
    for _ in range(4):
        G = tilt(G)
        G = rotate(G)
    return G

p1_G = tilt(G)
print('Part 1:', score(p1_G))

hist = []
for i in range(1_000_000_000):
    G = cycle(G)
    j = next((i for i in range(len(hist)) if hist[i] == G), None)
    if j:
        r = (1_000_000_000 - (j+1)) % (i-j)
        print('Part 2:', score(hist[j + r]))
        break
    hist.append(G)
    