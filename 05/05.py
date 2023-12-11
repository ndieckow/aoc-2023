import os
from helper import *

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

seeds = ints(input[0])

mapping = dict()
source = None
dest = None
acc = None
for line in input[2:]:
    if len(line) == 0:
        continue
    i = ints(line)
    if len(i) == 0:
        # store previous acc
        if acc is not None:
            mapping[(source, dest)] = sorted(acc, key = lambda x: x[1])
        source, _, dest = line.split()[0].split('-')
        acc = []
    else:
        d, s, l = ints(line)
        acc.append((d, s, l))
mapping[(source, dest)] = sorted(acc, key = lambda x: x[1]) # one final time

def convert(source, dest, num):
    ranges = mapping[(source, dest)]
    # check whether num is in any of the ranges
    for d, s, l in ranges:
        if s <= num < s + l:
            offset = num - s
            return d + offset
    # not in any of the ranges, just return it as is
    return num

def convert_range(source, dest, num_range):
    start, length = num_range
    ranges = mapping[(source, dest)]
    out_ranges = set()

    # Partition `num_range` into several ranges based on `ranges`
    # Illustrations feature the considered range from `ranges` on top, and `num_range` at the bottom
    i = 0
    while i < len(ranges) and length > 0:
        d, s, l = ranges[i]
        if start < s:
            #         [-----)
            # [-----)
            #      OR
            #   [-----)
            # [----------)
            out_ranges.add((start, min(length, s - start)))
            start = s
            length -= s - start
        elif start < s + l:
            offset = start - s
            if start + length < s + l:
                #    [-----)
                # [-----)
                out_ranges.add((d + offset, length))
                start += length
                length = 0
            else:
                # [-----)
                #    [-----)
                out_ranges.add((d + offset, s + l - start))
                length -= s + l - start
                start = s + l
                i += 1
        else:
            # [-----)
            #         [-----)
            i += 1
    # At this point, it is possible that there is still a bit of stuff left. Just add it as is.
    if length > 0:
        out_ranges.add((start, length))
    
    return out_ranges
                
def convert_full_range(seed_range):
    ranges = set([seed_range])
    for source, dest in mapping:
        ranges = set().union(*[convert_range(source, dest, num_range) for num_range in ranges])
    return ranges

def convert_full(seed):
    num = seed
    for source, dest in mapping:
        num = convert(source, dest, num)
    return num

seed_ranges = []
i = 0
while i < len(seeds)-1:
    seed_ranges.append((seeds[i], seeds[i+1]))
    i += 2

print('Part 1:', min(convert_full(seed) for seed in seeds))
print('Part 2:', min(min(x[0] for x in convert_full_range(seed_range)) for seed_range in seed_ranges))