import os
from helper import *
from math import prod

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    
    def __repr__(self):
        return (f'(x={self.x}, m={self.m}, a{self.a}, s={self.s})')

def apply_workflow(wf_name, x, m, a, s):
    if wf_name in ['R', 'A']:
        return wf_name

    wf = workflow[wf_name]
    for rule in wf:
        ifelse = rule.split(':')
        if len(ifelse) == 2:
            if eval(ifelse[0]):
                return apply_workflow(ifelse[1], x, m, a, s)
        else:
            return apply_workflow(ifelse[0], x, m, a, s)

def rangelen(rang):
    return rang[1] - rang[0] if rang[0] <= rang[1] else 0

def apply_workflow_range(wf_name, **ratings):
    if any(rangelen(r) == 0 for r in ratings.values()):
        return 0
    if wf_name in ['R', 'A']:
        return prod(rangelen(r) for r in ratings.values()) if wf_name == 'A' else 0
    
    wf = workflow[wf_name]
    result = 0
    for rule in wf:
        ifelse = rule.split(':')
        vars1, vars2 = ratings.copy(), ratings.copy()
        if len(ifelse) == 2:
            cond = ifelse[0]
            rangname = cond[0]
            rang = ratings[rangname]
            val = int(cond[2:])
            
            vars1[rangname] = (max(rang[0], val+1) if cond[1] == '>' else rang[0], min(rang[1], val) if cond[1] == '<' else rang[1])
            vars2[rangname] = (max(rang[0], val) if cond[1] == '<' else rang[0], min(rang[1], val+1) if cond[1] == '>' else rang[1])
            
            result += apply_workflow_range(ifelse[1], **vars1)
            ratings = vars2
        else:
            return result + apply_workflow_range(ifelse[0], **ratings)

ans = 0
switch = False
workflow = dict()
for line in input:
    if len(line) == 0:
        switch = True
        continue
    
    if not switch:
        name,rest = line.split('{')
        rules = rest[:-1].split(',')
        workflow[name] = rules
    else:
        ratings = line[1:-1].split(',')
        ratings = [rating.split('=') for rating in ratings]
        ratings = {r:int(num) for r,num in ratings}
        res = apply_workflow('in', **ratings)
        if res == 'A':
            ans += sum(ratings.values())

print('Part 1:', ans)

# Part 2
ratings = {name:(1,4001) for name in 'xmas'}
print('Part 2:', apply_workflow_range('in', **ratings))