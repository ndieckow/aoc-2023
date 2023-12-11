import os
from helper import *

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

grid = dict()

R, C = len(input), len(input[0])
col_counter, row_counter = Counter(), Counter()
for r,line in enumerate(input):
    for c,ch in enumerate(line):
        grid[(r,c)] = ch
        if ch == '#':
            col_counter[c] += 1
            row_counter[r] += 1
empty_cols = list(set(range(C)).difference(set(col_counter.keys())))
empty_rows = list(set(range(R)).difference(set(row_counter.keys())))

galaxies = []
for r in range(R):
    for c in range(C):
        if grid[(r,c)] == '#':
            galaxies.append((r,c))

def dist(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

def solve(res = 2):
    ans = 0
    for i,g1 in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            g2 = galaxies[j]
            bre = set(range(min(g1[0], g2[0]), max(g1[0], g2[0]))) & set(empty_rows) # number of 'super-resolution' rows that are passed
            bce = set(range(min(g1[1], g2[1]), max(g1[1], g2[1]))) & set(empty_cols) # same for columns
            blowup = len(bre) + len(bce)
            ans += dist(g1, g2) + blowup * (res - 1)
    return ans

print('Part 1:', solve())
print('Part 2:', solve(1000000))