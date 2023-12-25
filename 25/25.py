import os
from helper import *
import copy
import random
import networkx as nx

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

adj = defaultdict(set)
G = nx.Graph()
for line in input:
    words = line.split()
    comp = words[0][:-1]
    adj[comp] |= set(words[1:])
    for ocomp in adj[comp]:
        G.add_edge(comp, ocomp, capacity=1.0)
        adj[ocomp].add(comp)

def find_regions(adj):
    left = set(adj.keys())
    regions = []
    cnt = 0
    while cnt < len(adj):
        start = list(left)[0]
        q = deque([start])
        seen = set([start])
        while q:
            v = q.pop()
            for w in adj[v]:
                if w in seen:
                    continue
                seen.add(w)
                q.appendleft(w)
        regions.append(copy.deepcopy(seen))
        cnt += len(seen)
        left = left.difference(seen)
    return regions

res = nx.minimum_cut(G, 'fqt', 'krh')
print(len(res[1][0])*len(res[1][1]))