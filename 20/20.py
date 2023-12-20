import os
from helper import *
from math import lcm

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

flipflop = set()
memory = dict()

adj = defaultdict(list)
type = dict()
for line in input:
    words = line.split()
    a = words[0]
    b = [w[:-1] if w.endswith(',') else w for w in words[2:]]
    name = a[1:]
    adj[name] = b
    type[name] = a[0]
    for c in b:
        if c not in memory:
            memory[c] = dict()
        memory[c][name] = 0
    if a[0] == '&' and name not in memory:
        memory[name] = dict()

N = 1000
q = deque() # source, dest, pulse
low = 0
high = 0
press = 0

interest = ['xn', 'qn', 'xf', 'zl']
cyc = defaultdict(lambda: set())

while True:
    press += 1
    q.appendleft((None, 'roadcaster', 0))
    low += 1

    while q:
        source, dest, pulse = q.pop()

        if dest == 'rx' and pulse == 0:
            print(press)
            break

        send_pulse = -1

        if dest not in type:
            continue

        if type[dest] == '%':
            if not pulse:
                if dest in flipflop:
                    flipflop.remove(dest)
                    send_pulse = 0
                else:
                    flipflop.add(dest)
                    send_pulse = 1
        elif type[dest] == '&':
            if source:
                memory[dest][source] = pulse
            if all(memory[dest].values()):
                send_pulse = 0
            else:
                send_pulse = 1
        else:
            send_pulse = pulse
        
        # send ze pulse
        if send_pulse != -1:
            for w in adj[dest]:
                q.appendleft((dest, w, send_pulse))
                if send_pulse:
                    high += 1
                else:
                    low += 1
        
        for nm in interest:
            if 0 in memory[nm].values():
                cyc[nm].add(press)
    
    if all(len(cyc[nm]) > 2 for nm in interest): # for some reason, if there's only 2 elements, each cycle is off by one
        cycles = [sorted(list(cyc[nm])) for nm in interest]
        cycles = [a[-1] - a[-2] for a in cycles]
        print('Part 2:', lcm(*cycles))
        break

    if press == 1000:
        print('Part 1:', high * low)