import os

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

dirmap = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0),
}
DIRS = list(dirmap.keys())

V1, V2 = [(0, 0)], [(0, 0)] # vertices
bp1, bp2 = 0, 0 # boundary points
for line in input:
    d, n, color = line.split()

    n = int(n)
    dir = dirmap[d]
    bp1 += n
    V1.append((V1[-1][0] + n * dir[0], V1[-1][1] + n * dir[1]))

    color = color[1:-1]
    d = DIRS[int(color[-1])]
    dir = dirmap[d]
    n = int(eval('0x' + color[1:-1]))
    V2.append((V2[-1][0] + n * dir[0], V2[-1][1] + n * dir[1]))
    bp2 += n

# Shoelace formula
for i, (V, bp) in enumerate([(V1, bp1), (V2, bp2)]):
    A = 0
    for v,w in zip(V, V[1:]):
        A += 1/2 * (v[1] + w[1]) * (v[0] - w[0])
    print(f'Part {i+1}:', int(abs(A)) + bp // 2 + 1)