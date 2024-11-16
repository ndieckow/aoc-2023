from collections import defaultdict
from math import prod

input = open("08.in").read().strip().split('\n')

ins = input[0]

G = defaultdict(list)

for line in input[2:]:
    node,b = line.split(' = ')
    l, r = b[1:-1].split(', ')
    G[node] += [l, r]

def path_length(start, goals):
    cur = start
    i = 0
    while cur not in goals:
        dir = 0 if ins[i % len(ins)] == 'L' else 1
        cur = G[cur][dir]
        i += 1
    return i

starts = [x for x in G.keys() if x[-1] == 'A']
goals = [x for x in G.keys() if x[-1] == 'Z']

def get_factors(starts, goals, ins):
    lengths = [path_length(start, goals) for start in starts]
    return [x // len(ins) for x in lengths]

# Observation:
# All path lengths are divisible by 277, which is the length of the LR sequence.
# Each Z node has the same children as the corresponding A node, except that their L/R order is swapped.
# This turns out to continue, so that the path from ZZZ -> ZZZ has the same length as the one from AAA -> ZZZ.
# Same for the other start/end node pairs.
# Since all lengths share the number instructions (here 277) as a factor, we can just take the product of the factors and multiply by 277 to get the LCM.

print("Part 1:", path_length('AAA', ['ZZZ']))
print("Part 2:", prod(get_factors(starts, goals, ins)) * len(ins))