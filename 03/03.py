import os

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

list(range(ord('0'), ord('9') + 1)) + ['.']
symbols = []
for r,line in enumerate(input):
    for c,ch in enumerate(line):
        if not ch.isdigit() and ch != '.':
            symbols.append((r,c))

def get_ch(r,c):
    if r >= len(input) or r < 0 or c >= len(input[0]) or c < 0:
        return '.'
    return input[r][c]

adj = []
done = set()
gear_ratios = 0
for r,c in symbols:
    nums = [] # for part 2

    for (dr,dc) in [(-1,-1), (-1,0), (1,0), (-1,1), (1,-1), (1,1), (0,1), (0,-1)]:
        if input[r+dr][c+dc].isdigit():
            R,C = r+dr, c+dc
            # scan out whole number
            while 0 <= r+dr < len(input) and 0 <= c+dc < len(input[0]) and input[r+dr][c+dc].isdigit():
                dc -= 1
            dc += 1
            start_dc = dc
            while 0 <= r+dr < len(input) and 0 <= c+dc < len(input[0]) and input[r+dr][c+dc].isdigit():
                dc += 1
            end_dc = dc
            
            # check if this particular number has been found already
            if any((r+dr,c+dc) in done for dc in range(start_dc, end_dc)):
                continue
            
            for dc in range(start_dc, end_dc):
                done.add((r+dr,c+dc))
            
            number = int(''.join(input[r+dr][c+dc] for dc in range(start_dc, end_dc)))
            adj.append(number)
            
            if get_ch(r,c) == '*':
                nums.append(number)
    
    if len(nums) == 2:
        gear_ratios += nums[0]*nums[1]

print('Part 1:', sum(adj))
print('Part 2:', gear_ratios)