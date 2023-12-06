
from math import ceil, floor, sqrt

L = open('input.txt').read().split('\n')
time = int(''.join(L[0].split(':')[1].split()))
record = int(''.join(L[1].split(':')[1].split()))

# (t - i) * i > d -> i*i - it + d > 0
s = sqrt(time*time - 4*record)
x1 = (time + s) / 2
x2 = (time - s) / 2
ans = ceil(x1 - 1) - floor(x2 + 1) + 1

print(f'Solution: {ans}')
