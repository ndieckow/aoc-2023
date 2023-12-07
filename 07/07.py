import os
from helper import *
from collections import Counter

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

embedding = {x:i for i,x in enumerate(list('AKQJT98765432')[::-1])}
embedding2 = {x:i for i,x in enumerate(list('AKQT98765432J')[::-1])}

def solve(part = 1):
    embed = embedding if part == 1 else embedding2
    states = []
    for line in input:
        hand, bid = line.split()
        bid = int(bid)
        hand_emb = tuple(embed[x] for x in hand)

        c = Counter(hand)
        n_jokers = c['J']
        if part == 2:
            del c['J']
        vals = sorted(c.values())[::-1]

        if part == 1:
            kind = vals[0]
        else:
            kind = vals[0] + n_jokers if n_jokers < 5 else 5
        
        others_same = (vals[1] > 1) if kind < 5 else True

        state = (kind, others_same, hand_emb, bid)
        states.append(state)

    states = sorted(states)
    ans = 0
    for i in range(len(states)):
        ans += (i+1) * states[i][-1]
    return ans

for part in [1, 2]:
    print(f'Part {part}:', solve(part))