import os
from helper import *

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

def hash(x):
    ans = 0
    current = 0
    for ch in x:
        current += ord(ch)
        current *= 17
        current %= 256
    ans += current
    return ans

ans = 0
equations = input[0].split(',')
for eq in equations:
    ans += hash(eq)
print('Part 1:', ans)

# Part 2
boxes = [[] for _ in range(256)]
for eq in equations:
    if '=' in eq:
        label, lens = eq.split('=')
        lens = int(lens)
        
        box = boxes[hash(label)]

        already = False
        for i in range(len(box)):
            if label == box[i][1]:
                box.insert(i, (lens, label))
                del box[i+1]
                already = True
                break
        if not already:
            box.append((lens, label))
    elif '-' in eq:
        label = eq[:-1]
        box = boxes[hash(label)]
        for i in range(len(box)):
            if label == box[i][1]:
                del box[i]
                break

ans2 = 0
for i,box in enumerate(boxes):
    for j,(lens, label) in enumerate(box):
        ans2 += (1 + i) * (j + 1) * lens
print('Part 2:', ans2)