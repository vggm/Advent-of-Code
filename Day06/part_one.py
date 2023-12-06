from math import ceil, floor, sqrt

L = open('input.txt').read().split('\n')
times = list(map(int, L[0].split(':')[1].split()))
distances = list(map(int, L[1].split(':')[1].split()))

ans = 1
for (t, d) in zip(times, distances):
  # (t - i) * i > d -> -i^2 + ti - d > 0 -> i^2 - ti + d > 0
  s = sqrt(t*t - 4*d)
  x1 = (t + s) / 2
  x2 = (t - s) / 2
  ans *= ceil(x1 - 1) - floor(x2 + 1) + 1

print('Solution:', ans)
