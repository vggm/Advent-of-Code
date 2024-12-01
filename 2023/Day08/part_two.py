from functools import reduce
import math

F = open('input.txt').read().strip()
L = F.split('\n')
M = L[0]
N = {
  l.split(' = ')[0]: (l.split(' = ')[1].split(', ')[0].removeprefix('('),
                      l.split(' = ')[1].split(', ')[1].removesuffix(')'))
  for l in L[2:]
}

sources = [node for node, _ in N.items() if node.endswith('A')]
currents = sources.copy()

cnt = 0
steps = [0] * len(currents)
found = [False] * len(currents)
while not all(found):
  found = list(map(lambda n: n.endswith('Z'), currents))
  if not all(found):
    m = M[cnt % len(M)]
    for k, curr in enumerate(currents):
      if not found[k]:
        currents[k] = N[curr][0 if m == 'L' else 1]
        steps[k] = cnt + 1
    cnt += 1

print(f'Sources: {sources}')
print(f'Currents: {currents}')
print(f'NSteps: {steps}')
print(f'Total: {reduce(math.lcm, steps)}')
