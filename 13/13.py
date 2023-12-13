import os
from helper import *
from copy import deepcopy

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

def analyze(grid):
    # horizontal
    _,R,_,C = grid_bounds(grid)
    R += 1
    C += 1
    
    refls = set()
    for r in range(R - 1):
        row1 = [grid[(r,c)] for c in range(C)]
        row2 = [grid[(r+1,c)] for c in range(C)]
        if row1 != row2:
            continue
        perfect = True
        for ro in range(1, min(r + 1, R - 1 - r)):
            row1 = [grid[(r - ro,     c)] for c in range(C)]
            row2 = [grid[(r + 1 + ro, c)] for c in range(C)]
            if row1 != row2:
                perfect = False
                break
        if perfect:
            refls.add(100 * (r + 1))
    for c in range(C - 1):
        col1 = [grid[(r,c)] for r in range(R)]
        col2 = [grid[(r,c+1)] for r in range(R)]
        if col1 != col2:
            continue
        perfect = True
        for co in range(1, min(c + 1, C - 1 - c)):
            col1 = [grid[(r, c - co)] for r in range(R)]
            col2 = [grid[(r, c + co + 1)] for r in range(R)]
            if col1 != col2:
                perfect = False
                break
        if perfect:
            refls.add(c + 1)
    
    return refls

for part in [1, 2]:
    grid = defaultdict(lambda: '.')
    ans = 0
    i = 0
    r = 0
    for line in input:
        if len(line) == 0 and grid:
            i += 1

            R, C = r, c+1
            baseline = analyze(grid)
            refls = baseline.copy()
            if part == 2:
                for r in range(R):
                    for c in range(C):
                        grid2 = deepcopy(grid)
                        ch = grid2[(r,c)]
                        grid2[(r,c)] = '.' if ch == '#' else '#'
                        analysis = analyze(grid2)
                        if analysis is not None:
                            refls |= analysis
                tmp = refls.difference(baseline)
                assert len(tmp) == 1
                ans += list(tmp)[0]
            else:
                ans += list(refls)[0]
            grid = defaultdict(lambda: '.')
            r = 0
            continue
        for c,ch in enumerate(line):
            grid[(r,c)] = ch
        r += 1
    
    print(f'Part {part}: {ans}')