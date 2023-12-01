import os

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

num_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def ints(x, part=1):
    out = []
    for i,c in enumerate(x):
        if part == 2:
            for numstr,num in num_dict.items():
                if x[i:].startswith(numstr):
                    out.append(num)
        if 48 <= ord(c) <= 57:
            out.append(int(c))
    return out

for part in range(1, 3):
    ans = 0
    for line in input:
        ls = ints(line, part=part)
        val = int(str(ls[0]) + str(ls[-1]))
        ans += val
    print(f'Part {part}: {ans}')