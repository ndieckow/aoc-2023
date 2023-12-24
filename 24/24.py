import os
from sympy import solve, symbols

inpath = __file__.split(os.sep)[-1].split('.')[0] + '.in'
input = open(inpath).read().split('\n')

stones = []
for line in input:
    a, b = line.split(' @ ')
    pos = tuple(map(int, a.split(', ')))
    vel = tuple(map(int, b.split(', ')))
    stones.append((pos, vel))

test_area = (200000000000000, 400000000000000)

def is_parallel(vel1, vel2):
    return vel1[0] / vel2[0] == vel1[1] / vel2[1]

ans = 0
for i,s1 in enumerate(stones):
    for s2 in stones[i+1:]:
        p1, v1 = s1
        p2, v2 = s2
        if is_parallel(v1, v2):
            continue

        # Find a,b such that p1 + a * v1 = p2 + b * v2
        # a * v1 - b * v2 = p2 - p1
        # --> Gauss
        if v1[0] == 0:
            continue
        c = - v1[1] / v1[0]
        if (c * v2[0] - v2[1]) == 0:
            continue
        b = ((p2[1] - p1[1]) + c * (p2[0] - p1[0])) / (-c * v2[0] - v2[1])
        a = (p2[0] - p1[0] + b * v2[0]) / v1[0]

        if a < 0 or b < 0:
            continue

        if test_area[0] <= p1[0] + a * v1[0] <= test_area[1] and test_area[0] <= p1[1] + a * v1[1] <= test_area[1]:
            ans += 1
print('Part 1:', ans)

# Part 2
# we only need three stones, because that's enough to determine a line in R^3
eqs = []
p = symbols('p1 p2 p3')
v = symbols('v1 v2 v3')
t = symbols(' '.join([f't{i}' for i in range(3)]))
for i,s in enumerate(stones[:3]):
    q,w = s
    eqs += [p[j] - q[j] + t[i] * (v[j] - w[j]) for j in range(3)]
ans = solve(eqs, p + v + t, simplify=False, dict=True)
print('Part 2:', sum(ans[0][p[i]] for i in range(3)))

import numpy as np

def eval_fn(params, s, s_idx):
    # p - q + t * (v - w)
    q, w = s
    return np.array([params[i] - q[i] + params[6 + s_idx] * (params[3+i] - w[i]) for i in range(3)])

def jac(params):
    J = np.zeros((9, 9))
    tmp = np.zeros(3)
    for i in range(3):
        q, w = stones[i]
        tmp[i] = 1.0
        J[i*3 + 0] = np.concatenate(([1.0, 0.0, 0.0, params[6 + i], 0.0, 0.0], tmp * (params[3 + 0] - w[0])))
        J[i*3 + 1] = np.concatenate(([0.0, 1.0, 0.0, 0.0, params[6 + i], 0.0], tmp * (params[3 + 1] - w[1])))
        J[i*3 + 2] = np.concatenate(([0.0, 0.0, 1.0, 0.0, 0.0, params[6 + i]], tmp * (params[3 + 2] - w[2])))
        tmp[i] = 0.0
    return J

x = np.arange(9) * 100000
for _ in range(100):
    F = np.concatenate([eval_fn(x, s, i) for i,s in enumerate(stones[:3])])
    J = jac(x)
    sol = np.linalg.solve(J, -F)
    x = sol + x
x = list(map(int, x))
print('Part 2 (Newton):', sum(x[:3]))