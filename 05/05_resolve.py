# This is a re-solve of Day 5 I wrote in 2024. I haven't looked at my old solution since I wrote it last year.
# The aim of this is to create a somewhat clean solution without being in a hurry, and analyze its complexity.

from helper import ints

input = open("05.in").read().strip().split('\n')

seeds = ints(input[0])

steps = ["seed","soil","fertilizer","water","light","temperature","humidity","location"]
ranges = {}

i = 1
src, dst = None, None
while i < len(input):
    line = input[i]
    if not line:
        i += 1
        line = input[i]
        src, dst = line.split(' ')[0].split('-to-')
        ranges[(src,dst)] = []
    else:
        ranges[(src,dst)].append(tuple(ints(line)))
    i += 1

for k in ranges.keys():
    ranges[k] = sorted(ranges[k], key=lambda x: x[1])

"""
def f(x, src, dst):
    ran = ranges[(src,dst)]
    for d,s,l in ran:
        if x < s:
            return x
        elif s <= x < s + l:
            return d + (x - s)
    return x

def f_full(x):
    for s,d in zip(steps, steps[1:]):
        y = f(x, s, d)
        x = y
    return x
"""

def f_range(in_ran, src, dst):
    start, len = in_ran
    conv_ran = ranges[(src,dst)]
    out_ranges = []
    for (d,s,l) in conv_ran:
        if len <= 0:
            return out_ranges
        if start + len <= s:
            out_ranges += [(start,len)]
        elif start < s+l:
            left = (start, s-start)
            mid = (max(start,s), min(s+l, start+len) - max(start,s))
            right = (s+l, start+len-(s+l))
            # mid is guaranteed to be in the transformation range
            mid = (mid[0] - s + d, mid[1])
            out_ranges += [ran for ran in [left, mid] if ran[1] > 0]
            start, len = right
    out_ranges += [(start,len)]
    return out_ranges

def f_range_full(in_ran):
    rans = [in_ran]
    for s,d in zip(steps, steps[1:]):
        rans = [f_range(ran, s, d) for ran in rans]
        rans = [x for xx in rans for x in xx]
    return rans

def f_single_full(x):
    return min(f_range_full((x, 1)))[0]

def pair(ls):
    return [(ls[2*i], ls[2*i+1]) for i in range(len(ls) // 2)]

seed_ranges = pair(seeds)
print("Part 1:", min([f_single_full(s) for s in seeds]))
print("Part 2:", min([min(f_range_full(seed_ran))[0] for seed_ran in seed_ranges]))