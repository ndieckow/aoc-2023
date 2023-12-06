import os
from helper import *
import math

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

time = ints(input[0])
distance = ints(input[1])

ans = 1
for i in range(len(time)):
    opts = 0
    for j in range(time[i]):
        # hold down for j ms
        val = (time[i] - j) * j
        if val > distance[i]:
            opts += 1
    ans *= opts
print('Part 1:', ans)

# Part 2
time = int(''.join(str(x) for x in time))
distance = int(''.join(str(x) for x in distance))

tmp = math.sqrt(time**2 / 4 - distance)
ans2 = math.floor(time / 2 + tmp) - math.ceil(time / 2 - tmp) + 1
print('Part 2:', ans2)