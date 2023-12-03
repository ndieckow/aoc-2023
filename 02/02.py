import os
import math

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

red = 12
green = 13
blue = 14

var_map = {
    'red':red,
    'green':green,
    'blue':blue
}

for part in [1, 2]:
    ans = 0
    for line in input:
        l, r = line.split(':')
        game_id = int(l.split()[1])
        draws = r.split(';')

        faileds = []
        maxs = {'red':0, 'green':0, 'blue':0}
        for i in range(len(draws)):
            failed = False
            cubes = draws[i].split(',')
            for cube in cubes:
                val, name = cube.split()
                val = int(val)
                
                if part == 2:
                    maxs[name] = max(maxs[name], val)

                if int(val) > var_map[name]:
                    failed = True
            faileds.append(failed)
        
        if part == 1:
            if not any(faileds):
                ans += game_id
        else:
            ans += math.prod(maxs.values())
    print(f'Part {part}: {ans}')