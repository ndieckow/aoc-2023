import os
from helper import *

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

seeds = ints(input[0])
print(seeds)

map_dicts = dict()
# seed, soil, fertilizer, water, light, temperature, humidity, location
acc = []
for line in input[1:]:
    nums = ints(line)
    if len(line) > 0 and len(nums) == 0:
        if acc != []:
            acc.sort(key = lambda x: x[1])
            map_dicts[(source, dest)] = acc.copy()
            acc = []

        source, _, dest = line.split()[0].split('-')
        map_dicts[(source, dest)] = dict()
    elif len(nums) > 0:
        acc.append(tuple(nums))
map_dicts[(source, dest)] = acc
print(map_dicts)

ans = 99999999999999
cat = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
for seed in seeds:
    val = seed
    print('='*40)
    for i in range(len(cat)-1):
        print(val)
        nums = map_dicts[(cat[i], cat[i+1])]

        tmp = [x[1] for x in nums]
        if val < tmp[0] or val >= tmp[-1] + nums[-1][2]:
            val = val
        else:
            for cur in range(len(nums)):
                if val < tmp[cur]:
                    cur -= 1
                    break
                elif val == tmp[cur]:
                    break
            # now, we have found the right range
            de,so,ra = nums[cur]
            diff = val - so
            val = de + diff if diff < ra else val
    print('loc',val)
    ans = min(ans, val)
print(ans)