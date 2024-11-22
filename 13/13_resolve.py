import numpy as np

blocks = [x.split('\n') for x in open("13.in").read().strip().split('\n\n')]

arrs = []
for block in blocks:
    arr = []
    for line in block:
        arr.append([0 if x == '.' else 1 for x in line])
    arrs.append(np.array(arr))

def check_mirror_hor(block, r, part2=False):
    n = min(r+1, len(block) - r - 1)
    a = block[:r+1][::-1][:n]
    b = block[r+1:][:n]
    return abs(np.logical_xor(a, b).sum()) == part2

ans = 0
part2 = False
for i,block in enumerate(arrs):
    R, C = block.shape
    found = False
    for r in range(R-1):
        if check_mirror_hor(block, r, part2):
            ans += 100 * (r + 1)
            found = True
            break
    
    if found:
        continue
    for c in range(C-1):
        if check_mirror_hor(block.T, c, part2):
            ans += c+1
            break
print(ans)