import os
from helper import ints
from collections import Counter

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

ans = 0 # Answer for part 1
counter = Counter(range(len(input))) # Sum of values are answer for part 2
for i,line in enumerate(input):
    l,r = line.split(':')
    cardnum = int(l.split()[1])
    nums_left, nums_right = [ints(x) for x in r.split('|')]
    n_winning = len(set(nums_left).intersection(nums_right))
    if n_winning >= 1:
        ans += 2 ** (n_winning - 1)
        for j in range(1, n_winning+1):
            counter[i+j] += counter[i]

print('Part 1:', ans)
print('Part 2:', sum(counter.values()))