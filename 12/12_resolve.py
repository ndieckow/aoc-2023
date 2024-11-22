input = open('12.in').read().strip().split('\n')

def is_valid(a, nums):
    if not nums:
        return not any([x == '#' for x in a])
    
    grp = 0
    cnt = 0
    for x in a:
        if x == '#':
            cnt += 1
            if grp >= len(nums) or cnt > nums[grp]:
                return False
        else:  # x == '.'
            if cnt > 0:
                if cnt != nums[grp]:
                    return False
                grp += 1
                cnt = 0
    if grp < len(nums)-1 or grp == len(nums) - 1 and cnt != nums[-1]:
        return False
    return True


MEM = {}
def solve_brute(a, nums):
    state = (''.join(a), tuple(nums))
    if state in MEM:
        return MEM[state]
    
    if not any([x == '?' for x in a]):
        val = int(is_valid(a, nums))
        MEM[state] = val
        return val
    
    ans = 0
    grp = 0
    cnt = 0
    for i,x in enumerate(a):
        if x == '?':
            if cnt > 0:
                if grp >= len(nums):
                    break
                if cnt < nums[grp]:
                    ans = solve_brute(['#'] + list(a[i+1:]), [nums[grp] - cnt] + nums[grp+1:])
                    break
                elif cnt == nums[grp]: 
                    ans = solve_brute(['.'] + list(a[i+1:]), nums[grp+1:])
                    break
                else:
                    break
            else:
                ans = solve_brute(['#'] + list(a[i+1:]), nums[grp:]) + solve_brute(['.'] + list(a[i+1:]), nums[grp:])
                break
        elif x == '.':
            if cnt > 0:
                if grp >= len(nums) or cnt != nums[grp]:
                    break
                cnt = 0
                grp += 1
        elif x == '#':
            cnt += 1

    MEM[state] = ans
    return MEM[state]

acc = 0
for line in input:
    a, b = line.split(' ')
    nums = [int(x) for x in b.split(',')]
    n_opts = solve_brute(a, nums)
    acc += n_opts
print(acc)

# Part 2

acc = 0
for line in input:
    a, b = line.split(' ')
    a = '?'.join([a]*5)
    nums = [int(x) for x in b.split(',')]*5
    n_opts = solve_brute(a, nums)
    acc += n_opts
print(acc)