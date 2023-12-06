
L = open('input.txt').read().split('\n')
times = list(map(int, L[0].split(':')[1].split()))
distances = list(map(int, L[1].split(':')[1].split()))

ans = 1
for (t, d) in zip(times, distances):
  cnt = 0
  for i in range(1, t):
    if (t - i) * i > d:
      cnt += 1
  ans *= cnt

print('Solution:', ans)
