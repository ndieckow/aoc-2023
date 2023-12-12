import os
from helper import *
import sys

sys.setrecursionlimit(15000)

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

# solution from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/12.py
MEM = {}
cnt = 0
def dp(report, nums, state):
    global cnt
    if state in MEM:
        return MEM[state]
    idx, block, blocklen = state
    
    if idx == len(report): # we're at the end
        if (block == len(nums) and blocklen == 0) or (block == len(nums) - 1 and nums[block] == blocklen): # either we end with a '.', or a '#'
            return 1
        else:
            return 0
    
    ret = 0
    for ch in ['.', '#']:
        if report[idx] in [ch, '?']:
            if ch == '.' and blocklen == 0: # we're not in a block --> increase index
                ret += dp(report, nums, (idx + 1, block, blocklen))
            elif ch == '.' and blocklen > 0 and block < len(nums) and nums[block] == blocklen: # we are in a finished block --> start new block
                ret += dp(report, nums, (idx + 1, block + 1, 0))
            elif ch == '#':
                ret += dp(report, nums, (idx + 1, block, blocklen + 1))
    MEM[state] = ret
    return ret

for part in [1, 2]:
    ans = 0
    for line in input:
        words = line.split()
        report = words[0]
        nums = [int(x) for x in words[1].split(',')]

        if part == 2:
            report_, nums_ = report, nums.copy()
            for _ in range(4):
                report_ = ''.join(list(report_) + ['?'] + list(report))
                nums_ += nums
            report, nums = report_, nums_
        
        ans += dp(report, nums, (0, 0, 0))
        MEM.clear()
    print(f'Part {part}: {ans}')